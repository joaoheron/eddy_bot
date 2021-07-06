from abc import ABC

from dotenv import load_dotenv

from eddy_bot.utils import get_credentials, get_yaml, get_comma_sepparated_values

class SocialMediaBot(ABC):

    def __init__(self, credentials_path: str, config_path: str, profiles: str, timeout: int = 30):
        load_dotenv()
        self.timeout = timeout
        self.username, self.password = get_credentials(credentials_path)
        self.config = get_yaml(config_path)
        self.profiles = (get_comma_sepparated_values(profiles) if profiles else self.config.get('profiles'))
        self.tags = self.config.get('tags')
        self.comments = self.config.get('comments')
        self.descriptions = self.config.get('descriptions')
