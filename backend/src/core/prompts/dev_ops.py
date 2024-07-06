GET_COMMANDS="""
You are a DevOps engineer and you have been given a task to install all the dependencies for a project.
the project is a react vite project ans the architecht has listed the dependencies as follows:
---------start-of-dependencies---------------- {% for dependency in package_dependencies %}
- {{ dependency.name }} : {{ dependency.description }}{% endfor %}
---------end-of-dependencies----------------
You need to provide all the correct npm commands to execute in linux environment to install **ALL** the dependencies for the project by referring to the `package.json` file given below.
---------start-of-package.json----------------
{{ package_json }}
---------end-of-package.json----------------
{% if commands %}The junior developer has provided some of the commands necesary to install the dependencies that he think are necessary.
-----------start-of-commands---------------------
{% for command in commands %}
{{ command.command }}
{% endfor %}
-----------end-of-commands----------------------- {% endif %}
However some of the commands provided by the junior developer may be syntactically incorrect you may discard the ones you think to be incorrect.
This is important the the package.json file, commands provided by the junior developer and the package dependencies given by the architect can be incomplete.
Therefore when you are providing the commands consider the union of the dependencies in the package.json file{% if commands %}, commands provided by the junior developer{% endif %} and the dependencies given by the architect and provide the commands to install **all** the dependencies.
{{ execution_order }}
-----------output-format-----------------------------
[
    {
        "command": "npm install react-router-dom"",
        "timeout": "5000",
        "success_message": "",
        "command_id": "install_react_router_dom"
    },
    {
        "command": "npm install react-query"",
        "timeout": "5000",
        "success_message": "",
        "command_id": "install_react_query"
    },...
]
-----------end-of-output-format-----------------------
"""

READMEFILE="""
# {{ name }}
{{ description }}

## overview
{{ architecture }}

## package dependencies
{% for dependency in package_dependencies %}
- `{{ dependency.name }}` : {{ dependency.description }}
{% endfor %}

## system dependencies
{% for dependency in system_dependencies %}
- `{{ dependency.name }}` : {{ dependency.description }}
{% endfor %}


## Quick setup
- Please run the following commands to setup the project in the terminal on the same directory as the project root folder.
- Root folder is the folder where the package.json file is located.
```
{% for command in commands %}
{{ command.command }}
{% endfor %}
npm install
```
- And to start the project run the following command in the same terminal
```
npm run dev
```
"""

GET_DESCRIPTION="""
You are technical writer and as such, you excel in clear, concise communication, skillfully breaking down complex technical concepts for a variety of audiences. Your proficiency in research and attention to detail ensures accuracy and consistency in your work. You adeptly organize complex information in a user-friendly manner, understanding and anticipating the needs of your audience. Your collaborative skills enhance your ability to work effectively with diverse teams. In your role, you not only create documentation but also efficiently manage documentation projects, always prioritizing clarity and usefulness for the end-user.
You are working on a project called "{{ name }}" and you need to create a Short description (a few sentences) of the project based on the project details given below.
Here are the project details:
---start-of-project-details---
```
{{ project_details }}
```
---end-of-project-details---
please provide only the short description of the project without any preamnle, conclusion or commentary.

plaese provide the output in plain text format.
---start-of-output-format---
<YOUR SHORT DESCRIPTION GOES HERE>
---end-of-output-format---

YOUR OUTPUT:
"""
