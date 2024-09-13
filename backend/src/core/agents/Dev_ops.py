import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
LOG = getattr(importlib.import_module('core.logger'), 'log')

execute_command=getattr(importlib.import_module('core.actions.execute_command'), 'execute_command')

class Dev_ops(Agent):

    job_role:str="Dev_ops"

    def __init__(self):
        self.set_actions([execute_command])
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')

        LOG.info(f'{self.job_role} is executing the command')
        project = await self.actions[0].run(project)

        project.next_agent = None
        return project