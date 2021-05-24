"""Console script for eddy_bot."""
import os
import sys
import click
import eddy_bot.vars as vr

from eddy_bot.crawlers.instagram.instagram_bot import InstagramSeleniumBot
from eddy_bot.crawlers.twitter.twitter_bot import TwitterBot

@click.group()
def cli():
    pass

@click.command()
@click.option('--action', '-a', default='comment', help='Action to be executed over this social media', required=True)
@click.option('--credentials-path', '-cr', default=vr.credentials_path, help='Credentials file path', required=False)
@click.option('--config-path', '-c', default=vr.config_path, help='Configuration file path', required=False)
def instagram(action, credentials_path, config_path):
    """
        Build decision tree.
    """
    try:
        bot = InstagramSeleniumBot(credentials_path=credentials_path, config_path=config_path)
        bot.login()
        bot.comment_profiles_posts()
    except Exception as e:
        raise e

@click.command()
@click.option('--action', '-a', default='tweet', help='Action to be executed over this social media', required=True)
@click.option('--credentials-path', '-cr', default=vr.credentials_path, help='Credentials file path', required=False)
@click.option('--config-path', '-c', default=vr.config_path, help='Configuration file path', required=False)
def twitter(action, credentials_path, config_path):
    """
        Build decision tree.
    """
    try:
        bot = TwitterBot(credentials_path=credentials_path, config_path=config_path)
        bot.tweet()
    except Exception as e:
        raise e

cli.add_command(instagram)
cli.add_command(twitter)

if __name__ == "__main__":
    sys.exit(cli()) # pragma: no cover
