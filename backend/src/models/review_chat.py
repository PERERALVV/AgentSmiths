from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class ChatMessage(BaseModel):
    message: str
    direction: str  # You might want to use an Enum here for "incoming" and "outgoing" values
    sender: str
class ReviewChat(BaseModel):
    chat: List[ChatMessage] = []
    timestamp: Optional[str] = Field(default_factory=lambda: datetime.now().isoformat())