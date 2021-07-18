import pathlib
from os import getenv, path, system

import numpy as np

from eddy_bot.logger import logger
from eddy_bot.models.social_media_bot import SocialMediaBot

class TiktokBot(SocialMediaBot):
    """
        TiktokBot xdotool bot class
    """
    scripts_folder = 'eddy_bot/crawlers/tiktok/scripts'

    def __init__(self, config_path: str, profiles: str, timeout: int = 30):
        SocialMediaBot.__init__(self, config_path, profiles)
        TiktokBot.validate_environment(['TIKTOK_USER', 'TIKTOK_PASS'])

    def login(function):
        def login_tiktok(self, *args, **kwargs):
            try:
                logger.info(f'Logging in...')
                system(f'sh {TiktokBot.scripts_folder}/login_xdo.sh')
            except Exception as ex:
                raise ex

            function(self, *args, **kwargs)

        return login_tiktok

    def _close(self):
        try:
            system(f'sh {TiktokBot.scripts_folder}/close_chrome_xdo.sh')
        except Exception as ex:
            raise ex

    @login
    def follow(self):
        try:
            for p in self.profiles:
                logger.info(f'Following @{p} ...')
                system(f'sh {TiktokBot.scripts_folder}/follow_xdo.sh {p}')
        except Exception as ex:
            raise ex
        finally:
            self._close()

    @login
    def unfollow(self):
        try:
            for p in self.profiles:
                logger.info(f'Unfollowing @{p} ...')
                system(f'sh {TiktokBot.scripts_folder}/unfollow_xdo.sh')
        except Exception as ex:
            raise ex
        finally:
            self._close()