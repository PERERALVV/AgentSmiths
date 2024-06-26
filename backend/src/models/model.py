from pydantic import BaseModel
from typing import Dict, Any
 
class requirements_chats(BaseModel):
    userID : str
    conversation: list
    # conversation: str
    # conversation: List[str, Any]

# {
#   "userID": "userTest01",
#   "conversation": {["Hi what do you want me to make?","I want a website for my business"],["What type of business do you have?","I have a salon"],["What features do you want on your website?","I want to showcase services"]}
# }