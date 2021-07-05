"""Console script for eddy_bot."""
import sys
import click
import eddy_bot.vars as vr

from eddy_bot.crawlers.instagram.instagram_bot import InstagramSeleniumBot
from eddy_bot.crawlers.twitter.twitter_bot import TwitterBot

@click.group()
def cli():
    pass

@click.command()
@click.option('--comment', '-c', default='This is a comment', help='Comment to be posted', required=False)
@click.option('--follow', '-f', help='Flag to follow profile', is_flag=True, required=False)
@click.option('--profiles', '-p', default='instagram', help='Profiles to perform the actions over, sepparated by commas(,)', required=False)
@click.option('--credentials-path', '-cred', default=vr.credentials_path, help='Credentials file path', required=False)
@click.option('--config-path', '-conf', default=vr.config_path, help='Configuration file path', required=False)
def instagram(comment, follow, profiles, credentials_path, config_path):
    """
        Build instagram bot.
    """
    try:
        bot = InstagramSeleniumBot(credentials_path=credentials_path, config_path=config_path, profiles=profiles)
        bot.login()
        if comment is not None:
            bot.comment_profiles_posts(profiles)
        if follow is not None:
            bot.follow()
    except Exception as e:
        raise e

@click.command()
@click.option('--tweet', '-t', help='Message to be tweeted', required=False)
@click.option('--mediapath', '-m', help='Path of the file to be tweeted', required=False)
@click.option('--follow', '-f', help='Flag to follow profile', is_flag=True, required=False)
@click.option('--profiles', '-p', default='instagram', help='Profiles to perform the actions over, sepparated by commas(,)', required=False)
@click.option('--credentials-path', '-cr', default=vr.credentials_path, help='Credentials file path', required=False)
@click.option('--config-path', '-c', default=vr.config_path, help='Configuration file path', required=False)
def twitter(tweet, mediapath, follow, profiles, credentials_path, config_path):
    """
        Build twitter bot.
    """
    try:
        bot = TwitterBot(credentials_path=credentials_path, config_path=config_path, profiles=profiles)
        if tweet is not None:
            bot.tweet(tweet, mediapath)
        if follow is not None:
            bot.follow()
    except Exception as e:
        raise e

cli.add_command(instagram)
cli.add_command(twitter)

if __name__ == "__main__":
    sys.exit(cli()) # pragma: no cover
