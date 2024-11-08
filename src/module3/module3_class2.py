from config import Config

class Module3Class2:
    def __init__(self, config: Config):
        self.config = config

    def set_session_id(self, session_id):
        self.config.set_dynamic_param('session_id', session_id)
        print(f"Session ID set to: {session_id}")
