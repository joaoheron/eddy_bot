from os import environ
from abc import ABC, abstractmethod

import numpy as np
from dotenv import load_dotenv

from eddy_bot.utils import get_credentials, get_yaml, get_comma_sepparated_values

class SocialMediaBot(ABC):
    """
        Social media bot abstract class
    """
    def __init__(self, config_path: str, profiles: str, timeout: int = 30):
        load_dotenv()
        self.timeout = timeout
        self.config = get_yaml(config_path)
        self.profiles = (get_comma_sepparated_values(profiles) if profiles else self.config.get('profiles'))
        self.tags = self.config.get('tags')
        self.comments = self.config.get('comments')
        self.descriptions = self.config.get('descriptions')

    @staticmethod
    def validate_environment(essential_vars: list):
        missing_vars = np.setdiff1d(essential_vars, environ)
        if missing_vars:
            raise Exception(f'Missing variables: {missing_vars}. Please export all the needed environment variables.')
