import importlib
import asyncio
# print(build_directory_tree('/code/backend/src/core'))
# print(json.dumps(get_multilevel_directory_contents('/code/backend/workspace/6546465465616515362/hondahitha hotels'),indent=4))
# print(get_multilevel_directory_contents('/code/backend/src/core'))

# from const.ProjectConst import get_root
# import os
# print(get_root('clientID2',"homda")) # ../workspace/clientID
# os.makedirs(get_root('clientID2',"homda"), exist_ok=True) # creates ../workspace/clientID

# summarize_files=getattr(importlib.import_module('core.actions.temp_action'), 'summarize_files')()

# async def main():
#     result=await summarize_files.run('/code/backend/src/core/templates/tpl/javascript_react')
#     with open('result.py', 'w') as file:
#         file.write('files = ' + repr(result) + '\n')

# asyncio.run(main())

# import asyncio
# import importlib
# import json

# LOG = getattr(importlib.import_module('core.logger'), 'log')

# async def main():
#     # Example JSON object
#     data = {
#         "name": "GitHub Copilot",
#         "type": "AI Assistant",
#         "features": ["Code completion", "Documentation lookup", "Error fixing"]
#     }
#     # Convert JSON object to a string and log it
#     LOG.info(json.dumps(data, indent=4))
#     LOG.info('This is a test message')
#     LOG.log_json(data)
# asyncio.run(main())

LOG = getattr(importlib.import_module('core.logger'), 'log')
start=getattr(importlib.import_module('core.html.process'), 'start')
WEBSITE= getattr(importlib.import_module('models.website'), 'WEBSITE')
WEBSITE=WEBSITE()
WEBSITE.name="Suhada Bakers"
WEBSITE.user_id="clientID2"
WEBSITE.project_id="846644646"


WEBSITE.pages=[
    {
        "page_name": "Home",
        "description": "Welcome to Suhada Bakers! Our website showcases our delectable pastries, cakes, and breads, along with information about our bakery, our story, and our commitment to using fresh, high-quality ingredients. You can also view our menu, place orders online, and find our location and contact details.",
        "linked_pages": "About Us, Menu, Gallery, Order Online, Contact Us"
    },
    {
        "page_name": "About Us",
        "description": "Discover the story behind Suhada Bakers. Learn about our passion for baking, our dedication to using local and sustainable ingredients, and our mission to create joyful experiences through delicious treats.",
        "linked_pages": "Home, Menu, Gallery"
    },
    {
        "page_name": "Menu",
        "description": "Explore our extensive menu of baked goods, including classic pastries, elegant cakes, savory breads, and seasonal specialties. Each item is handcrafted with love and care, using only the finest ingredients. You'll find detailed descriptions, images, and pricing for each item.",
        "linked_pages": "Home, About Us, Order Online"
    },
    {
        "page_name": "Gallery",
        "description": "Browse through our gallery showcasing our visually stunning baked goods. You'll find images of our cakes, pastries, breads, and other creations, all crafted with meticulous attention to detail and artistry.",
        "linked_pages": "Home, About Us, Menu"
    },
    {
        "page_name": "Order Online",
        "description": "Conveniently place your orders online for pick-up or delivery. Choose from our menu, customize your order, and provide your details for a smooth and enjoyable online ordering experience.",
        "linked_pages": "Home, Menu, Contact Us"
    },
    {
        "page_name": "Contact Us",
        "description": "Get in touch with us! You can find our location, phone number, and email address here. We're always happy to answer your questions, take special orders, or provide information about our bakery.",
        "linked_pages": "Home, Order Online"
    },
    {
        "page_name": "Blog",
        "description": "Stay up-to-date with the latest news from Suhada Bakers. We'll be sharing baking tips, seasonal recipes, special promotions, and behind-the-scenes glimpses into our bakery.",
        "linked_pages": "Home"
    }
]

# develop_plan=getattr(importlib.import_module('core.html.develop_plan'), 'develop_plan')()
# code_files=getattr(importlib.import_module('core.html.code_files'), 'code_files')
# import copy

# async def start(WEBSITE):
#     result = await develop_plan.run(WEBSITE)
#     result.file_names=[item['page_name'] for item in result.dev_plan]
#     LOG.info(result.file_names)
#     # tasks=[]
#     for i in range(0, len(WEBSITE.dev_plan), 2):
#         website=copy.deepcopy(result)
#         # website.pages = WEBSITE.pages[i:i+2]
#         website.dev_plan = WEBSITE.dev_plan[i:i+2]
#         await code_files().run(website)
#         # task=code_files()
#         # tasks.append(task.run(website))
#     # LOG.info(tasks)
#     # await asyncio.gather(*tasks)
#     # result = await code_files.run(result)

# # asyncio.run(main())

# # async def create_html():
# #     loop = asyncio.get_event_loop()
# #     loop.run_until_complete(await start())

# d=getattr(importlib.import_module('core.env.Agent_environment'), 'create')
asyncio.run(start(WEBSITE))