import yaml
import os

def save_to_yaml(data, filename):
    """Save the player data to a YAML file"""
    with open(filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

def load_from_yaml(filename):
    """Load player data from a YAML file"""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return yaml.safe_load(file) or []  # Return an empty list if the file is empty
    return []  # Return an empty list if the file doesn't exist
