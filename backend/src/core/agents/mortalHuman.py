# from metagpt.actions import Action,UserRequirement
# from metagpt.roles import Role
# from metagpt.schema import Message


# class sendq(Action):
#     name: str = "send the question to the front end and get the answer from the client"
    
#     async def run(self,initial_json_object: str):
#         return initial_json_object
    
# class getans(Action):
#     name: str = "get the answer from the client"
    
#     async def run(self,initial_json_object: str):
#         return initial_json_object
    
# class punyHuman(Role):
#     name: str = "sir james the 3rd"
#     profile: str = "useless Human"
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.set_actions([sendq])
#         self._watch([UserRequirement])
#     async def _act(self) -> Message:
