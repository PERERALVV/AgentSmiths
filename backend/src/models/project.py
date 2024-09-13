from pydantic import BaseModel
from typing import List, Optional, Any
import importlib

json=getattr(importlib.import_module('const.ProjectConst'), 'USE_JSON')

# TODO:still to be defined proper data types for most of the fields
class Project(BaseModel):
    root_path: Optional[str] = None
    execution_path: Optional[str] = None
    clientID: Optional[str] = None
    projectID: Optional[str] = None
    host_url: Optional[str] = None 
    name: Optional[str] = None
    next_agent: Optional[str] = None
    user_connection: Optional[Any] = None
    user_convo: Optional[Any] = []
    BaSpecification: Optional[str] = None
    Spec_review: Optional[Any] = None
    userStories: Optional[List[str]] = None
    userTasks: Optional[List[Any]] = None
    architecture: Optional[Any] = None
    architecture_desc: Optional[str] = None
    system_dependencies: Optional[List[dict]] = None
    package_dependencies: Optional[List[dict]] = None
    template_name: Optional[Any] = None 
    dev_plan: Optional[Any] = None
    template_obj: Optional[Any] = None
    template_project_files: Optional[Any] = None
    existing_file_summaries: Optional[Any] = None
    current_task_index: Optional[int] = None
    existing_files: Optional[Any] = None # if filtering is turned on this will only contain relevant files for a task
    rough_implementation: Optional[Any] = None #this will have a memory if you hope to store in a database remove the prompt and only leave the resp before storing
    sub_tasks_for_current_task: Optional[Any] = None
    current_sub_task_index: Optional[int] = None
    commands: Optional[Any] = []
    current_sub_task_send_for_review: Optional[bool] = False #this will decide wheter review for the implementation of the subtask is required or not if creating new files no review needed
    curent_sub_task_code_pending_review: Optional[Any] = None
    current_sub_task_review: Optional[Any] = None
    update_codebase: Optional[bool] = False
    current_sub_task_completed: Optional[bool] = False


    