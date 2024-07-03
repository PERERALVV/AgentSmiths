# ==============================================================================================
# duplicate file for temporary use delete after use not needed for production 
# only usefull when buuilding new templates
# ==============================================================================================

import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
import json
import os
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

DESCRIBE_FILE = getattr(importlib.import_module('core.prompts.describe_file'), 'DESCRIBE_FILE')
FILE_CONTENT = getattr(importlib.import_module('core.prompts.describe_file'), 'FILE_CONTENT')
SUMMARIZE_FILES=getattr(importlib.import_module('core.function_calls'), 'SUMMARIZE_FILES')
GET_MULTILEVEL_DIRECTORY_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_multilevel_directory_contents')

class summarize_files(Action):
    name:str = "summarize_files"
    return_json: bool = False
    goal: str = DESCRIBE_FILE
    function_calls = SUMMARIZE_FILES

    def __init__(self):
        super().__init__()

    
    async def run(self,root_path):
        files=GET_MULTILEVEL_DIRECTORY_CONTENTS(root_path)
        fs=[]
        for file in files:
            file_path = os.path.relpath(file['full_path'], root_path)
            content=file['content']
            msg=FILE_CONTENT.format(fpath=file_path,content=content)
            # print(msg)
            rsp=await self.ask(msg)
            rsp=self.parse_json(rsp)
            rsp['path'] = file_path
            fs.append(rsp)
        return fs