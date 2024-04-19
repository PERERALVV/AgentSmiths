import socketio
from agents.agent import responseAgent

ra = responseAgent()

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