from config import Config

class Module1Class1:
    def __init__(self, config: Config):
        self.config = config

    def connect_db(self):
        db_host = self.config.static_params['db_host']
        db_port = self.config.static_params['db_port']
        print(f"Connecting to DB at {db_host}:{db_port}")

    def show_user(self):
        current_user = self.config.dynamic_params['current_user']
        print(f"Current user: {current_user}")
