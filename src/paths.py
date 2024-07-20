import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

def get_data_file(filename):
    return os.path.join(BASE_PATH, 'data', filename)