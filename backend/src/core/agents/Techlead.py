import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
LOG = getattr(importlib.import_module('core.logger'), 'log')

plan_development=getattr(importlib.import_module('core.actions.plan_development'), 'plan_development')

class Techlead(Agent):

    job_role:str="Techlead"

    def __init__(self):
        self.set_actions([plan_development])
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')

        LOG.info(f'{self.job_role} is planning the development')
        project = await self.actions[0].run(project)
        project.dev_plan["plan"] = [{**item, "status": "todo"} for item in project.dev_plan["plan"]]

        project.next_agent = "Developer"
        return project