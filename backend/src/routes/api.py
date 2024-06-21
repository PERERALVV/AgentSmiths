# from services.chatbot.bot import chatbot
from fastapi import FastAPI
from socketio import AsyncServer
from socketio.asgi import ASGIApp
from fastapi.middleware.cors import CORSMiddleware

# import json
# from metagpt.logs import logger
# from metagpt.context import Context

from core.agents.BA import BA

app = FastAPI()
origins=["http://localhost:3000","http://192.168.56.1:3000"] #add your orodings here
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
# import importlib
# RA=getattr(importlib.import_module('core.agents.ReqAnalyst'), 'RA')
# ra=RA()
# project=getattr(importlib.import_module('models.project'), 'Project')()
# project.name="hondahitha hotels"
# # project.BaSpecification="""{"description": "Simple website for a pizza shop allowing customers to order chicken pizza online.", "features": ["Order pizza online", "View menu (only chicken pizza)", "Select size (standard sizes)"], "ui": {"view_engine": "React", "styling": "Styled Components", "javascript": "JavaScript", "design": "Simple and clean design, with a focus on ease of use for ordering pizza."}, "pages": [{"route": "/", "description": "Displays the menu with the chicken pizza option, allowing users to select a size and proceed to checkout."}, {"route": "/checkout", "description": "Displays the order summary with the selected pizza type and size, allowing the user to confirm the order."}], "page_layout": {"/": {"elements": ["Heading: 'Order Your Chicken Pizza'", "Pizza Image", "Size Selection (e.g., Small, Medium, Large)", "Button: 'Proceed to Checkout'"]}, "/checkout": {"elements": ["Heading: 'Order Summary'", "Pizza Type: Chicken Pizza", "Pizza Size: (Selected Size)", "Button: 'Confirm Order'"]}}}"""
# arch=getattr(importlib.import_module('core.agents.Architect'), 'ARCH')()

# mod=getattr(importlib.import_module('core.actions.modify_spec'), 'ModifySpec')()
# plan=getattr(importlib.import_module('core.actions.plan_development'), 'plan_development')()
# code=getattr(importlib.import_module('core.actions.implement_task'), 'implement_task')()
# project.BaSpecification="""A simple hotel website with a static menu for food ordering.

# The website will have the following pages:

# * Home page: 
#     * Displays a brief description of the hotel (e.g., location, amenities, contact information).
#     * Links to the food menu and contact page.
# * Food menu page:
#     * Displays a static menu of the hotel's restaurant. 
#     * The menu will only feature one type of pizza, with no variations.
#     * Users can submit their order (with their name and phone number) for pickup or delivery.
#     * The order submission form will not allow users to select a specific time for pickup or delivery.
# * Contact page:
#     * Displays the hotel's phone number (0771234567).

# The website will be built using the following technologies:

# * Backend: Node.js with Express framework.
# * Database: MongoDB with Mongoose ORM.
# * Frontend: EJS view engine, Bootstrap for styling, and vanilla JavaScript.

# The website will be implemented in the following way:

# * Home page: The home page will be a simple HTML page with a few paragraphs of text and links to other pages.
# * Food menu page: The menu items (in this case, only one pizza) will be stored in a MongoDB collection. The website will retrieve the menu items from the database and display them on the page. The order submission form will be handled by an Express route, collecting user name and phone number and storing this data in the database. The user will not receive any confirmation of their order after submitting it.
# * Contact page: The contact page will be a simple HTML page with the hotel's phone number.

# The website will not have any user authentication or registration functionality, images or videos. The website will have a basic design with no specific color scheme or font preferences."""
@app.get("/")
async def root():
    return {"message": "Hello World"}
# import json
# getchat=getattr(importlib.import_module('database.database'), 'retrieve_chats_by_attribute')
# @app.get("/chatlist")
# async def chatlist():
#     res = await getchat("connect_to_human", True)
#     res=[r.model_dump() for r in res]
#     for chat in res:
#         chat['messages'] = [
#             {
#                 'message': message['message'],
#                 'direction': 'outgoing' if message['sender'] == 'bot' else 'incoming',
#                 'sender': 'SupportBot' if message['sender'] == 'bot' else 'User'
#             }
#             for message in chat['messages']
#         ]
#         del chat['connect_to_human']
    
#     return res

# @app.get("/test")
# async def test():
#     # result=await ra.act(project)
#     # result=await arch.act(result)
#     # return result
    
#     # try:#this is one way to send some data to the client and get a response and return it by seting timeout as Null but this means the server will wait for the response forever
#     #     res=await sio.call("connect", "sdfdsf",to="dfs",timeout=None)
#     #     return res
#     # except Exception as e:
#     #     print(e)

#     # result=await ra.act(project)
    
#     result=await mod.run(project)
#     result=await ra.act(result)

#     result=await arch.act(result)
#     # print(result)
#     result=await plan.run(result)
#     result=await code.run(result)
#     return result
#     # await plan.run(project)




# @sio.on("connect")
# async def connect(sid, environ):
#     print(f"Client {sid} connected")
#     # await sio.emit("message", {"data": "Welcome!"}, to=sid)

# @sio.on("disconnect")
# async def disconnect(sid):
#     print(f"Client {sid} disconnected")

# bots = {}
# support_humans=[]
# human_connected_users=[]
# @sio.on("init")
# async def init(sid):
#     bot = chatbot(sid)
#     await bot.bot_init()
#     bots[sid] = bot
#     print(f"Client with SID {sid} initialized with data:")

# @sio.on("chat")
# async def handle_message(sid, data):
#     print(f"Message from {sid}: {data}")
#     bot = bots.get(sid)
#     if bot:
#         response= await bot.bot_chat(data)
#         await sio.emit("response", response, to=sid)
#         # await sio.emit("response",data, to=sid) #for testing
#         print("Response sent")
#     else:
#         print(f"No bot found for SID {sid}")

# @sio.on("close")
# async def disconnect(sid):
#     if sid in bots:
#         await bots[sid].bot_close()
#         bots.pop(sid, None)
#         print(f"Client disconnected with SID: {sid}")  

# @sio.on("connect_to_human")
# async def connect_human(sid):
#     bot = bots.get(sid)
#     if bot:
#         await bot.connect_human()
#         human_connected_users.append(sid)
#         await sio.emit("human_result","connected", to=sid)

# @sio.on("init_human")
# async def init_human(sid,data):
#     support_humans.append(data)
#     print(f"Human with SID {sid} initialized")

# @sio.on("close_human")
# async def close_human(sid,data):
#     if sid in support_humans:
#         support_humans.remove(data)
#         print(f"Human disconnected with SID: {sid}")

# @sio.on("chat_from_human")
# async def chat_from_human(sid, data):
#     print(f"Message from human {sid}: {data}")
#     user_id=data['user_id']
#     if user_id in human_connected_users:
#         response={"human_id":data['human_id'],"data":data["data"]}
#         await sio.emit("chat_to_bot", response, to=user_id)
#         print("Response sent")
#     else:
#         print(f"No bot found for SID {sid}")

# @sio.on("chat_to_human")
# async def chat_to_human(sid, data):
#     print(f"Message to human {sid}: {data}")
#     human_id=data['human_id']
#     if human_id in support_humans:
#         response={"user_id":sid,"data":data["data"]}
#         await sio.emit("chat_from_bot", response, to=human_id)
#         print("Response sent")
#     else:
#         print(f"No human found for SID {sid}")

# # temp endpoint for testing
# ba=BA()
# @sio.on("chat")
# async def handle_message(sid, data):
#     res=ba.consult(data)
#     print(res)
#     await sio.emit("response", res, to=sid)

# ==========================================
# gayuni
@sio.on("connect")
async def connect(sid,environ,auth):
    print(f'{sid} : connected')
    await sio.emit('join',{'sid':sid})
    await sio.emit("message", {"data": "Welcome!"}, to=sid)


# ===============only for testing============================
import importlib

gemini=getattr(importlib.import_module('routes.llm'), 'Ggemini')()

def talk_with_moda_gayuni(message):
    rsp=gemini.chatGemini(message)
    return rsp
# ====================================================================
BA=BA()
@sio.on("chat")
async def chat(sid,message):
    await sio.emit('chat',{'sid':sid,'message':message})
    # response = ra.chainquery({"response": message})
    response=talk_with_moda_gayuni(message)
    # response = BA.consult(message)
    if response:
        print(f'Response for message "{message}": {response}')  # Print the response
        await sio.emit('chat_response', {'sid': sid, 'message': response})   

@sio.on("disconnect")
async def disconnect(sid):
    print(f'{sid} : diconnected')

asgi_app = ASGIApp(sio, app)

if __name__ == "__main__":
    pass