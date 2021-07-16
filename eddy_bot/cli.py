"""Console script for eddy_bot."""
import sys
import click
import eddy_bot.vars as vr

from eddy_bot.crawlers.tiktok.tiktok_bot import TiktokBot
from eddy_bot.crawlers.twitter.twitter_bot import TwitterBot
from eddy_bot.crawlers.instagram.instagram_bot import InstagramSeleniumBot

@click.group()
def cli():
    pass

@click.command()
@click.option('--comment', '-c', default='This is a comments', help='Comment to be posted', required=False)
@click.option('--follow', '-f', help='Flag to follow profiles', is_flag=True, required=False)
@click.option('--unfollow', '-u', help='Flag to unfollow profiles', is_flag=True, required=False)
@click.option('--profiles', '-p', default='instagram', help='Profiles to perform the actions over, sepparated by commas(,)', required=False)
@click.option('--config-path', '-conf', default=vr.config_path, help='Configuration file path', required=False)
def instagram(comment, follow, unfollow, profiles, config_path):
    """
        Build instagram bot.
    """
    try:
        bot = InstagramSeleniumBot(config_path=config_path, profiles=profiles)
        bot.login()
        if comment is not None:
            bot.comment_profiles_posts()
        if follow is not None:
            bot.follow()
        elif unfollow is not None:
            bot.unfollow()
    except Exception as e:
        raise e

@click.command()
@click.option('--tweet', '-t', help='Message to be tweeted', required=False)
@click.option('--mediapath', '-m', help='Path of the file to be tweeted', required=False)
@click.option('--follow', '-f', help='Flag to follow profiles', is_flag=True, required=False)
@click.option('--unfollow', '-u', help='Flag to unfollow profiles', is_flag=True, required=False)
@click.option('--bio-update', '-b', help='Message to update self profile description', required=False)
@click.option('--picture-update', '-pu', help='Message to update self profile description', is_flag=True, required=False)
@click.option('--profiles', '-p', default='instagram', help='Profiles to perform the actions over, sepparated by commas(,)', required=False)
@click.option('--config-path', '-c', default=vr.config_path, help='Configuration file path', required=False)
def twitter(tweet, mediapath, follow, unfollow, bio_update, picture_update, profiles, config_path):
    """
        Build twitter bot.
    """
    try:
        bot = TwitterBot(config_path=config_path, profiles=profiles)
        if tweet is not None:
            bot.tweet(tweet, mediapath)
        if bio_update is not None or picture_update is not None:
            bot.update_profile(bio_update, picture_update, mediapath)
        if follow is not None:
            bot.follow()
        elif unfollow is not None:
            bot.unfollow()
    except Exception as e:
        raise e

@click.command()
@click.option('--follow', '-f', help='Flag to follow profiles', is_flag=True, required=False)
@click.option('--unfollow', '-u', help='Flag to unfollow profiles', is_flag=True, required=False)
@click.option('--profiles', '-p', default='instagram', help='Profiles to perform the actions over, sepparated by commas(,)', required=False)
@click.option('--config-path', '-c', default=vr.config_path, help='Configuration file path', required=False)
def tiktok(follow, unfollow, profiles, config_path):
    """
        Build tiktok bot.
    """
    try:
        bot = TiktokBot(config_path=config_path, profiles=profiles)
        bot.login()
        if follow is not None:
            bot.follow()
        elif unfollow is not None:
            bot.unfollow()
    except Exception as e:
        raise e

cli.add_command(instagram)
cli.add_command(twitter)
cli.add_command(tiktok)

if __name__ == "__main__":
    sys.exit(cli()) # pragma: no cover
