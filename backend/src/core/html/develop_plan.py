DEV_PLAN="""
You are working in a software development agency and a project manager approach you telling you that you're assigned to work on a new project. You are working on a WEBSITE called "{{ name }}" and you need to create a detailed development plan so that developers can start developing the app.

The WEBSITE your building is a static website and should be implemented using HTML, CSS, and JavaScript.
THE CODE for a specific page should be contained in a single HTML file haing CSS inside styles tag and JavaScript inside script tag.
The project manager have gathered the name and decriptions of the pages that should be included in the website.

The names and the descriptions of the pages are:
{% for page in pages %}
------------------------------------{{ page.name }}------------------------------------
{{ page.description }}
{%if page.linked_pages %}{{ page.linked_pages }}{% endif %}
---------------------------------------------------------------------------------------
{% endfor %}

You should create a development task for each page containing page name and complete description about the page.
A team of AI developers will be responsible for building the website. Each developer will be assigned a specific page to create and implement. 
Each developer will only have access to the page name and description for the specific page they are working on. They will not be able to see the page names or descriptions for other pages. 
So make sure you include all necessary details for each page independantly so that the AI developer will be able to develop that particular page independantly.
remeber each developer will only have access to the page_name and the description for their page in the development plan you create and will create their page soley based on the description you provide for that page
so make sure to include all the information necessary to independantly implement a page, in the description of that page, otherwise the developers will not be able to implement the pages correctly.

-----------output-format-----------------------------
[
    {
        "page_name": "<file name of the 1st page with extention>",
        "description": "<description of the 1st page>"
    },
    {
        "page_name": "<file name of the 2nd page with extention>",
        "description": "<description of the 2nd page>"
    },......
]
-----------end-of-outputformat-----------------------
"""

DEV_PLAN_CALL={
    'function_declarations': [{
        'name': 'define_pages',
        'description': 'Define a list of pages with their file names and descriptions.',
        'parameters': {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "page_name": {
                        "type": "STRING",
                        "description": "Page file name with extension."
                    },
                    "description": {
                        "type": "STRING",
                        "description": "Description of the page."
                    }
                },
                "required": ["page_name", "description"]
            },
            "description": "List of pages with their names and descriptions."
        }
    }]
}

GOAL="""
You are an experienced tech lead in a software development agency and your main task is to break down the project into smaller tasks that developers will do. You must specify each task as clear as possible. Each task must have a description of what needs to be implemented.
"""

import json

import importlib
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')

LOG = getattr(importlib.import_module('core.logger'), 'log')

class develop_plan(Action):

    name:str = "develop_plan"
    return_json: bool = False
    goal: str = GOAL
    function_calls = DEV_PLAN_CALL

    def __init__(self):
        super().__init__()

    async def run(self,WEBSITE):
        
        data={
            "name":"Restaurant Website",
            "pages":WEBSITE.pages
        }
        msg=render_template_with_data(DEV_PLAN, data)
        # LOG.info(msg)
        rsp=await self.ask(msg)
        rsp=self.parse_json(rsp)
        LOG.info(json.dumps(rsp,indent=4))
        WEBSITE.dev_plan=rsp
        return WEBSITE

