import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
APPLY_TEMPLATE= getattr(importlib.import_module('core.templates'), 'apply_project_template')
LOG= getattr(importlib.import_module('core.logger'), 'log')

class apply_template(Action):

    name:str = "apply_template"
    description: str = "Apply the template to the project this does not access the llm"

    async def run(self,project):
        result=APPLY_TEMPLATE(project)
        if result is not None:
            project=result
            LOG.info(f"Template{project.template_name} applied to project {project.name}")
        return project