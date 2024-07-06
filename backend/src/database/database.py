from urllib.parse import quote_plus

username = quote_plus('vibuda')
# password = quote_plus('Vp48BPutmziOa30E')
password = quote_plus('rdMy8vqkpzeIHHlO')
# cluster = 'cluster0.ng1p2r4.mongodb.net'
cluster = 'cluster0.mhaksto.mongodb.net'
# authSource = '<authSource>'
# authMechanism = '<authMechanism>'
uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'

# # Create a new client and connect to the server
# db = client["AGENTSMTHS"]
# chats_collection = db["support_chats"]
# messages_collection = db["messages"]  

import motor.motor_asyncio
# ===========================================================
# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client["AGENTSMTHS"] # Replace with your database name
support_chat_collection = db["support_chats"] # Replace with your collection name
faq_collection = db["FAQs"] # Replace with your collection name
review_chat_collection = db["review_chats"] # Replace with your collection name

# =======ayesha's code=======================
user_collection = db["User"]
forgot_password_collection = db["user_otp"]
projects_collection = db["projects"]
group_collections = db["group_collections"]
feedback_collection = db["feedback"]
# ===========================================================

# ===================================models for support_chats===================================
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
    status: str = "Unread"

class ChatMessage(BaseModel):
    message: str
    direction: str  # You might want to use an Enum here for "incoming" and "outgoing" values
    sender: str

class ReviewChat(BaseModel):
    chat: List[ChatMessage] = []
    # rating: int
    # feedback: str
    timestamp: Optional[str] = Field(default_factory=lambda: datetime.now().isoformat())
# =================================================================================================

# ===================== suporrt chat crud operations ===============================================
# Store a new chat
async def store_chat(userID,chat: List,connect_to_human: bool=False):
    messages = []
    for message in chat:
        (key,val),=message.items()
        messages.append(Message(sender=key, message=val))
    supportChat=SupportChat(user_id=userID, messages=messages, connect_to_human=connect_to_human)
    await support_chat_collection.insert_one(supportChat.model_dump())

# Retrieve a chat by user_id
async def retrieve_chat_by_user_id(user_id: str):
    chat = await support_chat_collection.find_one({"user_id": user_id})
    return SupportChat(**chat) if chat else None

# Retrieve multiple chats based on a specific attribute value
async def retrieve_chats_by_attribute(attribute: str, value: str):
    chats = []
    async for chat in support_chat_collection.find({attribute: value}):
        chats.append(SupportChat(**chat))
    return chats

# Get all messages in the entire chats collection
async def get_all_messages():
    messages = []
    async for chat in support_chat_collection.find():
        messages.extend(chat["messages"])
    return messages

async def store_review_chat(chat:ReviewChat):
    
    reviewChat=chat.model_dump()
    reviewChat['chat'] = [
        {**message, "sender": "bot user"} if message['sender'] == "SupportBot" 
        else {**message, "sender": "support agent"} if message['sender'] == "user" 
        else message 
        for message in reviewChat['chat']
    ]
    # print(reviewChat)
    await review_chat_collection.insert_one(reviewChat)
# =====================================================================================================

# ===================================models for faqs===================================
from pydantic import BaseModel, Field

class FAQ(BaseModel):
    question: str
    answer: str

# class FAQList(BaseModel):
#     faqs: List[FAQ] = []

# =================================================================================================

# ===================== faq crud operations =================================================

# Store a new FAQ
async def store_faq(faq: FAQ):
    await faq_collection.insert_one(faq.model_dump())

# Retrieve all FAQs
async def retrieve_faqs():
    faqs = []
    async for faq in faq_collection.find():
        faqs.append(FAQ(**faq))
    # return FAQList(faqs=faqs)
    return faqs


# =====================================================================================================

#===================gayuni=======================================
from models.model import requirements_chats ,static_requirements_chats

requirements_collection = db["requirements_chats"]
static_requirements_chats = db["static_requirements_chats"]

async def create_chatHistory(chatHistory):
    document = chatHistory
    result = await requirements_collection.insert_one(document)
    return document

async def fetch_one_chatHistory(userID):
    document = await requirements_collection.find_one({"userID":userID})
    return document

async def fetch_all_chatHistory():
    all_chatHistory=[]
    cursor = requirements_collection.find({})
    async for document in cursor:
        all_chatHistory.append(requirements_chats(**document))
    return all_chatHistory

async def remove_chatHistory(userID):
    await requirements_collection.delete_one({"userID":userID})
    return True

async def create_staticChatHistory(staticChatHistory):
    document = staticChatHistory
    result = await static_requirements_chats.insert_one(document)
    return document

async def fetch_one_staticChatHistory(userID):
    document = await static_requirements_chats.find_one({"userID":userID})
    return document

async def fetch_all_staticChatHistory():
    all_staticChatHistory=[]
    cursor = static_requirements_chats.find({})
    async for document in cursor:
        all_staticChatHistory.append(static_requirements_chats(**document))
    return all_staticChatHistory

async def remove_staticChatHistory(userID,conversationID):
    await static_requirements_chats.delete_one({"userID":userID},{"conversationID":conversationID})
    return True
#===========================ping db==================================
async def main():
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
# ============================================================================
# Since the asyncio event loop is already running, we should call main() with await
import asyncio

asyncio.get_event_loop().create_task(main())
# # Example FAQs to store

# # Store them using the new function
if __name__ == "__main__":
    import asyncio
    # faq1 = FAQ(question="What is Python?", answer="Python is a programming language.")
    faq2 = FAQ(
        question="what is agent smiths? i want to know all of its functionalities. suppose i want to build a websirte using it how do i do that? tekll me every thing you know about agantsmiths", 
        answer="AgentSmiths is an AI-powered website builder that makes creating a website as easy as having a conversation! You can sign up or log in on the AgentSmiths website to get started. This user manual provides comprehensive information on how to use AgentSmiths to build your dream website"
        )
    # asyncio.run(store_faq(faq1))
    asyncio.run(store_faq(faq2))
