from eddy_bot.utils import get_resource, get_credentials, get_yaml

class SocialMediaBot():

    def __init__(self, credentials_path, tags_path, profiles_path, comments_path):
        self.username, self.password = get_credentials(credentials_path)
        self.tags = get_resource(tags_path)
        self.profiles = get_resource(profiles_path)
        self.comments = get_resource(comments_path)

    def __init__(self, credentials_path, config_path):
        self.username, self.password = get_credentials(credentials_path)
        self.config = get_yaml(config_path)
        self.tags = self.config.get('tags')
        self.profiles = self.config.get('profiles')
        self.comments = self.config.get('comments')
