CODE_FILES="""
You are working on a project and your job is to implement new code changes based on given instructions.
Your project is a STATIC WEBSITE which only include HTML, CSS, and JavaScript code.
the project will only contain HTML files with CSS inside style tags and JavaScript inside script tags.
The Tech Lead has given you the name and description of the pages that should be included in the website.
Each page of the WEBSITE will have their own HTML file and all of the code for that page will be contained in that file.
All the files of the project will be stored in the same directory.
{% if file_names %}
These are the file names of the files that will be present in the final project:{% for file_name in file_names %}
- {{ file_name }}{% endfor %}
**This is IMPORTANT pay special attention ro the file names given above when you are writing code to link pages using paths**{% endif %}
{%if pages|length > 0 %}
The WEBSITE will have the following pages:
{% for page in pages %}
* {{ page.page_name}}{% endfor %}
{% endif %}
You now have to implement the `{{ file_name }}` page according to the description of the page given below.
`{{ description }}`

{% if files|length > 0 %}
Here are the files that are already present in the project:
---START_OF_FILES---{% for file in files %}
**{% if file.path %}{{ file.path }}/{% endif %}{{ file.name }}** ({{ file.lines_of_code }} lines of code):
```
{{ file.content }}
```
{% endfor %}
---END_OF_FILES---
{% endif %}

**IMPORTANT: include only the code in your response no need to specify content type or attach any other preamble**
-----------output-format-----------------------------
<YOUR FULLY FUNCTIONAL CODE GOES HERE>
-----------end-of-outputformat-----------------------
YOUR OUTPUT:
"""

GOAL="""
You are a world class full stack software developer.
You write modular, clean, maintainable, production-ready code.
Your job is to implement tasks assigned by your tech lead.
"""


import importlib
import os
Action= getattr(importlib.import_module('core.actions.Action'), 'Action')
render_template_with_data = getattr(importlib.import_module('utils.PromptFormat'), 'render_template_with_data')
GET_MULTILEVEL_DIRECTORY_CONTENTS=getattr(importlib.import_module('utils.file_handling'), 'get_multilevel_directory_contents')
UPDATE_FILE=getattr(importlib.import_module('utils.file_handling'), 'update_file')
LOG = getattr(importlib.import_module('core.logger'), 'log')

class code_files(Action):

    name:str = "code_files"
    return_json: bool = False
    goal: str = GOAL


    def __init__(self):
        super().__init__()

    async def run(self,WEBSITE):
        for page in WEBSITE.dev_plan:
            # files=GET_MULTILEVEL_DIRECTORY_CONTENTS(WEBSITE.root_path)
            # LOG.info(files)
            data={
                "file_name":page['page_name'],
                "description":page['description'],
                # "files":files
                "file_names":WEBSITE.file_names
            }
            msg=render_template_with_data(CODE_FILES, data)
            # LOG.info(msg)
            rsp=await self.ask(msg)
            try:
                rsp=self.parse_html(rsp)
            except:
                try:
                    rsp=self.parse_std_resp(rsp)
                except Exception as e:
                    LOG.info(f"an error occjured while parsing{e}")
                    LOG.info(rsp)
                    pass
            # LOG.info(rsp)
            path=os.path.join(WEBSITE.root_path,page['page_name'])
            if not UPDATE_FILE(path,rsp,WEBSITE):
                LOG.info('ERROR!!!!!! File not updated')
        return WEBSITE