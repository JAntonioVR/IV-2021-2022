from dotenv import load_dotenv
import os
import logging

class Configuracion:
    def __init__(self):
        load_dotenv()
        if os.getenv('DATASET'):
            self.dataset = os.getenv('DATASET')
        else:
            self.dataset = 'data/Restaurant_Reviews.tsv'
        
        if os.getenv('LOGGING_FILE'):
            self.logging_file = os.getenv('LOGGING_FILE')

        if os.getenv('LOGGING_LEVEL'):
            self.logging_level = os.getenv('LOGGING_LEVEL')
        else:
            self.logging_level = logging.WARNING

    def get_dataset(self):
        return self.dataset
    
    def get_logging_file(self):
        return self.logging_file

    def get_logging_level(self):
        return self.logging_level

