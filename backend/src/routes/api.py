from services.chatbot.bot import chatbot
from fastapi import FastAPI
from socketio import AsyncServer
from socketio.asgi import ASGIApp
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import importlib
support_human_user_connect=getattr(importlib.import_module('models.support_human_user_connect'), 'SupportHumanUserConnect')()


app = FastAPI()
origins=['http://127.0.0.1:3001',
         "http://localhost:3002",
         "http://localhost:3001",
         "http://localhost:3000",
         ] #add your orodings here
# origins=['*'] #add your orodings here
sio = AsyncServer(async_mode='asgi', cors_allowed_origins=origins
                  ) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# ========================================for ai bot chat==========================================
def is_active_sid(sid, sio=sio):
    return sio.manager.is_connected(sid, '/')

bots = {}#connected unreg users
@sio.on("connect")
async def connect(sid, environ):
    print(f"Client {sid} connected")


@sio.on("disconnect")
async def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.on("init")
async def init(sid):
    bot = chatbot(sid)
    await bot.bot_init()
    bots[sid] = bot
    print(f"Client with SID {sid} initialized with data:")

@sio.on("support/chat")
async def handle_message(sid, data):
    print(f"Message from {sid}: {data}")
    bot = bots.get(sid)
    if bot:
        response= await bot.bot_chat(data)
        await sio.emit("response", response, to=sid)
        # await sio.emit("response",data, to=sid) #for testing
        print("Response sent")
    else:
        print(f"No bot found for SID {sid}")

@sio.on("close")
async def disconnect(sid):
    if sid in bots:
        await bots[sid].bot_close()
        bots.pop(sid, None)
        print(f"Client disconnected with SID: {sid}")
# ==========================================================================================================================

# ========================================for human connected chat==========================================

@sio.on("connect_to_human")#when user requests to connect to human
async def connect_human(sid):
    bot = bots.get(sid)
    if bot:
        await bot.connect_human()
        support_human_user_connect.user_requesting_human_support(sid)
        # await sio.emit("human_result","connected", to=sid)

@sio.on("init_human")#support agent opens page
async def init_human(sid,username):
    support_human_user_connect.support_agent_connected(sid)
    print(f"Human {username} with SID {sid} initialized")

@sio.on("close_human")#support agent closes page
async def close_human(sid,username):
    support_human_user_connect.support_agent_disconnected(sid)
    print(f"Human disconnected with SID: {sid}")

@sio.on("human_accept")
async def human_accept(sid, data):
    user=data["user_id"]
    if user in support_human_user_connect.users_requesting_human_support:
        support_human_user_connect.add_pair(user, sid)
        await sio.emit("connection_result_to_human","connected", to=sid)
        await sio.emit("connection_result_to_user","connected", to=user)
        support_human_user_connect.users_requesting_human_support.remove(user)
        print(f"Human {sid} accepted connection request from user {user}")
    else:
        await sio.emit("connection_result_to_user","error", to=user)
        await sio.emit("connection_result_to_human","error", to=sid)

@sio.on("chat_from_human")#when human sends a message to user
async def chat_from_human(sid, data):
    user=support_human_user_connect.get_user(sid)
    if support_human_user_connect.is_connected(sid) and support_human_user_connect.is_connected(user):
        response=data["data"]
        await sio.emit("response", response, to=user)
        print("Response sent")
    else:
        print(f"No connected user found for agent {sid}")

@sio.on("chat_to_human")#when user sends a message to human
async def chat_to_human(sid, msg):
    human=support_human_user_connect.get_agent(sid)#get human sid
    if support_human_user_connect.is_connected(sid) and support_human_user_connect.is_connected(human):
        response={"user_id":sid,"data":msg}
        await sio.emit("chat_from_bot", response, to=human)
        print("Response sent")
    else:
        print(f"No human found for user {sid}")

@sio.on("chat_Finished")
async def chatFinished(sid):
    print(f"Chat finished with {sid}")
    user=support_human_user_connect.get_user(sid)
    if support_human_user_connect.is_connected(sid) and support_human_user_connect.is_connected(user):
        await sio.emit("chatFinished", to=user)
        support_human_user_connect.remove_pair(sid)
        print("Chat finished")
    else:
        print(f"No connected pair found for agent {sid} and user {user}")

getchat=getattr(importlib.import_module('database.database'), 'retrieve_chats_by_attribute')

@app.get("/chatlist")
async def chatlist():
    res = await getchat("connect_to_human", True)
    res=[r.model_dump() for r in res]
    resp=[]
    for chat in res:
        if is_active_sid(sid=chat['user_id']) and chat['user_id'] in support_human_user_connect.users_requesting_human_support:
        # if True:
            chat['messages'] = [
                {
                    'message': message['message'],
                    'direction': 'outgoing' if message['sender'] == 'bot' else 'incoming',
                    'sender': 'SupportBot' if message['sender'] == 'bot' else 'User'
                }
                for message in chat['messages']
            ]
            del chat['connect_to_human']
            resp.append(chat)

    return resp


from typing import List
ChatMessage=getattr(importlib.import_module('models.review_chat'), 'ChatMessage')
ReviewChat=getattr(importlib.import_module('models.review_chat'), 'ReviewChat')

store_for_review=getattr(importlib.import_module('database.database'), 'store_review_chat')
@app.post("/reviewChat")
async def review_chat(chat_review: List[ChatMessage]):
    review_chat=ReviewChat(chat=chat_review)
    await store_for_review(review_chat)
# ==========================================================================================================


# =========================================faq parts========================================================

getfaqs=getattr(importlib.import_module('database.database'), 'retrieve_faqs')
@app.get("/faq")
async def faq():
    resp = await getfaqs()
    resp=[r.model_dump() for r in resp]
    return resp
# =========================================faq parts over====================================================



project_class=getattr(importlib.import_module('models.project'), 'Project')
# ==============================dynamic chat parts(gayuni)======================================================
create=getattr(importlib.import_module('core.env.Agent_environment'), 'create')
is_message_legitimate=getattr(importlib.import_module('core.validators.prompt_validator'), 'is_message_legitimate')
is_qna_match=getattr(importlib.import_module('core.validators.qna_validator'), 'is_qna_match')

from typing import Dict, Any
from core.validators.clarify_question import get_clarification
from models.model import requirements_chats
from database.database import (
    create_chatHistory,
    fetch_one_chatHistory,
    fetch_all_chatHistory,
    remove_chatHistory,
)
from models.model import static_requirements_chats
from database.database import (
    create_staticChatHistory,
    fetch_one_staticChatHistory,
    fetch_all_staticChatHistory,
    remove_staticChatHistory,
)


user_responses: Dict[str, asyncio.Queue] = {}
active_users: Dict[str, Dict[str, Any]] = {}

async def generate_code(bot_response:str,user_sid:str)->str:
    if user_sid not in user_responses:
        user_responses[user_sid] = asyncio.Queue()
    await sio.emit('message_exchange', {'sid': user_sid, 'message': bot_response})

    # Wait for the response and take the last element from the queue
    user_response = await user_responses[user_sid].get()
    print(f'The generate_code function received the message : {user_response}')
    return user_response


async def talk_to_user(msg,sid):
    if msg.lower() == "exit":
        print("chat ended")
        #TODO: send emit to font end to stop the chat
        await sio.emit("end_conversation",to=sid)
        return True
    while True:
        try:
            ans=await generate_code(msg,sid)
            print(f"User response: {ans}")
            if len(ans.split())>5:
                legitamacy=is_message_legitimate(ans)
            else:
                legitamacy=True
            # qna_match=is_qna_match(msg,ans)
            qna_match=True
            print(f"msg and ans: {msg} {ans}")
            if not qna_match:
                response = 'The answer you provided does not answer the question, \
                    please provide a valid answer'
                await sio.emit('message_exchange', {'sid': sid, 'message': response})
            elif not legitamacy:
                response = 'An illegitimate prompt injection was detected. \
                    Please note that after 3 illegitimate attempts, \
                        your user account will be banned from AgentSmiths.'
                await sio.emit('warning', {'sid': sid, 'message': response})
            else:
                break
                # pass
        except Exception as e:
            print(f"convo ended due to  err {e}")
        await asyncio.sleep(1)
    return ans

@sio.on("start_conversation")
async def start_conversation(sid):
    project = project_class()  
    userID = sid
    # # userID = auth.get('userID') 
    active_users[sid] = {
        "userID": userID, 
        "conversation": []
    }
    print(f'{sid} : start_conversation')
    print(f"Client with SID {sid} initialized with data:")
    project_name = await generate_code("Please enter the name of your Website",sid)
    print(f'Project name: {project_name}')
    try:
        project = await create(project,userID,sid,project_name,talk_to_user)
    except Exception as e:
        print(f"Error in creating project {e}")
        await sio.emit("something_wrong", to=sid)
    await sio.emit("code_ready", to=sid)
    # temp_bot_response = 'Hi why did you come here?'
    # active_users[sid]["conversation"].append({"bot": temp_bot_response})
    # received_user_response = await generate_code(temp_bot_response,sid)
    # print(f'YAYYYYYYYYYY!!! we got it : {received_user_response}')

@sio.on("end_conversation")
async def end_conversation(sid):
    if sid in active_users:
        user_data = active_users.pop(sid)
        userID = user_data["userID"]
        conversation = user_data["conversation"]
        
        # Create a document for the chat history
        chatHistory = requirements_chats(userID=userID, conversation=conversation)
        await post_chatHistory(chatHistory)
    print(f'{sid} : conversation saved')

@sio.on("message_exchange")
async def message_exchange(sid,message):
    print(f'{sid} : Got a reply from user')
    if sid in user_responses:
        print(f'user sid is inside user_response')
        await user_responses[sid].put(message)
        # saved_message = await user_responses[sid].get() #This will cause the function to block until another message is received
        print(f'{sid} : Saved users reply in the user_responses')


@sio.on("help_answer")
async def help_answer(sid,message):
    response=get_clarification(message)
    if response:
        print(f'Response for message "{message}": {response}') 
        await sio.emit('chat_response', {'sid': sid, 'message': response})
    else:
        print('No clarification received')

@app.post("/api/chatHistory", response_model=requirements_chats)
async def post_chatHistory(chatHistory:requirements_chats):
    response = await create_chatHistory(chatHistory.dict())
    if response:
        return response
    raise HTTPException(400,"Something went wrong / Bad request")

@app.get("/api/chatHistory")
async def get_requirement():
    response = await fetch_all_chatHistory()
    return response

@app.get("/api/chatHistory{userID}", response_model=requirements_chats)
async def get_requirement_by_id(userID):
    response = await fetch_one_chatHistory(userID)
    if response:
        return response
    raise HTTPException(404, f"There is no conversation by the user ID {userID}")

@app.delete("/api/chatHistory{userID}")
async def delete_chatHistory(userID):
    response = await remove_chatHistory(userID)
    if response:
        return "Successfully deleted conversation"
    raise HTTPException(404, f"There is no conversation by the user ID {userID}")

# ===========static chat==========================================================================================
WEBSITE= getattr(importlib.import_module('models.website'), 'WEBSITE')
start=getattr(importlib.import_module('core.html.process'), 'start')
@sio.on("static_chat")
async def static_chat(sid,uid,convID,conv,desc):
    print('RECEIVED!!!!!!!!!!!')
    try:
        staticChatHistory = static_requirements_chats(userID=uid, conversationID=convID, conversation=conv, description=desc)
        website=WEBSITE()
        name=conv[0]['answers']
        start(website,name,uid,sid,desc)
        await post_staticChatHistory(staticChatHistory)
        print(f'{uid} ({sid}) : disconnected and static website conversation saved')
        await sio.emit("chat_updated", {"status": "success"}, room=sid)
    except Exception as e:
        print(f"Error updating conversation: {str(e)}")
        await sio.emit("chat_updated", {"status": "error", "message": str(e)}, room=sid)

@app.post("/api/staticChatHistory", response_model=static_requirements_chats)
async def post_staticChatHistory(staticChatHistory:static_requirements_chats):
    response = await create_staticChatHistory(staticChatHistory.dict())
    if response:
        return response
    raise HTTPException(400,"Something went wrong / Bad request")

@app.get("/api/staticChatHistory")
async def get_requirement():
    response = await fetch_all_staticChatHistory()
    return response

@app.get("/api/staticChatHistory{userID}", response_model=static_requirements_chats)
async def get_requirement_by_id(userID):
    response = await fetch_one_staticChatHistory(userID)
    if response:
        return response
    raise HTTPException(404, f"There is no conversation by the user ID {userID}")

@app.delete("/api/staticChatHistory{userID}")
async def delete_staticChatHistory(userID):
    response = await remove_staticChatHistory(userID)
    if response:
        return "Successfully deleted conversation"
    raise HTTPException(404, f"There is no conversation by the user ID {userID}")

#================ayesha code==========================================================================
from fastapi import HTTPException, Depends, UploadFile, Form, File, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from bson import ObjectId
from jose import jwt, JWTError
from utils.jwt_handler import signJWT
import logging
import os
import shutil
from datetime import datetime
from utils.auth import get_password_hash, verify_password, create_access_token, get_current_user
from models.user import Signup, EmailCheck, OtpCheck, PasswordChange, Login, updateProfile,UserModel,ProjectModel,ReviewChat
from database.database import user_collection, forgot_password_collection, projects_collection,review_chat_collection,feedback_collection
from utils.get_userId import get_current_user_id
from werkzeug.security import generate_password_hash, check_password_hash
from utils.otp import email_alert
from typing import List

logger = logging.getLogger(__name__)

class Process:
    env = {
        "COOKIE_EXPIRES_TIME": os.getenv("COOKIE_EXPIRES_TIME", "1"),
        "SECRET_KEY": os.getenv("SECRET_KEY", "dc3cc26aa8816c0aa4cb3dbd1c93192b70d324cba8d584a90148bb77658d36daf1c84e128ae5aee5a38df03a489e893b952c90c5c7dc14ceae0a591b289aa2973200e60dba945724bd2394e976c1235e121f622fd2cd32d35b1bcfc69a9c56637e579f4492a985993f38f854a4b391123b18e0cd064c997eceb79fbd2a46ed72869001364f67604c3770101406e6e327a05ba9950277a8654e820c38b163f95f38f6f2e2655326a436dab7f2fab37e755f2df219e48d6f16b7067dbbc1ac4994b2b9e9474fa223706539b97e5871eea210a0812d8cfa48eab46a139eb3d3c3e767742a406ee0b5c12b5faed988610a980b5fc644726583b7143e52af628d874b"),
        "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM", "HS256"),
        "NODE_ENV": os.getenv("NODE_ENV", "production")
    }

async def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, Process.env["SECRET_KEY"], algorithms=[Process.env["JWT_ALGORITHM"]])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        
        user = await user_collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        
        user["_id"] = str(user["_id"])
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

def convert_datetime_to_string(data):
    if isinstance(data, dict):
        return {key: convert_datetime_to_string(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_datetime_to_string(item) for item in data]
    elif isinstance(data, datetime):
        return data.isoformat()
    else:
        return data

@app.post("/login")
async def login_for_access_token(login: Login):
    user = await user_collection.find_one({"name": login.name})
    if not user or not check_password_hash(user["password"], login.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = str(user["_id"])
    role = user.get("role", "user")  # Assuming role is stored in the user document

    token = signJWT(user_id, role)
    
    return token

@app.get("/userDetails")
async def get_user_details(current_user: str = Depends(get_current_user_id)):
    logger.info("Fetching user details for: %s", current_user)
    user = await user_collection.find_one({"_id": ObjectId(current_user)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])
    return user

@app.post("/updateProfile")
async def update_profile(
    name: str = Form(...),
    bio: str = Form(...),
    address: str = Form(...),
    phoneNumber: str = Form(...),
    dob: str = Form(...),
    profession: str = Form(...),
    avatar: UploadFile = File(None),
    current_user: str = Depends(get_current_user_id),
):
    update_data = {
        "name": name,
        "bio": bio,
        "address": address,
        "phoneNumber": phoneNumber,
        "dob": dob,
        "profession": profession,
    }

    if avatar:
        # Ensure the avatars directory exists
        avatar_dir = "avatars"
        if not os.path.exists(avatar_dir):
            os.makedirs(avatar_dir)
        
        # Save the avatar file
        avatar_path = f"{avatar_dir}/{current_user}_{avatar.filename}"
        with open(avatar_path, "wb") as buffer:
            shutil.copyfileobj(avatar.file, buffer)
        update_data["avatar"] = avatar_path

    await user_collection.update_one({"_id": ObjectId(current_user)}, {"$set": update_data})
    return {"message": "Profile updated successfully"}

@app.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logout successful"}, status_code=200)
    response.delete_cookie("token")
    return response

@app.post("/signup")
async def signup(user: Signup):
    userdetail = await user_collection.find({"email": user.email}).to_list(length=None)
    if userdetail:
        return {"message": "User already exists"}

    hashed_password = generate_password_hash(user.password)
    user_dict = dict(user)
    user_dict["password"] = hashed_password
    user_dict["role"] = "user"  # Assign 'user' role here
    await user_collection.insert_one(user_dict)
    
    return {"message": "Success"}

@app.post("/emailCheck", response_model=bool)
async def check_email_existence(emailcheck: EmailCheck):
    email = emailcheck.email
    user = await user_collection.find_one({"email": email})
    if user:
        email_alert("OTP Verification", email)
        return True
    else:
        return False

@app.post("/otpCheck", response_model=bool)
async def otpCheck(details: OtpCheck):
    email = details.email
    otp = details.otp
    user = await forgot_password_collection.find_one({"email": email})
    if user:
        stored_otp = user.get("otp")
        if stored_otp == otp:
            return True
        return False
    return False

@app.post("/passwordChange")
async def change_password(password_change_data: PasswordChange):
    email = password_change_data.email
    newPassword = password_change_data.new_password

    user = await user_collection.find_one({"email": email})
    if not user:
        return JSONResponse(status_code=404, content={"message": "User not found."})

    update_result = await user_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"password": generate_password_hash(newPassword)}}
    )

    if update_result.modified_count == 1:
        return JSONResponse(status_code=200, content={"message": "Password updated successfully."})
    else:
        return JSONResponse(status_code=500, content={"message": "Failed to update password."})
    
@app.get("/users")
async def read_users(current_user: str = Depends(get_current_user_id)) -> List[dict]:  
    try:
        # Fetch all user documents and convert the result to a list
        all_users = await user_collection.find().to_list(length=None)
        users = []
        for user in all_users:
            user_dict = {
                "id": str(user["_id"]),
                "email": user["email"],
                "name": user["name"]
            }
            if "role" in user:
                user_dict["role"] = user["role"]
            if "bio" in user:
                user_dict["bio"] = user["bio"]
            if "address" in user:
                user_dict["address"] = user["address"]
            if "phoneNumber" in user:
                user_dict["phoneNumber"] = user["phoneNumber"]
            if "dob" in user:
                user_dict["dob"] = user["dob"]
            if "profession" in user:
                user_dict["profession"] = user["profession"]
            users.append(user_dict)
        return users
    except Exception as e:
        logger.error(f"Error retrieving user details: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve user details")
    
@app.put("/users/{user_id}", response_model=UserModel)
async def update_user(user_id: str, updated_user: UserModel, current_user: str = Depends(get_current_user_id)) -> UserModel:
    try:
        user_data = updated_user.dict(exclude_unset=True)
        update_result = await user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
        
        if update_result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        updated_user_data = await user_collection.find_one({"_id": ObjectId(user_id)})
        updated_user_data["_id"] = str(updated_user_data["_id"])
        return updated_user_data
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# Delete a user by ID
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: str,current_user: str = Depends(get_current_user_id)):
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": f"User {user_id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.get("/projects/count")
async def get_project_count() -> dict:
    try:
        count = await projects_collection.count_documents({})
        return {"count": count}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to retrieve project count")

@app.get("/users/count")
async def get_user_count() -> dict:
    try:
        count = await user_collection.count_documents({})
        return {"count": count}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to retrieve user count")
    
@app.get("/support-chat/count")
async def get_chat_count() -> dict:
    try:
        count = await review_chat_collection.count_documents({})
        return {"count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve chat count: {str(e)}")

@app.get("/adminfeedback/count")
async def get_feedback_count() -> dict:
    try:
        count = await feedback_collection.count_documents({})
        return {"count": count}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to retrieve feedback count")
    
@app.get("/projects", response_model=List[ProjectModel])
async def read_projects(current_user: str = Depends(get_current_user_id)):
    try:        
        cursor = projects_collection.find({}, {"userID": 1, "projectName": 1, "_id": 0})
               
        projects = []
        async for project in cursor:
            project_model = ProjectModel(
                userID=project["userID"],
                projectName=project["projectName"]
                
            )
            projects.append(project_model)
        
        return projects
    
    except Exception as e:
        logger.error(f"Error retrieving projects: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve projects")
    
@app.delete("/projects/{project_id}", response_model=dict)
async def delete_project(project_id: str, current_user: str = Depends(get_current_user_id)):
    try:
        
        result = await projects_collection.delete_one({"userID": project_id})
        
        
        if result.deleted_count == 1:
            return {"message": f"Project {project_id} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Project not found")
    
    except Exception as e:
        logger.error(f"Error deleting project: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete project")
    
@app.get("/support-chat", response_model=List[ReviewChat])
async def get_chat_messages(current_user: str = Depends(get_current_user_id)):
    try:
        chat_documents = await review_chat_collection.find().to_list(None)  # Await the find operation and convert to list
        chat_messages = []
        for chat in chat_documents:
            chat['_id'] = str(chat['_id'])  # Convert ObjectId to string
            chat_messages.append(ReviewChat(id=chat['_id'], chat=chat['chat']))
        return chat_messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching chat messages: {str(e)}")
    
# API endpoint to delete a chat
@app.delete("/support-chat/{chat_id}")
async def delete_chat_message(chat_id: str,current_user: str = Depends(get_current_user_id)):
    try:
        result = await review_chat_collection.delete_one({"_id": ObjectId(chat_id)})
        if result.deleted_count == 1:
            return {"message": "Chat message deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Chat message not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting chat message: {str(e)}")
    
@app.get("/adminfeedback", response_model=List[dict])
async def read_feedback(current_user: str = Depends(get_current_user_id)) -> List[dict]:
    try:
        # Fetch all documents and convert the result to a list
        all_feedbacks = await feedback_collection.find().to_list(length=None)
        
        # Sort feedbacks by '_id' (assuming '_id' is a timestamp field)
        sorted_feedbacks = sorted(all_feedbacks, key=lambda x: x['_id'].generation_time, reverse=True)
        
        feedbacks = []
        for feedback in sorted_feedbacks:
            feedback_dict = {
                "_id": str(feedback["_id"]),  # Convert ObjectId to string
                "topic": feedback.get("topic", "Feedback"),  # Default to "Feedback" if not present
                "message": feedback.get("message", "<p>hello</p>"),  # Default to "<p>hello</p>" if not present
                "status": feedback.get("status", "unread")  # Default to "unread" if not present
            }
            feedbacks.append(feedback_dict)
        
        return feedbacks
    except Exception as e:
        logger.error(f"Error retrieving feedback details: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve feedback details")

@app.delete("/adminfeedback/{feedback_id}")
async def delete_feedback(feedback_id: str, current_user: str = Depends(get_current_user_id)):
    try:
        # Convert feedback_id to ObjectId
        feedback_object_id = ObjectId(feedback_id)

        # Delete the feedback document from the collection
        result = await feedback_collection.delete_one({"_id": feedback_object_id})

        if result.deleted_count == 1:
            return {"message": "Feedback deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Feedback not found")
    except Exception as e:
        logger.error(f"Error deleting feedback: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete feedback")
    
@app.put("/adminfeedback/{feedback_id}/update", response_model=dict)
async def update_feedback_status(feedback_id: str, current_user: str = Depends(get_current_user_id)) -> dict:
    try:
        # Update feedback status to "read"
        result = await feedback_collection.update_one(
            {"_id": ObjectId(feedback_id)},
            {"$set": {"status": "read"}}
        )
        
        if result.modified_count == 1:
            updated_feedback = await feedback_collection.find_one({"_id": ObjectId(feedback_id)})
            updated_feedback["_id"] = str(updated_feedback["_id"])  # Convert ObjectId to string
            return updated_feedback
        else:
            raise HTTPException(status_code=404, detail="Feedback not found")
    except Exception as e:
        logger.error(f"Error updating feedback status: {e}")
        raise HTTPException(status_code=500, detail="Failed to update feedback status")


# =================ravindu's code=======================
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import os

BASE_PATH = '../workspace/static/'
@app.get("/get-html-files", response_class=JSONResponse)
async def get_html_files():
    html_files = sorted(
        [f for f in os.listdir(BASE_PATH) if f.endswith('.html')])
    return {"files": html_files}


@app.get("/get-html-css/{filename}", response_class=JSONResponse)
async def get_html_css(filename: str):
    html_file_path = os.path.join(BASE_PATH, filename)
    css_file_path = os.path.join(BASE_PATH, filename.replace('.html', '.css'))

    if not os.path.exists(html_file_path):
        return JSONResponse(content={'error': 'HTML file not found'}, status_code=404)

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    css_content = ""
    if os.path.exists(css_file_path):
        with open(css_file_path, 'r', encoding='utf-8') as file:
            css_content = file.read()

    return JSONResponse(content={'html': html_content, 'css': css_content})


@app.post("/save-html")
async def save_html(request: Request):
    data = await request.json()
    filename = data.get('filename')
    html_content = data.get('html')

    if not filename or not html_content:
        raise HTTPException(
            status_code=400, detail="Filename and HTML content are required")

    css_filename = filename.replace('.html', '.css')
    html_with_css_link = f'<link rel="stylesheet" href="{css_filename}">\n{html_content}'

    html_file_path = os.path.join(BASE_PATH, filename)
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_with_css_link)

    return {"message": "HTML content saved successfully"}


@app.post("/save-css")
async def save_css(request: Request):
    data = await request.json()
    filename = data.get('filename')
    css_content = data.get('css')

    if not filename or not css_content:
        raise HTTPException(
            status_code=400, detail="Filename and CSS content are required")

    css_file_path = os.path.join(BASE_PATH, filename)
    with open(css_file_path, 'w', encoding='utf-8') as file:
        file.write(css_content)

    return {"message": "CSS content saved successfully"}

from pydantic import BaseModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import base64
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

load_dotenv()

class EmailRequest(BaseModel):
    topic: str
    message: str


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("SMTP_EMAIL")
EMAIL_TO = os.getenv("SMTP_EMAIL")

username = quote_plus('ayesha')
password = quote_plus('pTPivwignr4obw2U')
cluster = 'cluster0.mhaksto.mongodb.net'
uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'
client = AsyncIOMotorClient(uri)
db = client['AGENTSMTHS']
collection = db['feedback']


def extract_base64_images(html):
    img_tags = re.findall(
        r'<img src="data:image/(png|jpeg|jpg);base64,([^"]+)"', html)
    images = []
    for i, img in enumerate(img_tags):
        image_type, image_data = img
        image_data = base64.b64decode(image_data)
        image_filename = f'image{i}.{image_type}'
        images.append((image_filename, image_data, image_type))
        html = html.replace(
            f'data:image/{image_type};base64,{img[1]}', f'cid:{image_filename}')
    return html, images


@app.post("/send-email")
async def send_email(request: EmailRequest):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = request.topic

        html_content, images = extract_base64_images(request.message)

        body = MIMEText(html_content, "html")
        msg.attach(body)

        for filename, image_data, image_type in images:
            image = MIMEImage(image_data, _subtype=image_type)
            image.add_header('Content-ID', f'<{filename}>')
            msg.attach(image)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        feedback_data = {"topic": request.topic, "message": request.message}
        result = await collection.insert_one(feedback_data)
        if not result.inserted_id:
            raise HTTPException(
                status_code=500, detail="Failed to save feedback")

        return {"message": "Email sent and feedback saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# ================ayesha notification code=======================
from configparser import ConfigParser
from motor.motor_asyncio import AsyncIOMotorClient
import google.generativeai as genai
from fastapi import FastAPI, HTTPException, BackgroundTasks, WebSocket
from urllib.parse import quote_plus
from bson import ObjectId
from bson.json_util import dumps
import textwrap
from pydantic import BaseModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import asyncio
import logging
from datetime import datetime
import json 
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("noti_google_api_key")

username = quote_plus('ayesha')
password = quote_plus('pTPivwignr4obw2U')
cluster = 'cluster0.mhaksto.mongodb.net'
uri = f'mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0&ssl=true'
client = AsyncIOMotorClient(uri)
db = client['AGENTSMTHS']
collection = db['support_chats']
group_collections = db["group_collections"]
representative_questions_collection = db["representative_questions"]

genai.configure(api_key=api_key)
model_gemini_pro = genai.GenerativeModel("gemini-pro")

safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

@app.get("/fetch_user_messages")
async def fetch_user_messages():
    documents = await collection.find({"status": "Unread"}).to_list(None)
    
    if not documents:
        raise HTTPException(status_code=404, detail="No unread messages found")

    user_messages = []
    for doc in documents:
        if 'messages' in doc:
            user_messages.extend([msg for msg in doc['messages'] if msg.get('sender') == 'user'])

    for doc in documents:
        doc['_id'] = str(doc['_id'])

    return {"user_messages": json.loads(dumps(user_messages)), "documents": json.loads(dumps(documents))}

def check_message_against_clusters(message, representative_questions, threshold=0.75):
    message_embedding = encode_text_sbert(message)
    for rep_question in representative_questions:
        rep_question_embedding = encode_text_sbert(rep_question)
        similarity = cosine_similarity([message_embedding], [rep_question_embedding])[0][0]
        if similarity >= threshold:
            return True
    return False

# Filter out unwanted messages like greetings and thank-yous
def filter_unwanted_messages(messages):
    unwanted_phrases = [
        "hello", "hi", "hey", "greetings", "good morning", "good afternoon",
        "good evening", "thank you", "thanks", "bye", "goodbye"
    ]
    
    filtered_messages = [
        message for message in messages
        if isinstance(message, dict) and 'message' in message and not any(phrase in message['message'].lower() for phrase in unwanted_phrases)
    ]
    
    return filtered_messages

periodic_task = None

async def periodic_cluster_update():
    while True:
        # Background task to run update_or_create_clusters
        await update_or_create_clusters()
        # Adjust sleep time as needed (e.g., every 10 seconds)
        await asyncio.sleep(3)

@app.on_event("startup")
async def startup_event():
    global periodic_task
    # Assign the created task to the global variable
    periodic_task = asyncio.create_task(periodic_cluster_update())

@app.on_event("shutdown")
async def shutdown_event():
    global periodic_task
    if periodic_task:
        # Cancel the periodic task
        periodic_task.cancel()
        try:
            # Wait for the task to be cancelled
            await periodic_task
        except asyncio.CancelledError:
            # This exception is expected when a task is cancelled
            pass
        finally:
            periodic_task = None
            print("Periodic task cancelled and cleaned up")

async def update_or_create_clusters():
    new_messages = await fetch_user_messages()
    documents = await collection.find({"status": "Unread"}).to_list(None)
    
    # Extract user messages and their parent document IDs from all documents
    user_messages = []
    document_id_map = {}  # To map message to its parent document ID
    
    for document in documents:
        doc_id = document['_id']
        messages = document.get('messages', [])
        for msg in messages:
            if msg.get('sender') == 'user':
                user_messages.append(msg)
                document_id_map[msg['message']] = doc_id
    
    # Filter out unwanted messages
    filtered_messages = filter_unwanted_messages(user_messages)
    existing_clusters_docs = await group_collections.find({"status": "Unread"}).to_list(None)
    
    existing_clusters_messages = [message['messages'] for message in existing_clusters_docs]
    
    updated_clusters = []
    for message in filtered_messages:
        cluster_id = check_message_against_clusters(message["message"], existing_clusters_messages)
        
        if cluster_id:
            continue
        else:
            new_cluster = {
                "created_date": datetime.utcnow().isoformat(),
                "status": "Unread",
                "messages": message["message"] 
            }
            insert_result = await group_collections.insert_one(new_cluster)
            updated_clusters.append(str(insert_result.inserted_id))
        existing_clusters_docs = await group_collections.find({"status": "Unread"}).to_list(None)
        existing_clusters_messages = [message['messages'] for message in existing_clusters_docs]
    
    for message in filtered_messages:
        doc_id = document_id_map.get(message["message"])
        if doc_id:
            await collection.update_one({"_id": doc_id}, {"$set": {"status": "read"}})
    
    return {"updated_clusters": updated_clusters}

# Load SBERT model for sentence embeddings
sbert_model = SentenceTransformer('all-mpnet-base-v2')

# Function to encode text using SBERT model
def encode_text_sbert(text):
    return sbert_model.encode([text])[0]

# Function to rephrase a question using the generative AI model
def rephrase_message(question, model_gemini_pro):
    prompt = f"Rephrase the following question as instruction to admin from system to check and solve the user's problem in one sentence more accurately: {question}"
    response = model_gemini_pro.generate_content(prompt)
    return response.text.strip()

# WebSocket endpoint remains unchanged
@app.websocket("/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        unread_clusters = await group_collections.find({"status": "Unread"}).to_list(None)

        if not unread_clusters:
            await websocket.send_json({"message": "No unread clusters found"})
            continue

        for cluster_document in unread_clusters:
            cluster_id = str(cluster_document["_id"])
            messages = cluster_document.get("messages", [])

            if isinstance(messages, str):
                messages = [{"message": messages}]

            rephrased_messages = []
            for message in messages:
                rephrased_message = rephrase_message(message["message"], model_gemini_pro)
                rephrased_messages.append(rephrased_message)

            for message in rephrased_messages:
                notification = {
                    "question": message,
                    "cluster_id": cluster_id
                }
                await websocket.send_json(notification)

        data = await websocket.receive_json()
        action = data.get("action")
        cluster_id = data.get("cluster_id")

        if action in ["Done", "Ignore"] and cluster_id:
            update_query = {"_id": ObjectId(cluster_id)}
            update_fields = {"$set": {"status": "read"}}
            update_result = await group_collections.update_one(update_query, update_fields)

            if update_result.modified_count == 1:
                await websocket.send_json({"message": f"Cluster {cluster_id} status updated"})
            else:
                await websocket.send_json({"message": f"Failed to update status for cluster {cluster_id}"})
        else:
            await websocket.send_json({"message": "Invalid action or cluster ID"})

    await websocket.close()


asgi_app = ASGIApp(sio, app)

if __name__ == "__main__":
    pass
