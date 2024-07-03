import importlib
import os
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')
GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'CODE_REVIEWER')
REVIEW_CHANGES= getattr(importlib.import_module('core.prompts.reviewer'), 'REVIEW_CHANGES')

REVIEW_CHANGES_CALL=getattr(importlib.import_module('core.function_calls'), 'REVIEW_CHANGES')

GET_HUNKS = getattr(importlib.import_module('utils.track_changes'), 'get_diff_hunks')
GET_FILE_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_file_contents')
UPDATE_FILE=getattr(importlib.import_module('utils.file_handling'), 'update_file')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class simple_code_review(Action):

    name:str = "simple_code_review"
    return_json: bool = False
    goal: str = GOAL
    function_calls = REVIEW_CHANGES_CALL

    max_tries:int=2 # maxium number of times to re ask for review when all hunks are not reviewed

    def __init__(self):
        super().__init__()

    
    async def run(self,project):
        if project.current_sub_task_send_for_review:
            LOG.info('reviewing code')
            file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
            file_name=os.path.basename(file_path)
            old_content=GET_FILE_CONTENTS(os.path.join(project.root_path,file_path),project.root_path)['content']
            hunks=GET_HUNKS(file_name,old_content,project.curent_sub_task_code_pending_review['code'])
            data={
                "file_name":file_name,
                "file_path":file_path,
                "development_tasks": project.dev_plan['plan'],
                "current_task_index": project.current_task_index,
                "old_content":old_content,
                "hunks":hunks
            }
            # LOG.info(GET_HUNKS(file_name,old_content,project.curent_sub_task_code_pending_review))
            msg=render_template_with_data(REVIEW_CHANGES, data)
            # LOG.info(msg)
            rsp=await self.askM(msg)
            rsp=self.parse_json(rsp)
            LOG.info(rsp)
            for i in range(self.max_tries):
                if len(rsp['hunks'])==len(hunks):
                    project.current_sub_task_review=rsp
                    # project.current_sub_task_send_for_review=False
                    break
                elif len(rsp['hunks'])<len(hunks):
                    msg=f"""You have only reviewed {len(rsp['hunks'])} out of the total {len(hunks)} number of hunks provided.
                    Please review all hunks and add 'apply', 'ignore' or 'rework' decision for each."""
                    rsp=await self.askM(msg)
                    rsp=self.parse_json(rsp)
                    LOG.WARNING('partial result, reasking for review')
                elif len(rsp['hunks'])>len(hunks):
                    msg=f"""Your review contains more hunks ({len(rsp['hunks'])}) than in the original diff ({len(hunks)}). 
                    Note that one hunk may have multiple changed lines."""
                    rsp=await self.askM(msg)
                    rsp=self.parse_json(rsp)
                    LOG.WARNING('partial result, reasking for review')
                else:
                    raise Exception('Error in review')
        return project




# ====================this part should be in the think part of the agent=======================
            # if len(rsp['hunks'])==1:
            #     if rsp['hunks'][0]['decision']=='Apply':
            #         project.current_sub_task_send_for_review=False
            #         path=os.path.join(project.root_path,file_path)
            #         if not UPDATE_FILE(path,project.curent_sub_task_code_pending_review,project):
            #             LOG.info('ERROR!!!!!! File not updated')
            #     elif rsp['hunks'][0]['decision']=='Ignore' or rsp['hunks']['decision']=='Rework':
            #         # project.current_sub_task_index=-1
            #         raise Exception('Rework needed')
            # elif len(rsp['hunks'])==0:
            #         project.current_sub_task_send_for_review=False
            #         path=os.path.join(project.root_path,file_path)
            #         if not UPDATE_FILE(path,project.curent_sub_task_code_pending_review,project):
            #             LOG.info('ERROR!!!!!! File not updated')
            # else:
            #     # project.current_sub_task_index=-1
            #     raise Exception('many hunks received')

            # if not any(hunk['decision'] != 'Apply' for hunk in rsp['hunks']):
            #     path=os.path.join(project.root_path,file_path)
            #     if not UPDATE_FILE(path,project.curent_sub_task_code_pending_review,project):
            #         LOG.info('ERROR!!!!!! File not updated')
            # else:
            #     raise Exception('Rework needed')
# ==============================================================================================
# agent think about what action to take next and choose it by setting the project variable next_action
# ==============================================================================================
