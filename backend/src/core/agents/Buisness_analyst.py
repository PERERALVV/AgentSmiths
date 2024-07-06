import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
LOG = getattr(importlib.import_module('core.logger'), 'log')

ask_questions=getattr(importlib.import_module('core.actions.ask_questions'), 'ask_questions')
review_spec=getattr(importlib.import_module('core.actions.review_spec'), 'review_spec')
modify_spec=getattr(importlib.import_module('core.actions.modify_spec'), 'ModifySpec')

FRONTENDONLY=getattr(importlib.import_module('const.ProjectConst'), 'FRONTEND_ONLY')

MAX_ROUNDS = 5

class Buisness_analyst(Agent):

    job_role:str="Buisness_analyst"

    def __init__(self):
        self.set_actions([ask_questions,review_spec,modify_spec])
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')
        iterations = 0
        while iterations < MAX_ROUNDS:
            LOG.info(f'{self.job_role} is asking questions')
            project = await self.actions[0].run(project)
            LOG.info(f'{self.job_role} is reviewing the spec')
            project = await self.actions[1].run(project)
            if project.Spec_review is None:
                break
            iterations += 1
        original_spec = project.BaSpecification
        if FRONTENDONLY:
            try:
                LOG.info(f'{self.job_role} is modifying the spec')
                project = await self.actions[2].run(project)
            except Exception as e:
                LOG.error(f'Error in modifying the spec {e}')
                project.BaSpecification = original_spec
                project.user_connection("exit",project.projectID)
                project.next_agent = "Requirements_analyst"
                return project
        
        project.user_connection("exit",project.projectID)
        project.next_agent = "Requirements_analyst"
        return project