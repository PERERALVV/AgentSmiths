import importlib
import os
import re
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

UPDATE_FILE=getattr(importlib.import_module('utils.file_handling'), 'update_file')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class update_codebase(Action):

    name:str = "update_codebase"
    return_json: bool = False


    
    async def run(self,project):
        if project.update_codebase:
            # LOG.info('updating codebase')
                file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
                path=os.path.join(project.root_path,file_path)
                if not UPDATE_FILE(path,project.curent_sub_task_code_pending_review['code'],project):
                    LOG.info('ERROR!!!!!! File not updated')
        return project