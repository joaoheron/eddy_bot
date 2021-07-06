from random import choice
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

def pick_random_resource(resources):
    res = choice(resources)
    return res

def get_comma_sepparated_values(values):
    return [x.strip() for x in values.split(',')]
