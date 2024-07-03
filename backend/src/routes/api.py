from services.chatbot.bot import chatbot
from fastapi import FastAPI
from socketio import AsyncServer
from socketio.asgi import ASGIApp
from fastapi.middleware.cors import CORSMiddleware

import importlib
support_human_user_connect=getattr(importlib.import_module('models.support_human_user_connect'), 'SupportHumanUserConnect')()


app = FastAPI()
origins=['http://127.0.0.1:3001',"http://localhost:3001"] #add your orodings here
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

@sio.on("chat")
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
asgi_app = ASGIApp(sio, app)

if __name__ == "__main__":
    pass
