from pydantic import BaseModel
from typing import List, Optional

class WEBSITE(BaseModel):
    name: Optional[str] = None
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    root_path: Optional[str] = None
    pages: Optional[List[dict]] = None
    dev_plan: Optional[List[dict]] = None
    file_names: Optional[List]=None