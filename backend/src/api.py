# from sockets import sio_app
import socketio
from agents.agent import responseAgent

from services.chatbot.bot import chatbot
from fastapi import FastAPI
from socketio import AsyncServer
from socketio.asgi import ASGIApp
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount('/',app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creating socketio server
origins=['http://127.0.0.1:3000'] #add your orodings here
sio_server = socketio.AsyncServer(
    async_mode='asgi', 
    cors_allowed_origins=[]
) 

ra = responseAgent()

@app.get('/')
async def home():
    return {'message':'Hello Developers!'}


@sio_server.on("connect")
async def connect(sid, environ):
    print(f"Client connected with SID: {sid}")
    await sio_server.emit("message", {"data": "Welcome!"}, to=sid)


bots = {}

@sio_server.on("init")
async def init(sid):
    bot = chatbot(sid)
    bot.bot_init()
    bots[sid] = bot
    print(f"Client with SID {sid} initialized with data:")

@sio_server.on("chat")
async def handle_message(sid, data):
    print(f"Message from {sid}: {data}")
    bot = bots.get(sid)
    if bot:
        await sio_server.emit("response", bot.bot_chat(data), to=sid)
        print("Response sent")
    else:
        print(f"No bot found for SID {sid}")

@sio_server.on("close")
async def disconnect(sid):
    print(f"Client disconnected with SID: {sid}")
    if sid in bots:
        del bots[sid]

###########################

@sio_server.event
async def connect(sid,environ,auth):
    print(f'{sid} : connected')
    await sio_server.emit('join',{'sid':sid})

@sio_server.event
async def chat(sid,message):
    await sio_server.emit('chat',{'sid':sid,'message':message})
    response = ra.chainquery({"response": message})
    if response:
        print(f'Response for message "{message}": {response}')  # Print the response
        await sio_server.emit('chat_response', {'sid': sid, 'message': response})   

@sio_server.event
async def disconnect(sid):
    print(f'{sid} : diconnected')

# asgi_app = ASGIApp(
#   sio_server, 
#   app)

# Creating socketio app from socketio server
sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets',
)
