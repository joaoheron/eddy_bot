from os import getenv, path

import numpy as np

from eddy_bot.models.social_media_bot import SocialMediaBot

# sudo apt-get install xautomation wmctrl
# sudo apt-get install xdotool

class TiktokBot(SocialMediaBot):

    def __init__(self, config_path: str, profiles: str, timeout: int = 30):
        SocialMediaBot.__init__(self, config_path, profiles)
        self.validate_env_vars(['TIKTOK_USER', 'TIKTOK_PASS'])
