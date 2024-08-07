# src/driver_manager.py

import os
import json

class ConfigLoader:
    def __init__(self):
        self.env = os.getenv('ENV', 'development')
        self.config = self.load_config()

    def load_config(self):
        config_file = f'config/config_{self.env}.json'
        with open(config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

config_loader = ConfigLoader()
