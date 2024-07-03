from typing import List

class AGENT :
    """
        child classes should set actions in the constructor
    """
    name:str
    job_role:str
    actions:List[object]

    def set_actions(self, actions: List[type]):
        self.actions = [action() for action in actions]
        return self
    
    async def act(self):
        # should be implemented by the child class
        raise NotImplementedError