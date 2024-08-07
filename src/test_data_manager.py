# src/test_data_manager.py

import json

class TestDataManager:
    def __init__(self, env):
        self.env = env
        self.test_data = self.load_test_data()

    def load_test_data(self):
        data_file = f'data/test_data_{self.env}.json'
        with open(data_file, 'r') as file:
            return json.load(file)

    def get_test_data(self, key, default=None):
        return self.test_data.get(key, default)

# Initialize test data manager
test_data_manager = TestDataManager(os.getenv('ENV', 'development'))
