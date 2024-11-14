import threading
import time
from service import FootballStatsService
from models import FootballPlayer
from config import Config

class FootballStatsClient:
    def __init__(self, config):
        self.config = config
        self.logger = config.get("logger")
        self.service = FootballStatsService(config)
        self.players = []

    def process_player_data(self, player_stats):
        """Process and filter player data"""
        if player_stats:
            player = FootballPlayer(player_stats)
            if player.is_valid():
                self.logger.info(f"Processing player: {player.player_id}")
                self.players.append(player)
            else:
                self.logger.warning(f"Invalid data for player {player.player_id}")

    def start(self):
        """Start the client and begin data processing"""
        self.logger.info("Client started")
        self.service.start_fetching()

    def add_player(self, player_stats):
        """Simulate adding a player to the client's dataset"""
        self.process_player_data(player_stats)
