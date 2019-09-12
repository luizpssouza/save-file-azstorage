# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

def setEnvironmentVariables():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

class Env(object):
    def __init__(self, *args, **kwargs):
        self.AZURE_STORAGE_CONNECTIONSTRING=os.environ.get("AZURE_STORAGE_CONNECTIONSTRING")
        self.AZURE_STORAGE_CONTAINER=os.environ.get("AZURE_STORAGE_CONTAINER")
        self.AZURE_STORAGE_SUBFOLDER=os.environ.get("AZURE_STORAGE_SUBFOLDER")
