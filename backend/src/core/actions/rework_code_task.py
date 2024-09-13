import importlib
import os

Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'CODER')
CODE_REWORK = getattr(importlib.import_module('core.prompts.coder'), 'CODE_REWORK')

GET_FILE_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_file_contents')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class rework_code_task(Action):
    name:str = "rework_code_task"
    return_json: bool = False
    goal: str = GOAL
    def __init__(self):
        super().__init__()

    async def run(self,project):
        if project.current_sub_task_send_for_review:
            if any(hunk['decision'] == 'Rework' for hunk in project.current_sub_task_review['hunks']):# this is just only for added safety 
                LOG.info('reworking code')
                self.setmemory(project.curent_sub_task_code_pending_review['memory'])
                if len(project.current_sub_task_review['hunks']) == 0 and project.current_sub_task_review['review_notes'] is not None: # empty hunks and review notes
                    LOG.info('reworking empty hunks with review notes')
                        # self.setmemory(project.curent_sub_task_code_pending_review['memory'])
                    file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
                    old_content=GET_FILE_CONTENTS(os.path.join(project.root_path,file_path),project.root_path)['content']
                    data={
                        "content":old_content,
                        "original_content":old_content,
                        "reason_for_rework":project.current_sub_task_review['review_notes'],
                        "review_notes":project.current_sub_task_review['review_notes']
                    }
                    msg=render_template_with_data(CODE_REWORK,data)
                    rsp=await self.askM(msg)
                    rsp=self.parse_std_resp(rsp)
                    LOG.info(rsp)
                    project.curent_sub_task_code_pending_review={"code":rsp,"memory":self.getmemory()}
                    project.current_sub_task_send_for_review=True
                elif len([hunk for hunk in project.current_sub_task_review['hunks'] if hunk['decision'] == 'Rework']) == 1: # only one hunk for rework
                    LOG.info('single hunk for reworking')
                        # self.setmemory(project.curent_sub_task_code_pending_review['memory'])
                    # if only one hunk no need to apply the diff since the only diff needs rework
                    # hence the content and the original content will be the same
                    file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
                    old_content=GET_FILE_CONTENTS(os.path.join(project.root_path,file_path),project.root_path)['content']
                    data={
                        "content":old_content,
                        "original_content":old_content,
                        "reason_for_rework":project.current_sub_task_review['hunks'][0]['reason'],
                        "review_notes":project.current_sub_task_review['review_notes']
                    }
                    msg=render_template_with_data(CODE_REWORK,data)
                    rsp=await self.askM(msg)
                    rsp=self.parse_std_resp(rsp)
                    LOG.info(rsp)
                    project.curent_sub_task_code_pending_review={"code":rsp,"memory":self.getmemory()}
                    project.current_sub_task_send_for_review=True
                else:
                    LOG.info('multiple hunks for reworking')
                        # self.setmemory(project.curent_sub_task_code_pending_review['memory'])
                    # since multiple hunks we have applied the accepted hunks and is stored in current_sub_task_code_pending_review
                    # essentially it has overwritten the new content with the partially accepted version
                    file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
                    old_content=GET_FILE_CONTENTS(os.path.join(project.root_path,file_path),project.root_path)['content']
                    data={
                        "content":project.curent_sub_task_code_pending_review['code'],
                        "original_content":old_content,
                        "reason_for_rework":project.current_sub_task_review['hunks'][0]['reason'],
                        "review_notes":project.current_sub_task_review['review_notes']
                    }
                    msg=render_template_with_data(CODE_REWORK,data)
                    rsp=await self.askM(msg)
                    rsp=self.parse_std_resp(rsp)
                    LOG.info(rsp)
                    project.curent_sub_task_code_pending_review={"code":rsp,"memory":self.getmemory()}
                    project.current_sub_task_send_for_review=True
                    
        return project
    
