from models.model import requirements_chats
#MongoDB Driver
import motor.motor_asyncio
from urllib.parse import quote_plus

username = quote_plus('gayuni')
password = quote_plus('Vkied60fwvEnLarr')

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://'+username+':'+password+'@cluster0.mhaksto.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
database = client.AGENTSMTHS
collection = database.requirements_chats

async def create_chatHistory(chatHistory):
    document = chatHistory
    result = await collection.insert_one(document)
    return document

async def fetch_one_chatHistory(userID):
    document = await collection.find_one({"userID":userID})
    return document

async def fetch_all_chatHistory():
    all_chatHistory=[]
    cursor = collection.find({})
    async for document in cursor:
        all_chatHistory.append(requirements_chats(**document))
    return all_chatHistory

async def update_chatHistory(userID,conv):
    await collection.update_one({"userID":userID},{"$set":{"conversation":conv}})
    document = await collection.find_one({"userID":userID})
    return document

async def remove_chatHistory(userID):
    await collection.delete_one({"userID":userID})
    return True
