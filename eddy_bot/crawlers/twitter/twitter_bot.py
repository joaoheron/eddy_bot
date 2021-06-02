from os import getenv

import tweepy

from eddy_bot.models.social_media_bot import SocialMediaBot
from eddy_bot.utils import pick_random_resource

class TwitterBot(SocialMediaBot):

    def __init__(self, credentials_path, config_path, timeout=30):
        SocialMediaBot.__init__(self, credentials_path, config_path)
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
            self.api.verify_credentials()
            print("Authentication OK.")
        except Exception as ex:
            raise ex("Error during authentication.")

    def tweet(self, tweet=None):
        self.verify_credentials()
        try:
            if tweet is None:
                tweet = pick_random_resource(self.comments)
            self.api.update_status(tweet)
        except Exception as ex:
            raise ex

    def follow(self, profile=None):
        self.verify_credentials()
        try:
            if tweet is None:
                profile = pick_random_resource(self.profiles)
            self.api.create_friendship(profile)
        except Exception as ex:
            raise ex

    def update_profile_description(self, description=None):
        self.verify_credentials()
        try:
            if description is None:
                profile = pick_random_resource(self.descriptions)
            self.api.update_profile(profile)
        except Exception as ex:
            raise ex
