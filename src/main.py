import time
from config import Config
from log_setup import setup_logging
from client import FootballStatsClient
import logging

def main():
    
    logging.basicConfig(
    filename='app.log',          
    level=logging.DEBUG,         
    format='%(asctime)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'   
)
    
    # Load configuration from the YAML file
    config = Config(config_file="config.yaml")
    logger = setup_logging(log_level=config.get("log_level"), log_file=config.get("log_file"))
    config.config["logger"] = logger

    # Create and start the client
    client = FootballStatsClient(config)
    client.start()

    # Simulate some wait time to let threads complete
    time.sleep(20)

if __name__ == "__main__":
    main()

