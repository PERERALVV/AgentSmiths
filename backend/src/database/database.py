from urllib.parse import quote_plus

username = quote_plus('vibuda')
password = quote_plus('Vp48BPutmziOa30E')
cluster = 'cluster0.ng1p2r4.mongodb.net'
# authSource = '<authSource>'
# authMechanism = '<authMechanism>'
uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority&appName=Cluster0'

# # Create a new client and connect to the server
# db = client["AGENTSMTHS"]
# chats_collection = db["support_chats"]
# messages_collection = db["messages"]  

import motor.motor_asyncio
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId


class Message(BaseModel):
    message: str
    sender: str
    # timestamp: Optional[str] = Field(default_factory=lambda: datetime.now().isoformat())

class SupportChat(BaseModel):
    user_id: str
    messages: List[Message] = []
    connect_to_human: bool = False

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client["AGENTSMTHS"] # Replace with your database name
collection = db["support_chats"] # Replace with your collection name

# Store a new chat
async def store_chat(userID,chat: List,connect_to_human: bool=False):
    messages = []
    for message in chat:
        (key,val),=message.items()
        messages.append(Message(sender=key, message=val))
    supportChat=SupportChat(user_id=userID, messages=messages, connect_to_human=connect_to_human)
    await collection.insert_one(supportChat.model_dump())

# Retrieve a chat by user_id
async def retrieve_chat_by_user_id(user_id: str):
    chat = await collection.find_one({"user_id": user_id})
    return SupportChat(**chat) if chat else None

# Retrieve multiple chats based on a specific attribute value
async def retrieve_chats_by_attribute(attribute: str, value: str):
    chats = []
    async for chat in collection.find({attribute: value}):
        chats.append(SupportChat(**chat))
    return chats

# Get all messages in the entire chats collection
async def get_all_messages():
    messages = []
    async for chat in collection.find():
        messages.extend(chat["messages"])
    return messages

