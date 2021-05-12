
def get_credentials():
    with open(vr.credentials_path, 'r') as f:
        tagsl = [line.strip() for line in f]
    return tagsl[0], tagsl[1]
    
def get_resource(path):
    with open(path, 'r') as f:
        resources = [line.strip() for line in f]
    return resources
