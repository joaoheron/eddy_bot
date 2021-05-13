from random import randint, choice
from yaml import load, FullLoader

def get_credentials(path):
    with open(path, 'r') as f:
        tagsl = [line.strip() for line in f]
    return tagsl[0], tagsl[1]
    
def get_resource(path):
    with open(path, 'r') as f:
        resources = [line.strip() for line in f]
    return resources

def get_yaml(path):
    with open(path) as yaml_file:
        obj = load(yaml_file, Loader=FullLoader)
        return obj

def pick_random_resource(self, resource):
    res = choice(resource)
    return res
