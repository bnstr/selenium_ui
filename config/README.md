
## Support for multiple environments. 
```
project_root/
├── config/
│   ├── config_dev.json
│   ├── config_test.json
│   ├── config_prod.json
├── data/
│   ├── test_data_dev.json
│   ├── test_data_test.json
│   ├── test_data_prod.json
```

### Configuration Management
##### Configuration Files
Each environment has its own configuration file stored in the config directory:

config_dev.json:
```
{
  "base_url": "http://dev.example.com",
  "credentials": {
    "username": "dev_user",
    "password": "dev_pass"
  },
  "other_settings": {}
}

```

##### Environment Variables
Use environment variables to dynamically select the environment. For example, you can set ENV as an environment variable in your CI/CD pipeline:
```
export ENV=development
```
##### Configuration Loader
Create a configuration loader that reads the correct file based on the environment variable:

```
# src/config_loader.py

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

```
### Test Data Management
Create a test data manager that handles environment-specific data:
```
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


```

### Test Suite Example
```
# tests/test_suite.py

from src.config_loader import config_loader
from src.test_data_manager import test_data_manager
from src.environment import environment

def test_example():
    base_url = config_loader.get('base_url')
    credentials = config_loader.get('credentials')

    print(f"Testing on: {base_url}")
    print(f"Using credentials: {credentials}")

    test_data = test_data_manager.get_test_data('sample_data')
    print(f"Test data: {test_data}")

    environment.execute_task()

if __name__ == "__main__":
    test_example()

```

This project structure allows you to manage multiple environments effectively by:

1) Separating Configuration Files: Each environment has its own configuration file with environment-specific settings.
2) Using Environment Variables: Select the active environment dynamically, useful for local testing and CI/CD.
3) Creating a Configuration Loader: Load configurations and test data based on the active environment.
