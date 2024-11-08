from config import Config

class Module3Class1:
    def __init__(self, config: Config):
        self.config = config

    def get_db_host(self):
        db_host = self.config.static_params['db_host']
        print(f"DB Host: {db_host}")
