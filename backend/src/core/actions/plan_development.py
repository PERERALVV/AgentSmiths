import importlib
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')
PLANDEV = getattr(importlib.import_module('core.prompts.techlead'), 'PLANDEV')
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
DEVELOPMENT_PLAN= getattr(importlib.import_module('core.function_calls'), 'DEVELOPMENT_PLAN')
GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'TECHLEAD')
GET_MULTILEVEL_DIRECTORY_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_multilevel_directory_contents')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class plan_development(Action):
    name:str = "plan_development"
    return_json: bool = False
    goal: str = GOAL
    function_calls = DEVELOPMENT_PLAN

    def __init__(self):
        super().__init__()

    async def run(self,project):
        if project.template_obj is not None:
            template_summary="The code so far includes:\n"+project.template_obj.get("summary")
            files=GET_MULTILEVEL_DIRECTORY_CONTENTS(project.root_path)
        else:
            template_summary=None
            files=None

        
        data={
        "name": project.name,
        "app_type": "WEBSITE",
        "app_summary": project.BaSpecification,
        "user_stories": project.userStories,
        "user_tasks": project.userTasks,
        "architecture": project.architecture_desc,
        "technologies": project.system_dependencies + project.package_dependencies,
        "existing_summary": template_summary,
        "files": files,
        "task_type": 'app',
        }
        msg=render_template_with_data(PLANDEV, data)
        # LOG.info(msg)
        rsp=await self.ask(msg)
        LOG.info(rsp)
        project.dev_plan=self.parse_json(rsp)
        return project
    
# if __name__=="__main__":
#     data={
#     "name": "{{ name }}",
#     "app_type": "WEBSITE",
#     "app_summary": "{{ BaSpecification }}",
#     "user_stories": "{{ userStories }}",
#     "user_tasks": "{{ userTasks }}",
#     "architecture": "{{ project_architecture }}",
#     "technologies": "{{ technologies }}",
#     "existing_summary": "{{ existing_summary }}",
#     "files": "{{ files }}",
#     "task_type": 'app',
#     }
#     msg=render_template_with_data(PLANDEV, data)
#     LOG.info(msg)