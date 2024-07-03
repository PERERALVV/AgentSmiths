import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')

plan_architecture=getattr(importlib.import_module('core.actions.plan_architecture'), 'plan_architecture')
apply_template=getattr(importlib.import_module('core.actions.apply_template'), 'apply_template')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class Architect(Agent):

    job_role:str="Architect"

    def __init__(self):
        self.set_actions([plan_architecture,apply_template])
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')

        LOG.info(f'{self.job_role} is planning the architecture')
        project = await self.actions[0].run(project)

        LOG.info(f'{self.job_role} is applying the template')
        project = await self.actions[1].run(project)
        
        project.next_agent = "Techlead"
        return project