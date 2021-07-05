from os import getenv, path

import tweepy

from eddy_bot.logger import logger
from eddy_bot.utils import pick_random_resource
from eddy_bot.models.social_media_bot import SocialMediaBot

class TwitterBot(SocialMediaBot):

    def __init__(self, credentials_path: str, config_path: str, profiles: str, timeout: int=30):
        SocialMediaBot.__init__(self, credentials_path, config_path, profiles)
        self.auth = tweepy.OAuthHandler(
            getenv('CONSUMER_API_KEY'),
            getenv('CONSUMER_API_SECRET_KEY')
        )
        self.auth.set_access_token(
            getenv('ACCESS_TOKEN'),
            getenv('ACCESS_TOKEN_SECRET')
        )
        self.api = tweepy.API(self.auth)

    def verify_credentials(self):
        try:
            logger.info("Verifying credentials...")
            self.api.verify_credentials()
            logger.info("Authentication OK.")
        except Exception as ex:
            raise ex("Error during authentication.")

    def tweet(self, tweet: str=None, mediapath: str=None):
        self.verify_credentials()
        kmids = {}
        try:
            if tweet is None:
                tweet = pick_random_resource(self.comments)
            if path.isfile(mediapath):
                media = self.api.media_upload(mediapath)
                kmids['media_ids'] = [media.media_id_string]

            self.api.update_status(tweet, **kmids)

        except Exception as ex:
            raise ex

    def follow(self, profiles: str=None):
        self.verify_credentials()
        try:
            if profiles is not None and len(profiles) > 0:
                self.profiles = profiles
            for p in self.profiles:
                self.api.create_friendship(p)

        except Exception as ex:
            raise ex

    def update_profile_description(self, description: str=None):
        self.verify_credentials()
        try:
            if description is None:
                description = pick_random_resource(self.descriptions)
            self.api.update_profile(description)
        except Exception as ex:
            raise ex
