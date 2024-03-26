from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()

# Store connected WebSocket clients
clients = set()

# WebSocket route for handling incoming connections
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)

    try:
        while True:
            # Receive message from client
            message = await websocket.receive_text()

            # Check message type
            message_type, payload = message.split(":", 1)
            if message_type == "frontend":
                # Message from frontend, broadcast to all connected clients
                for client in clients:
                    await client.send_text(payload)
            elif message_type == "demo_response":
                # Response from demo.py, print it
                print("Received response from demo.py:", payload)

    except WebSocketDisconnect:
        # Remove client when disconnected
        clients.remove(websocket)