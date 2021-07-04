from abc import ABC

from eddy_bot.utils import get_resource, get_credentials, get_yaml

class SocialMediaBot(ABC):

    def __init__(self, credentials_path: str, config_path: str, timeout: int=30):
        self.timeout = timeout
        self.username, self.password = get_credentials(credentials_path)
        self.config = get_yaml(config_path)
        self.tags = self.config.get('tags')
        self.profiles = self.config.get('profiles')
        self.comments = self.config.get('comments')
        self.descriptions = self.config.get('descriptions')
