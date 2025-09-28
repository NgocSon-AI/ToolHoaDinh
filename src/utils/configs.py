import os
import yaml
from dotenv import load_dotenv


class ConfigLoader():
    """
        Class responsible for loading configuration from yaml and .env
    """

    def __init__(self, config_path = "../configs/config.yaml"):
        load_dotenv()
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, key: str, default=None):
        return self.config.get(key, default)
    
    def env_resolve(self, value: str):
        """
        Args:
            - value string in YAML
        Returns:
            - 
        """
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            env_key = value[2:-1]
            return os.getenv(env_key)

        return value