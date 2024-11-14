import yaml
import os

class Config:
    def __init__(self, config_file="config.yaml"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from YAML file"""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, "r") as file:
            config_data = yaml.safe_load(file)
        
        # If dynamic config is set, update it
        if "dynamic_config" in config_data:
            self.dynamic_config = config_data["dynamic_config"]
        else:
            self.dynamic_config = {}
        
        return config_data

    def get(self, key):
        """Get a configuration value"""
        return self.config.get(key, None)
    
    def get_all(self):
        """Get all configuration settings"""
        return self.config
    
    def update_dynamic_config(self, key, value):
        """Update dynamic configuration settings"""
        self.dynamic_config[key] = value
        self.config["dynamic_config"] = self.dynamic_config
        # You can optionally write back the updated config to YAML file if desired
        self.save_config()

    def save_config(self):
        """Save the current config to the YAML file"""
        with open(self.config_file, "w") as file:
            yaml.dump(self.config, file)

