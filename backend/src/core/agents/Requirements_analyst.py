import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
LOG = getattr(importlib.import_module('core.logger'), 'log')

create_user_tasks=getattr(importlib.import_module('core.actions.create_user_tasks'), 'UserTasks')
create_user_stories=getattr(importlib.import_module('core.actions.create_user_stories'), 'UserStories')

class Requirements_analyst(Agent):

    job_role:str="Requirements_analyst"

    def __init__(self):
        self.set_actions([create_user_stories,create_user_tasks])
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')

        LOG.info(f'{self.job_role} is creating user stories')
        project = await self.actions[0].run(project)
        
        LOG.info(f'{self.job_role} is creating user tasks')
        project = await self.actions[1].run(project)
        
        project.next_agent = "Architect"
        return project