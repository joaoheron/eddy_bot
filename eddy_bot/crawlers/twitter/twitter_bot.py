from os import getenv, path

import tweepy

from eddy_bot.logger import logger
from eddy_bot.utils import pick_random_resource
from eddy_bot.models.social_media_bot import SocialMediaBot

class TwitterBot(SocialMediaBot):

    def __init__(self, credentials_path: str, config_path: str, profiles: str, timeout: int = 30):
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
    
    def verify_credentials(function):
        def verify(self, *args, **kwargs):
            try:
                logger.info("Verifying credentials...")
                self.api.verify_credentials()
                logger.info("Authentication OK.")
            except Exception as ex:
                raise ex("Error during authentication.")

            function(self, *args, **kwargs)

        return verify

    @verify_credentials
    def tweet(self, tweet: str = None, mediapath: str = None):
        kmids = {}
        try:
            if tweet is None:
                tweet = pick_random_resource(self.comments)
            if path.isfile(mediapath):
                media = self.api.media_upload(mediapath)
                kmids['media_ids'] = [media.media_id_string]

            logger.info(f'Tweeting \" {tweet} \" ...')
            self.api.update_status(tweet, **kmids)

        except Exception as ex:
            raise ex

    @verify_credentials
    def follow(self):
        try:
            for p in self.profiles:
                logger.info(f'Following {p} ...')
                self.api.create_friendship(p)

        except Exception as ex:
            raise ex

    @verify_credentials
    def update_profile_description(self, description: str):
        try:
            if description is None:
                description = pick_random_resource(self.descriptions)
            logger.info(f'Updating profile with description \" {description} \"')    
            self.api.update_profile(description)
        except Exception as ex:
            raise ex
