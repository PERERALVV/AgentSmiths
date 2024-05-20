import socketio
from core.agents.chatllm import chatllm

# from agentsOld.agent import responseAgent

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from services.chatbot.bot import chatbot

# ra = responseAgent()
cl = chatllm()

# Creating socketio server
sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

# Creating socketio app from socketio server
sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets',
)

@sio_server.event
async def connect(sid,environ,auth):
    print(f'{sid} : connected')
    await sio_server.emit('join',{'sid':sid})
    await sio_server.emit("message", {"data": "Welcome!"}, to=sid)

@sio_server.event
async def chat(sid,message):
    await sio_server.emit('chat',{'sid':sid,'message':message})
    # response = ra.chainquery({"response": message})
    response = cl.talk(message)
    if response:
        print(f'Response for message "{message}": {response}')  # Print the response
        await sio_server.emit('chat_response', {'sid': sid, 'message': response})   

@sio_server.event
async def disconnect(sid):
    print(f'{sid} : diconnected')