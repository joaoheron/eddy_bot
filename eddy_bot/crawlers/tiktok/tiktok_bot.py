import pathlib
from os import getenv, path, system

import numpy as np

from eddy_bot.logger import logger
from eddy_bot.models.social_media_bot import SocialMediaBot

class TiktokBot(SocialMediaBot):
    """
        TiktokBot xdotool bot class
    """
    def __init__(self, config_path: str, profiles: str, timeout: int = 30):
        SocialMediaBot.__init__(self, config_path, profiles)
        TiktokBot.validate_environment(['TIKTOK_USER', 'TIKTOK_PASS'])

    def login(self):
        try:
            logger.info(f'Logging in...')
            system(f'sh {pathlib.Path(__file__).parent.resolve()}/scripts/login_xdo.sh')
        except Exception as ex:
            raise ex

    def follow(self):
        try:
            for p in self.profiles:
                logger.info(f'Following @{p} ...')
                system(f'sh {pathlib.Path(__file__).parent.resolve()}/scripts/follow_xdo.sh')
        except Exception as ex:
            raise ex

    def unfollow(self):
        try:
            for p in self.profiles:
                logger.info(f'Unfollowing @{p} ...')
                system(f'sh {pathlib.Path(__file__).parent.resolve()}/scripts/unfollow_xdo.sh')
        except Exception as ex:
            raise ex
