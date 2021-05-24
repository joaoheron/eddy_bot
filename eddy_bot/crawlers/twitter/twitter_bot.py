from os import getenv

import tweepy

from eddy_bot.models.social_media_bot import SocialMediaBot
import eddy_bot.vars as vr


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
        
    def tweet():
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
