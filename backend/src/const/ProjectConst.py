STATIC_SITES=False # WILL ONLY PRODUCE STATIC SITES

USE_JSON=False # model will return json response if set to True

FILTER_RELEVANT_FILES=True # IF TRUE will only return files that are relevant to the project else will return all files

import os
def get_root(clientID,project_name):
    # Get the current script's directory
    current_script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Go two directories up
    parent_dir = os.path.dirname(os.path.dirname(current_script_dir))
    
    # Append 'workspace/clientID'
    return os.path.join(parent_dir, 'workspace', clientID, project_name)