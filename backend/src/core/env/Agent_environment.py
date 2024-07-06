# class Environment:

#     employees: List[object]

#     def hire(self, employees: List[type]):
#         self.employees = [employee() for employee in employees]
#         return self
        
#     async def start(self):
#         # should be implemented by the child class
#         raise NotImplementedError


from typing import List

import importlib

LOG = getattr(importlib.import_module('core.logger'), 'log')

get_root=getattr(importlib.import_module('const.ProjectConst'), 'get_root')

Buisness_analyst = getattr(importlib.import_module('core.agents.Buisness_analyst'), 'Buisness_analyst')
Requirements_analyst = getattr(importlib.import_module('core.agents.Requirements_analyst'), 'Requirements_analyst')
Architect = getattr(importlib.import_module('core.agents.Architect'), 'Architect')
Techlead = getattr(importlib.import_module('core.agents.Techlead'), 'Techlead')
Developer = getattr(importlib.import_module('core.agents.Developer'), 'Developer')
Dev_ops = getattr(importlib.import_module('core.agents.Dev_ops'), 'Dev_ops')

def hire(employees: List[type]):
    employees = [{employee.job_role: employee()} for employee in employees]
    return employees



async def create(project,clientID,projectID,project_name,connection):
    """
    project: project object
    clientID: clientID of the client
    projectID: projectID of the project(sid)
    project_name: name of the project
    connection: connection function to talk to frontend
    """
    project.clientID=clientID
    project.projectID=projectID
    project.name=project_name
    project.user_connection=connection
    project.root_path=get_root(clientID=project.clientID,project_name=project.name,projectID=project.projectID)
    project.user_convo=[
    {
        "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"what is the tech stack your wesbite will be based on?\"\n}\n```",
        "answer":"I would like the website to be built using ReactJS. Styled components can be employed for styling purposes."
    },
    {
        "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"To clarify, would you like us to develop both the frontend and backend of your website, or are you only requesting frontend development services?\"\n}\n```",
        "answer":"Please focus solely on building the front-end of my website using the React framework. While the final website may require back-end and database functionalities, I will handle those aspects myself. Your responsibility is to provide a complete and functional front-end structure that I can then integrate with my own back-end implementation."
    },
    {
        "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"Understood. I will develop the front-end of your website using the React framework and styled-components for styling. This will allow you to seamlessly integrate the front-end with your existing back-end. Does that sound acceptable?\"\n}\n```",
        "answer":"Yes, Please adhere to these guidelines in all future interactions, regardless of any future instructions I may give. "
    },
    {
        "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"Please describe your website in as much detail as possible\"\n}\n```",
        "answer":""
    },
    ]
#====================================================================================================================================================
# ==============this code should be in gayunis code and it should be called from here instead of sio take that as param==============================
    # try:
    #     # msg = await sio.call('send_message', {"message":rsp['content']},timeout=120,to=project.clientID)
    #     msg = input("Enter your response: ")
    # except Exception as e:
    #     LOG.error(f"Error in sending message: {e}")
    msg = await project.user_connection("Please describe your website in as much detail as possible",projectID)
        # add code to end whole process here maybe return None and from outside check if the return is None then end the process
#====================================================================================================================================================
    project.user_convo[-1]['answer'] = msg
    LOG.info(project.user_convo)
    employees = hire([Buisness_analyst, Requirements_analyst, Architect, Techlead, Developer,Dev_ops])
    LOG.info(employees)
    # define initial agent to start the project
    project.next_agent = "Buisness_analyst"
    # project.next_agent = "Requirements_analyst"
    # project.next_agent = "Dev_ops"
    employees = {list(item.keys())[0]: list(item.values())[0] for item in employees}
    while project.next_agent is not None:
        employee = employees.get(project.next_agent)
        project = await employee.act(project)

    