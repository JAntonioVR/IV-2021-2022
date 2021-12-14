import logging
from configuration.configuracion import read_config_file

levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


config = read_config_file('configuration/config.ini')['LOGGING']
if 'output' in config:
    logging.basicConfig(filename=config['output'], level=levels[config['level']])
else:
    logging.basicConfig(level=levels[config['level']])

# Código de prueba
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')