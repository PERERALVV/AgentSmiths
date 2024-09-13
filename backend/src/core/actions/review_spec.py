import importlib
import os
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

REVIEW_SPEC= getattr(importlib.import_module('core.prompts.buisness_analyst'), 'REVIEW_SPEC')
REVIEW_SPEC_CALL = getattr(importlib.import_module('core.function_calls'), 'REVIEW_SPEC')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class review_spec(Action):

    name:str = "review_spec"
    return_json: bool = False
    goal: str = REVIEW_SPEC
    function_calls = REVIEW_SPEC_CALL

    def __init__(self):
        # self.initial_convo=initial_convo
        super().__init__()

    async def run(self,project):
        data={
            "convo":project.user_convo,
            "spec":project.BaSpecification
        }
        msg=render_template_with_data(REVIEW_SPEC, data)
        # LOG.info(msg)
        rsp=await self.ask(msg)
        try:
            if rsp is not None:
                rsp=self.parse_json(rsp)
                LOG.info(rsp)
                if rsp['type']=="MISSING-INFORMATION":
                    project.Spec_review=rsp['content']
                else:
                    project.Spec_review=None
        except Exception as e:
            LOG.error(f"Error in review_spec: {e}")
            project.Spec_review=None
        return project
