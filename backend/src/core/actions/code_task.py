import importlib
import os
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'CODER')
IMPLEMENT_CHANGES = getattr(importlib.import_module('core.prompts.coder'), 'IMPLEMENT_CHANGES')

UPDATE_FILE=getattr(importlib.import_module('utils.file_handling'), 'update_file')

LOG = getattr(importlib.import_module('core.logger'), 'log')

valid_languages = [
      "javascript",
      "jsx",
      "typescript",
      "tsx",
      "html",
      "css",
      "scss",
      "json",
      "graphql" 
]

class code_task(Action):
    name:str = "code_task"
    return_json: bool = False
    goal: str = GOAL

    def __init__(self):
        super().__init__()

    
    async def run(self,project):
        if not project.current_sub_task_send_for_review:
            LOG.info('coding task')
            if ".gitignore" in project.sub_tasks_for_current_task[project.current_sub_task_index]['path']:
                LOG.info("skipping current sub task as it is for a gitignore file")
                project.current_sub_task_completed=True
                project.update_codebase=False
                return project
            file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
            data={
                "file_name":os.path.basename(file_path),
                "file_path":file_path,
                "file_content":"", # add function here to get the file content when file path is given 
                "instructions":project.rough_implementation['response'],
                "development_tasks": project.dev_plan['plan'],
                "current_task_index": project.current_task_index,
            }
            msg=render_template_with_data(IMPLEMENT_CHANGES, data)
            # LOG.info(msg)
            rsp=await self.askM(msg)
            rsp=self.parse_std_resp(rsp)
            if len(rsp.split('\n')[0].split()):
                first_word = rsp.split('\n')[0].split()[0].strip().lower()
                if first_word in valid_languages:
                    rsp='\n'.join(rsp.split('\n')[1:])
                    LOG.info(f"content formatted by removing preambles: {first_word}")
            # mostly this will be enough TODO: may need to ceck in line using re if multiple words
            # LOG.info(rsp)
            LOG.info(f"code path: {file_path}")
            LOG.info(rsp)
            path=os.path.join(project.root_path,file_path)

            project.current_sub_task_send_for_review = self.check_path_and_content(path)

            # if the new changes doesnt overwrite any existing files in the project we can implement it in the code base
            # no need to send for review
            project.curent_sub_task_code_pending_review={"code":rsp,"memory":self.getmemory()}
            if not project.current_sub_task_send_for_review:
                LOG.info('no existing file so setting to update codebase')
                project.update_codebase=True
                # if not UPDATE_FILE(path,rsp,project):
                #     LOG.info('ERROR!!!!!! File not updated')

        return project
    
    def check_path_and_content(self,path):
        # Check if the path exists
        if not os.path.exists(path):
            return False
        # Check if the file is not empty
        if os.path.getsize(path) > 0:
            return True
        else:
            return False
        
    