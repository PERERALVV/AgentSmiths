import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

DESCRIBE_FILE = getattr(importlib.import_module('core.prompts.describe_file'), 'DESCRIBE_FILE')
FILE_CONTENT = getattr(importlib.import_module('core.prompts.describe_file'), 'FILE_CONTENT')
SUMMARIZE_FILES=getattr(importlib.import_module('core.function_calls'), 'SUMMARIZE_FILES')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class summarize_files(Action):
    name:str = "summarize_files"
    return_json: bool = False
    goal: str = DESCRIBE_FILE
    function_calls = SUMMARIZE_FILES

    def __init__(self):
        super().__init__()

    
    async def run(self,project):
        file_path=project.sub_tasks_for_current_task[project.current_sub_task_index]['path']
        content=project.curent_sub_task_code_pending_review['code']
        msg=FILE_CONTENT.format(fpath=file_path,content=content)
        # LOG.info(msg)
        rsp=await self.ask(msg)
        rsp=self.parse_json(rsp)
        rsp['path'] = file_path
        # LOG.info(rsp)
        project.existing_file_summaries.append(rsp)
        return project