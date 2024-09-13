import os
from database import vecDB
from core.validators import prompt_validator, qna_validator # we import these to intialize the validators so the chat will be faster
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set script_dir as an environment variable
def set_root_path():
    os.environ['ROOT_PATH'] = script_dir


def setupall():
    set_root_path()
    # vecDB.initDB()

