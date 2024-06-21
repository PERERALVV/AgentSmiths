from pydantic import BaseModel
from typing import List, Optional, Any
import importlib

json=getattr(importlib.import_module('const.ProjectConst'), 'USE_JSON')

# TODO:still to be defined proper data types for most of the fields
class Project(BaseModel):
    root_path: Optional[str] = None
    clientID: Optional[str] = None 
    name: Optional[str] = None
    if json:
        BaSpecification: Optional[dict] = None
    else:
        BaSpecification: Optional[str] = None
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