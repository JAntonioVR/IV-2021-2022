from configparser import ConfigParser

def read_config_file(path):
    config = ConfigParser()
    config.read(path)
    dataset = config['DATA']['dataset']
    logging = config['LOGGING'].getboolean('log')
    log_output = None
    if(logging):
        log_output = config['LOGGING']['output']
    debug = config['DEBUG'].getboolean('debug')
    return {
        'dataset': dataset,
        'logging': logging,
        'log_output': log_output,
        'debug': debug
    }
