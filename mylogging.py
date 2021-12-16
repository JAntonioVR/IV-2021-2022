import logging

levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

'''
# FIXME ya no existe read_config_file
def init_logging():
    config = read_config_file('configuration/config.ini')['LOGGING']
    if 'output' in config:
        logging.basicConfig(filename=config['output'], level=levels[config['level']])
    else:
        logging.basicConfig(level=levels[config['level']])
'''