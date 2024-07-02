from pydantic import BaseModel
from typing import Dict, Any
 
class requirements_chats(BaseModel):
    userID : str
    conversation: list

class static_requirements_chats(BaseModel):
    userID : str
    conversationID: str
    conversation: list
    description: list