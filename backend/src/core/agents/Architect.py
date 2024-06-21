import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
plan_architecture=getattr(importlib.import_module('core.actions.plan_architecture'), 'plan_architecture')

class ARCH(Agent):

    name:str="sehara"
    job_role:str="Architect"

    def __init__(self):
        self.set_actions([plan_architecture])
    
    async def act(self,project):
        todo=self.actions[0]
        modified_proj=await todo.run(project)
        # print(modified_proj)
        return modified_proj