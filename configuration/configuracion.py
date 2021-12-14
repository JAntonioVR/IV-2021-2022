from configparser import ConfigParser

def read_config_file(path):
    config = ConfigParser()
    config.read(path)
    return config
