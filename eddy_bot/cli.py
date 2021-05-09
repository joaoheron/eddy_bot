"""Console script for eddy_bot."""
import os
import sys
import click

from eddy_bot.crawlers.instagram.selenium_crawler import get_data


@click.group()
def cli():
    pass

@click.command()
@click.option('--action', '-a', default='comment', help='Action to be executed over this social media', required=True)
def instagram(action):
    """
        Build decision tree.
    """
    try:
        get_data()
    except Exception as e:
        raise e

cli.add_command(instagram)

if __name__ == "__main__":
    sys.exit(cli()) # pragma: no cover
