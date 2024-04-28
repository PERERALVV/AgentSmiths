import React, { useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:8000');

function App() {
  useEffect(() => {
    socket.on('connect', () => {
      console.log('Connected to server');
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div className="App">
      {/* Your app code here */}
    </div>
  );
}

export default App;


from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = FastAPI()
app_asgi = socketio.ASGIApp(sio, app)

@sio.event
async def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)