import yaml

def configreader(configfile):
    '''
    opens dbconfig.yaml to get user, password, host and db
    '''
    with open(configfile, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    postgres = cfg['postgres']
    user = postgres['user']
    host = postgres['host']
    password = str(postgres['passwd'])
    db = postgres['db']
    return user, host, password, db
