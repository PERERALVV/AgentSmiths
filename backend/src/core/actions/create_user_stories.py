import json

import importlib
PromptFormat = importlib.import_module('utils.PromptFormat')
render_template_with_data = getattr(PromptFormat, 'render_template_with_data')
USERSTORIES = getattr(importlib.import_module('core.prompts.user_stories'), 'USERSTORIES')
USERTASKS = getattr(importlib.import_module('core.prompts.user_stories'), 'USERTASKS')
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
# Project = getattr(importlib.import_module('models.project'), 'Project')

# TODO : break this into two actions user stories and user tasks
class UserStories(Action):

    name: str = "UserStories"
    return_json: bool = True

    def __init__(self):
        super().__init__()
    
    async def run(self,project):
        data={"name":project.name,"BaSpec":project.BaSpecification}
        msg=render_template_with_data(USERSTORIES, data)
        rsp=await self.ask(msg)
        project.userStories=json.loads(rsp)
        data={"userStories":project.userStories}
        msg=render_template_with_data(USERTASKS, data)
        rsp=await self.ask(msg)
        project.userTasks=json.loads(rsp)
        return project
