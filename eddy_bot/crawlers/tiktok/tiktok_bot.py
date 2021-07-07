from os import getenv, path

from eddy_bot.models.social_media_bot import SocialMediaBot

class TwitterBot(SocialMediaBot):

    def __init__(self, credentials_path: str, config_path: str, profiles: str, timeout: int = 30):
        SocialMediaBot.__init__(self, credentials_path, config_path, profiles)
