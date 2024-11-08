from config import Config

class Module1Class2:
    def __init__(self, config: Config):
        self.config = config

    def log_message(self, message):
        log_level = self.config.static_params['log_level']
        print(f"[{log_level}] {message}")
