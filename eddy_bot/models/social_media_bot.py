from eddy_bot.utils import get_resource, get_credentials

class SocialMediaBot():

    def __init__(self, credentials_path, tags_path, profiles_path, comments_path):
        self.username, self.password = get_credentials(credentials_path)
        self.tags = get_resource(tags_path)
        self.profiles = get_resource(profiles_path)
        self.comments = get_resource(comments_path)
