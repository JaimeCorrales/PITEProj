import yaml

class Config:
    def __init__(self, config_file="config.yaml"):
        self.config_file = config_file
        self.static_params = {}
        self.dynamic_params = {}

        self.load_config()

    def load_config(self):
        
        with open(self.config_file, "r") as file:
            config_data = yaml.safe_load(file)

        
        self.static_params = config_data.get("static_params", {})
        self.dynamic_params = config_data.get("dynamic_params", {})

    def set_dynamic_param(self, param, value):
        """Set a dynamic configuration parameter."""
        if param in self.dynamic_params:
            self.dynamic_params[param] = value
        else:
            print(f"Warning: {param} is not a valid dynamic parameter.")

    def get_config(self):
        """Return the merged static and dynamic configurations."""
        return {**self.static_params, **self.dynamic_params}
