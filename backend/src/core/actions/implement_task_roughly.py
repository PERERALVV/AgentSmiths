import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

IMPLEMENT_TASK = getattr(importlib.import_module('core.prompts.developer'), 'IMPLEMENT_TASK')
GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'DEVELOPER')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class implement_task_roughly(Action):
    name:str = "implement_task"
    return_json: bool = False
    goal: str = GOAL

    def __init__(self):
        super().__init__()

    
    async def run(self,project):
        
        if project.existing_file_summaries is None:
            project.existing_file_summaries=project.template_obj.get("files")
        
        file_summaries=project.existing_file_summaries
        files=project.existing_files
        data={
            "name": project.name,
            "app_type": "WEBSITE",
            "app_summary": project.BaSpecification,
            "user_stories": project.userStories,
            "user_tasks": project.userTasks,
            # "directory_tree": ,
            "current_task_index": project.current_task_index,
            "development_tasks": project.dev_plan['plan'],
            "file_summaries": file_summaries,
            "files": files,
            "architecture": project.architecture_desc,
            "technologies": project.system_dependencies + project.package_dependencies,
            # "task_type": 'feature' if self.project.finished else 'app',
            "task_type": 'app',
            # "previous_features": self.project.previous_features,
            # "current_feature": self.project.current_feature,
        }
        msg=render_template_with_data(IMPLEMENT_TASK, data)
        # LOG.info(msg)
        rsp=await self.askM(msg)
        # LOG.info(rsp)
        project.rough_implementation={'response':rsp , 'memory':self.getmemory()}
        return project