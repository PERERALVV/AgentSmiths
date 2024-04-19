import asyncio
import websockets
from agent import responseAgent

v = responseAgent()

async def receive_messages(websocket):
    while True:
        # Receive messages from app.py
        message = await websocket.recv()
        print("Received message from app.py:", message)
        
        # Process the received message
        result = process_message(message)
        print("Reply message from chainquery:", result)
        
        # Send the response back to app.py
        await websocket.send("demo_response:" + result)

def process_message(message):
    # Process the message with the responseAgent
    result = v.chainquery({"response": message})
    # Return the response obtained from the responseAgent
    return result

async def connect_to_app():
    uri = "ws://localhost:8000/ws"  # Assuming app.py is running on this address
    async with websockets.connect(uri) as websocket:
        await receive_messages(websocket)

async def main():
    # Start connecting to app.py
    await connect_to_app()

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
