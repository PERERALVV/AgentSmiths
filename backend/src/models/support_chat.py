from typing import List, Optional
import uuid
from pydantic import BaseModel, Field

class message(BaseModel):
    message: str
    sender: str
    timestamp: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "message": "Hello, how can I help you?",
                "sender": "Support Bot",
                "timestamp": "2023-10-26T12:00:00Z"
            }
        }

class SupportChat(BaseModel):
    user_id: str = Field(...)
    messages: List[message] = []

    class Config:
        schema_extra = {
            "example": {
                "user_id": "user123",
                "messages": [
                    {
                        "message": "Hello, I'm having trouble with my account.",
                        "sender": "User",
                        "timestamp": "2023-10-26T12:01:00Z"
                    },
                    {
                        "message": "I can help with that. Can you tell me more about the issue?",
                        "sender": "Support Bot",
                        "timestamp": "2023-10-26T12:02:00Z"
                    }
                ]
            }
        }

