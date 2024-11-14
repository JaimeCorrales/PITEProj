from models import FootballPlayer
from config import Config
from service import FootballStatsService
from yaml_help import save_to_yaml, load_from_yaml
import threading
import time

class FootballStatsClient:
    def __init__(self, config, storage_file="players_data.yaml"):
        self.config = config
        self.logger = config.get("logger")
        self.storage_file = storage_file
        self.players = load_from_yaml(self.storage_file)  # Load existing player data from YAML file
        self.service = FootballStatsService(config)

    def process_player_data(self, player_stats):
        """Process and filter player data, then store in YAML"""
        if player_stats:
            player = FootballPlayer(player_stats)
            if player.is_valid():
                self.logger.info(f"Processing player: {player}")
                self.players.append(player.to_dict())  # Add player data to the list of players
                self.save_players_data()  # Save data to YAML after adding a player
            else:
                self.logger.warning(f"Invalid data for player {player.player_id}")

    def save_players_data(self):
        """Save the current list of players to the YAML file"""
        save_to_yaml(self.players, self.storage_file)

    def start(self):
        """Start the client and begin data processing"""
        self.logger.info("Client started")
        self.service.start_fetching()

    def add_player(self, player_stats):
        """Simulate adding a player to the client's dataset"""
        self.process_player_data(player_stats)
