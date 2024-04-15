import socketio

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

@sio_server.event
async def disconnect(sid):
    print(f'{sid} : diconnected')