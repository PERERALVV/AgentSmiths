import os
import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')

render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

FILTER_FILES = getattr(importlib.import_module('core.prompts.developer'), 'FILTER_FILES')
GOAL= getattr(importlib.import_module('core.prompts.agent_epics'), 'DEVELOPER')

GET_MULTILEVEL_DIRECTORY_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_multilevel_directory_contents')
BUILD_DIRECTORY_TREE=getattr(importlib.import_module('utils.file_handling'), 'build_directory_tree')

FILTER_RELEVANT_FILES=getattr(importlib.import_module('const.ProjectConst'), 'FILTER_RELEVANT_FILES')#this is a true or false flag

LIST_RELEVANT_FILES=getattr(importlib.import_module('core.function_calls'), 'LIST_RELEVANT_FILES')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class filter_relevant_files(Action):
    name:str = "filter_relevant_files"
    description:str = "this action filters the files and returs only the relevant files"
    return_json: bool = False
    goal: str = GOAL
    function_calls = LIST_RELEVANT_FILES

    def __init__(self):
        super().__init__()

    async def run(self,project):
        files=GET_MULTILEVEL_DIRECTORY_CONTENTS(project.root_path)
        # FILTER_RELEVANT_FILES=False
        if not FILTER_RELEVANT_FILES:
            project.existing_files = files
            return project
        
        if project.existing_file_summaries is None:
            project.existing_file_summaries=project.template_obj.get("files")
        
        file_summaries=project.existing_file_summaries
        data={
            "name": project.name,
            "app_type": "WEBSITE",
            "app_summary": project.BaSpecification,
            "architecture": project.architecture_desc,
            "technologies": project.system_dependencies + project.package_dependencies,
            "directory_tree": BUILD_DIRECTORY_TREE(project.root_path),
            "current_task": project.dev_plan['plan'][project.current_task_index],
            "development_tasks": project.dev_plan['plan'],
            # "previous_features": self.project.previous_features,
            # "current_feature": self.project.current_feature,
            "file_summaries": file_summaries,
        }
        msg=render_template_with_data(FILTER_FILES, data)
        # LOG.info(msg)
        rsp=await self.ask(msg)
        # LOG.info(rsp)        
        relevant_files=self.parse_json(rsp)
        LOG.info(f"found the relevant files: {relevant_files}")
        # files = [file for file in files if os.path.join('.',os.path.relpath(file['full_path'],project.root_path)) in relevant_files]
        files = [file for file in files if os.path.join(file['path'],file['name']) in relevant_files]
        project.existing_files = files
        LOG.info(f"filtered files\n: {files}")
        return project
        


        
        