from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()

# Define a global variable to store the message
message = ""

# CORS (Cross-Origin Resource Sharing) middleware to allow requests from any origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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

            # Print the received message in the terminal
            print("Received message:", message)

            # Broadcast message to all connected clients
            for client in clients:
                await client.send_text(message)

    except WebSocketDisconnect:
        # Remove client when disconnected
        clients.remove(websocket)

# Function to get the value of the message variable
def get_message():
    global message
    return message

