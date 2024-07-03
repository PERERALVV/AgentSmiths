import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
UserStories=getattr(importlib.import_module('core.actions.create_user_stories'), 'UserStories')

class RA(Agent):
    name:str="dinu"
    job_role:str="Requiremnt Analyst"

    def __init__(self):
        self.set_actions([UserStories])
    
    async def act(self,project):
        todo=self.actions[0]
        modified_proj=await todo.run(project)
        # print(modified_proj)
        return modified_proj