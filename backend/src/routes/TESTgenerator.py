# import asyncio
# from socketio import AsyncServer

# from .api import sio
# from .api import user_responses

# async def generate_code(bot_response:str,user_sid:str)->str:
#     if user_sid not in user_responses:
#         user_responses[user_sid] = asyncio.Queue()
#     await sio.emit('message_exchange', {'sid': user_sid, 'message': bot_response})

#     # Wait for the response and take the last element from the queue
#     user_response = await user_responses[user_sid].get()
#     print(f'The generate_code function received the message : {user_response}')
#     return user_response