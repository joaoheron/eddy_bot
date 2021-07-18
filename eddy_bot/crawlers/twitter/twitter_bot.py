from os import getenv, path, environ

import tweepy
import numpy as np

from eddy_bot.logger import logger
from eddy_bot.utils import pick_random_resource
from eddy_bot.models.social_media_bot import SocialMediaBot

class TwitterBot(SocialMediaBot):
    """
        Twitter tweepy api bot class
    """
    def __init__(self, config_path: str, profiles: str, timeout: int = 30):
        SocialMediaBot.__init__(self, config_path, profiles)
        SocialMediaBot.validate_environment(['CONSUMER_API_KEY', 'CONSUMER_API_SECRET_KEY', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET'])
        self.auth = tweepy.OAuthHandler(
            getenv('CONSUMER_API_KEY'),
            getenv('CONSUMER_API_SECRET_KEY')
        )
        self.auth.set_access_token(
            getenv('ACCESS_TOKEN'),
            getenv('ACCESS_TOKEN_SECRET')
        )
        self.api = tweepy.API(self.auth)

    def verify_authentication(function):
        def verify(self, *args, **kwargs):
            try:
                logger.info("Verifying credentials...")
                self.api.verify_authentication()
                logger.info("Authentication OK.")
            except Exception as ex:
                raise ex("Error during authentication.")

            function(self, *args, **kwargs)

        return verify

    @verify_authentication
    def follow(self):
        try:
            for p in self.profiles:
                logger.info(f'Following @{p} ...')
                self.api.create_friendship(p)
        except Exception as ex:
            raise ex('Error during following user.')

    @verify_authentication
    def unfollow(self):
        try:
            for p in self.profiles:
                logger.info(f'Unfollowing @{p} ...')
                self.api.destroy_friendship(p)
        except Exception as ex:
            raise ex('Error during unfollowing user.')

    @verify_authentication
    def tweet(self, tweet: str, mediapath: str):
        kmids = {}
        try:
            if tweet is None:
                tweet = pick_random_resource(self.comments)
            if path.isfile(mediapath):
                media = self.api.media_upload(mediapath)
                kmids['media_ids'] = [media.media_id_string]

            logger.info(f'Tweeting \"{tweet}\" ...')
            self.api.update_status(tweet, **kmids)

        except Exception as ex:
            raise ex('Error during tweeting.')

    @verify_authentication
    def update_profile(self, description: str, picture_update: str, mediapath: str):
        try:
            if description is not None:
                logger.info(f'Updating profile with description \"{description}\"')
                self.api.update_profile(description)
                logger.info('Profile description updated.')

            if path.isfile(mediapath) and picture_update:
                logger.info(f'Updating profile picture ... ')
                self.api.update_profile_image(mediapath)
                logger.info('Profile picture updated.')

        except Exception as ex:
            raise ex('Error during updating profile picture.')
