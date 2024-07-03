# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# # from passlib.context import CryptContext
# # uri = "mongodb+srv://Admin:1234@cluster0.4dfcpe1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# from urllib.parse import quote_plus
# username = quote_plus('ayesha')
# password= quote_plus('pTPivwignr4obw2U')
# cluster = 'cluster0.mhaksto.mongodb.net'
# uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
    

# db = client["AGENTSMTHS"] # Replace with your database name

# collection_name = db["User"]


# fogotPassword = db["user_otp"]


# import asyncio
# import motor.motor_asyncio
# from pydantic import BaseModel, Field
# from typing import List, Optional
# from datetime import datetime
# from bson import ObjectId
# from urllib.parse import quote_plus
# username = quote_plus('ayesha')
# password= quote_plus('pTPivwignr4obw2U')
# cluster = 'cluster0.mhaksto.mongodb.net'
# uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'

# client = motor.motor_asyncio.AsyncIOMotorClient(uri)
# db = client["AGENTSMTHS"] # Replace with your database name
# collection_name = db["User"] # Replace with your collection name
# FogotPassword = client.fogotPassword

# fogotPassword = FogotPassword["user"]
# async def ping_db():
#     try:
#         # The ismaster command is cheap and does not require auth.
#         await db.command("ismaster")
#         print("MongoDB connection is active")
#     except Exception as e:
#         print("Unable to connect to MongoDB: ", e)

# # Call the function
# # asyncio.run(ping_db())
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import os

username = quote_plus('ayesha')
password = quote_plus('pTPivwignr4obw2U')
cluster = 'cluster0.mhaksto.mongodb.net'
uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'

client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

db = client["AGENTSMTHS"]  # Replace with your database name
collection_name = db["User"]
fogotPassword = db["user_otp"]

async def main():
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

# Since the asyncio event loop is already running, we should call main() with await
import asyncio

asyncio.get_event_loop().create_task(main())
