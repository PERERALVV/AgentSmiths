import importlib
Agent=getattr(importlib.import_module('core.agents.Agent'), 'AGENT')
LOG = getattr(importlib.import_module('core.logger'), 'log')

filter_relevant_files=getattr(importlib.import_module('core.actions.filter_relevant_files'), 'filter_relevant_files')
implement_task_roughly=getattr(importlib.import_module('core.actions.implement_task_roughly'), 'implement_task_roughly')
parse_rough_task=getattr(importlib.import_module('core.actions.parse_rough_task'), 'parse_rough_task')
code_task=getattr(importlib.import_module('core.actions.code_task'), 'code_task')
simple_code_review=getattr(importlib.import_module('core.actions.simple_code_review'), 'simple_code_review')
apply_review=getattr(importlib.import_module('core.actions.apply_review'), 'apply_review')
rework_code_task=getattr(importlib.import_module('core.actions.rework_code_task'), 'rework_code_task')
update_codebase=getattr(importlib.import_module('core.actions.update_codebase'), 'update_codebase')
summarize_files=getattr(importlib.import_module('core.actions.summarize_files'), 'summarize_files')

class Developer(Agent):

    job_role:str="Developer"

    def __init__(self):
        self.set_actions(
            [
                filter_relevant_files,
                implement_task_roughly,
                parse_rough_task,
                code_task,
                simple_code_review,
                apply_review,
                rework_code_task,
                update_codebase,
                summarize_files
            ]
        )
    
    async def act(self,project):
        LOG.info(f'{self.job_role} is starting to work on the project {project.name}')

        project.current_task_index=0
        project.current_sub_task_index=0
        
        for j in range(len(project.dev_plan['plan'])):
            project.current_task_index=j
            LOG.info(f'{self.job_role} started working on task {j} \n{project.dev_plan["plan"][j]["description"]}')

            LOG.info(f'{self.job_role} is filtering relevant files')
            project = await self.actions[0].run(project)

            LOG.info(f'{self.job_role} is implementing the task roughly')
            project = await self.actions[1].run(project)

            LOG.info(f'{self.job_role} is creating sub tasks for the current task {j}')
            project = await self.actions[2].run(project)

            for i in range(len(project.sub_tasks_for_current_task)):
                project.current_sub_task_index=i
                iterations=0
                LOG.info(f"Task {j} Sub Task {i}")

                while True:

                    if project.update_codebase or project.current_sub_task_completed:
                        if project.update_codebase:
                            LOG.info(f'{self.job_role} is updating the codebase')
                            project = await self.actions[7].run(project)

                            LOG.info(f'{self.job_role} is summarizing the files')
                            project = await self.actions[8].run(project)

                        if iterations==4:
                            LOG.warning(f'{self.job_role} updated codebase after 4 review iterations due to exhaustion')
                        else:
                            LOG.info(f'{self.job_role} finished the sub task {i}') 
                        
                        project.current_sub_task_send_for_review=False
                        project.update_codebase=False
                        project.current_sub_task_completed=False
                        break

                    project = await self.actions[3].run(project)
                    project = await self.actions[4].run(project)
                    project = await self.actions[5].run(project)
                    project = await self.actions[6].run(project)

                    iterations+=1
                    if iterations==4:
                        project.update_codebase=True
        project.next_agent = "Dev_ops"
        return project
