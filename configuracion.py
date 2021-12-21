from dotenv import load_dotenv
import os
import logging

class Configuracion:
    def __init__(self):
        if os.path.isfile('.env'):
            load_dotenv()

        if os.getenv('DATASET'):
            self.dataset = os.getenv('DATASET')
        else:
            self.dataset = 'data/Restaurant_Reviews.tsv'
        
        if os.getenv('LOGGING_DIR'):
            self.logging_dir = os.getenv('LOGGING_DIR')
        else:
            self.logging_dir = None

        if os.getenv('LOGGING_FILE'):
            self.logging_file = os.getenv('LOGGING_FILE')
        else:
            self.logging_file = None

        if self.logging_dir != None and self.logging_file != None:
            self.logging_path = self.logging_dir + "/" + self.logging_file
        else:
            self.logging_path = None

        if os.getenv('LOGGING_FORMAT'):
            self.logging_format = os.getenv('LOGGING_FORMAT')
        else:
            self.logging_format = "%(levelname)s :  %(asctime)s - %(message)s"

        if os.getenv('LOGGING_LEVEL'):
            self.logging_level = os.getenv('LOGGING_LEVEL')
        else:
            self.logging_level = logging.WARNING

    def get_dataset(self):
        return self.dataset

    def get_logging_dir(self):
        return self.logging_dir
    
    def get_logging_file(self):
        return self.logging_file

    def get_logging_path(self):
        return self.logging_path
    
    def get_logging_format(self):
        return self.logging_format

    def get_logging_level(self):
        return self.logging_level
