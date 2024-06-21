import importlib
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')
GETARCHITECTURE = getattr(importlib.import_module('core.prompts.arch'), 'GETARCHITECTURE')
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
ARCHITECTURE = getattr(importlib.import_module('core.function_calls'), 'ARCHITECTURE')
GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'ARCHITECT')


class plan_architecture(Action):
    name:str = "plan_architecture"
    return_json: bool = False
    goal: str = GOAL
    function_calls = ARCHITECTURE


    def __init__(self):
        super().__init__()

    async def run(self,project):
        data={"project_name":project.name,"project_summary":project.BaSpecification,"user_stories":project.userStories,"user_tasks":project.userTasks,"os":"linux"}
        msg=render_template_with_data(GETARCHITECTURE, data)
        # print(msg)
        rsp=await self.ask(msg)
        project.architecture=self.parse_json(rsp)
        project.architecture_desc=project.architecture['architecture']
        project.system_dependencies=project.architecture['system_dependencies']
        project.package_dependencies=project.architecture['package_dependencies']
        project.template_name=project.architecture['template']
        return project