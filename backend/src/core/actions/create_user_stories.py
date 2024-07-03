import importlib

Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

USERSTORIES = getattr(importlib.import_module('core.prompts.user_stories'), 'USERSTORIES')
USERSTORIES_CALL = getattr(importlib.import_module('core.function_calls'), 'USER_STORIES')

LOG = getattr(importlib.import_module('core.logger'), 'log')

# Project = getattr(importlib.import_module('models.project'), 'Project')

# TODO : break this into two actions user stories and user tasks
class UserStories(Action):

    name: str = "UserStories"
    return_json: bool = False
    function_calls = USERSTORIES_CALL

    def __init__(self):
        super().__init__()
    
    async def run(self,project):
        data={"name":project.name,"BaSpec":project.BaSpecification}
        msg=render_template_with_data(USERSTORIES, data)
        rsp=await self.ask(msg)
        project.userStories=self.parse_json(rsp)
        LOG.info(project.userStories)
        return project
