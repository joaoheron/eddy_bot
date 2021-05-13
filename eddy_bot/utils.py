from random import randint, choice

def get_credentials(path):
    with open(path, 'r') as f:
        tagsl = [line.strip() for line in f]
    return tagsl[0], tagsl[1]
    
def get_resource(path):
    with open(path, 'r') as f:
        resources = [line.strip() for line in f]
    return resources

def pick_random_resource(self, resource):
    res = choice(resource)
    return res
