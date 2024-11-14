import threading
import time
import requests
from config import Config
from models import FootballPlayer

class FootballStatsService:
    def __init__(self, config):
        self.config = config
        self.logger = config.get("logger")
        self.api_url = config.get("api_url")
        self.api_key = config.get("api_key")
        self.retry_count = config.get("retry_count")
        self.timeout = config.get("timeout")
        self.players_data = []

    def fetch_player_stats(self, player_id):
        """Fetch real player stats using API"""
        headers = {"X-Auth-Token": self.api_key}
        url = f"{self.api_url}/{player_id}"
        attempts = 0
        while attempts < self.retry_count:
            try:
                self.logger.debug(f"Fetching data for player {player_id}")
                response = requests.get(url, headers=headers, timeout=self.timeout)
                if response.status_code == 200:
                    data = response.json()
                    player_stats = self.extract_player_data(data)
                    self.logger.info(f"Fetched data for player {player_id}: {player_stats}")
                    return player_stats
                else:
                    self.logger.warning(f"Failed to fetch data for player {player_id}, Status code: {response.status_code}")
                    attempts += 1
                    time.sleep(5)  # Wait before retrying
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Error fetching data for player {player_id}: {e}")
                attempts += 1
                time.sleep(2)  # Wait before retrying
        return None

    def extract_player_data(self, data):
        """Extract relevant player statistics from API response"""
        try:
            player_data = {                
                "id": data["id"],
                "name": data["name"],
                "firstName": data["firstName"],
                "lastName": data["lastName"],
                "dateOfBirth": data["dateOfBirth"],
                "nationality": data["nationality"],
                "position": data["position"],
                "shirtNumber": data["shirtNumber"],
            }
            return player_data
        except KeyError as e:
            self.logger.error(f"Error extracting player data: missing key {e}")
            return None

    def start_fetching(self):
        """Start the service to fetch player stats"""
        self.logger.info("Service started")
        for player_id in range(1, 6):  # Example: Fetching stats for 5 players
            threading.Thread(target=self.fetch_player_stats, args=(player_id,)).start()
            time.sleep(self.config.get("polling_interval"))
