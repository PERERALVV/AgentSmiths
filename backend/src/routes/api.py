# from services.chatbot.bot import chatbot
# from fastapi import FastAPI
# from socketio import AsyncServer
# from socketio.asgi import ASGIApp
# from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# origins=['http://127.0.0.1:3000'] #add your orodings here
# sio = AsyncServer(async_mode='asgi', cors_allowed_origins=origins
#                   ) 
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @sio.on("connect")
# async def connect(sid, environ):
#     print(f"Client connected with SID: {sid}")
#     await sio.emit("message", {"data": "Welcome!"}, to=sid)


# bots = {}

# @sio.on("init")
# async def init(sid):
#     bot = chatbot(sid)
#     bot.bot_init()
#     bots[sid] = bot
#     print(f"Client with SID {sid} initialized with data:")

# @sio.on("chat")
# async def handle_message(sid, data):
#     print(f"Message from {sid}: {data}")
#     bot = bots.get(sid)
#     if bot:
#         await sio.emit("response", bot.bot_chat(data), to=sid)
#         print("Response sent")
#     else:
#         print(f"No bot found for SID {sid}")

# @sio.on("close")
# async def disconnect(sid):
#     print(f"Client disconnected with SID: {sid}")
#     if sid in bots:
#         del bots[sid]


# asgi_app = ASGIApp(sio, app)