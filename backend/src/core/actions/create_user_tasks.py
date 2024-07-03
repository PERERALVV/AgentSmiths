import json
import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

USERTASKS = getattr(importlib.import_module('core.prompts.user_stories'), 'USERTASKS')
USERTASKS_CALL = getattr(importlib.import_module('core.function_calls'), 'USER_TASKS')
LOG = getattr(importlib.import_module('core.logger'), 'log')

class UserTasks(Action):

    name: str = "UserTasks"
    return_json: bool = False
    function_calls = USERTASKS_CALL


    def __init__(self):
        super().__init__()
    
    async def run(self,project):
        data={"userStories":project.userStories}
        msg=render_template_with_data(USERTASKS, data)
        rsp=await self.ask(msg)
        project.userTasks=self.parse_json(rsp)
        LOG.info(project.userTasks)
        return project
