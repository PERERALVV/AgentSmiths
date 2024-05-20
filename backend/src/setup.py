import os
from database import vecDB
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set script_dir as an environment variable
def set_root_path():
    os.environ['ROOT_PATH'] = script_dir

def initDB():
    vecDB.initDB()

def setupall():
    set_root_path()
    initDB()