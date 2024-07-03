import importlib
PromptFormat = importlib.import_module('utils.PromptFormat')
render_template_with_data = getattr(PromptFormat, 'render_template_with_data')
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
ONLYFRONTEND = getattr(importlib.import_module('core.prompts.modify_spec'), 'ONLYFORNTEND')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class ModifySpec(Action):
    
        name: str = "ModifySpec"
        description: str = "Modify the baspec of a project to only include the front end part of the project."
        return_json: bool = False
        
        def __init__(self):
            super().__init__()
    
        async def run(self,project):
            FRONTEND_FRAMEWORK="REACTJS"
            STYLING_METHOD="STYLED-COMPONENTS"
            data={"BaSpec":project.BaSpecification,"FRONTEND_FRAMEWORK":FRONTEND_FRAMEWORK,"STYLING_METHOD":STYLING_METHOD}
            msg=render_template_with_data(ONLYFRONTEND , data)
            # LOG.info(msg)
            rsp=await self.ask(msg)
            #TODO: maybe parsing needed
            project.BaSpecification=rsp
            LOG.info(project.BaSpecification)
            return project