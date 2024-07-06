import platform
import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'DEVELOPER')
PARSE_TASK = getattr(importlib.import_module('core.prompts.developer'), 'PARSE_TASK')
PARSE_TASK_CALL=getattr(importlib.import_module('core.function_calls'), 'PARSE_TASK')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class parse_rough_task(Action):
    name:str = "parse_rough_task"
    return_json: bool = False
    goal: str = GOAL
    function_calls = PARSE_TASK_CALL
    def __init__(self):
        super().__init__()

    
    async def run(self,project):
        self.setmemory(project.rough_implementation['memory'])
        instructions=project.rough_implementation['response']
        instructions_prefix = " ".join(instructions.split()[:5])
        instructions_postfix = " ".join(instructions.split()[-5:])
        data={
                'os': platform.system(),
                'instructions_prefix': instructions_prefix,
                'instructions_postfix': instructions_postfix,
            }
        msg=render_template_with_data(PARSE_TASK, data)
        # LOG.info(msg)
        resp = await self.askM(msg)
        resp=self.parse_json(resp)
        LOG.info(resp)
        project.sub_tasks_for_current_task=[task['save_file'] for task in resp['tasks'] if task['type'] == 'save_file']
        LOG.info(project.sub_tasks_for_current_task)
        project.commands.append([task['command'] for task in resp['tasks'] if task['type'] == 'command'])
        LOG.info(project.commands)
        return project