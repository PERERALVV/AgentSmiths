PLANDEV="""
You are working in a software development agency and a project manager and software architect approach you telling you that you're assigned to work on a new project.
You are working on an app called "{{ name }}" and you need to create a detailed development plan so that developers can start developing the app.

{{ project_details }}
{{ features_list }}
{% if files %}
The developers have already used a project scaffolding tool that creates the initial boilerplate for the project:
{{ existing_summary }}
{{ files_list }}
{% endif %}
Before we go into the coding part, your job is to split the development process of creating this app into smaller epics.
Now, based on the project details provided, think epic by epic and create the entire development plan.{% if files %}Continue from the existing code listed above{% else %}Start from the project setup{% endif %} and specify each epic until the moment when the entire app should be fully working{% if files %}. You should not reimplement what's already done - just continue from the implementation already there{% endif %} while strictly following these rules:

{{ project_tasks }}
-----------output-format-----------------------------
{
  "plan": [<epic1>, <epic2>, ...],
  "status": "todo",
}
-----------end-of-outputformat-----------------------
YOUR RESPONSE:
"""

# PLANDEV="""
# You are working in a software development agency and a project manager and software architect approach you telling you that you're assigned to work on a new project. You are working on a {{ app_type }} called "{{ name }}" and you need to create a detailed development plan so that developers can start developing the app.

# {{ project_details }}
# {{ features_list }}
# {% if files %}The developers have already used a project scaffolding tool that creates the initial boilerplate for the project:
# {{ existing_summary }}

# {{ files_list }}{% endif %}
# **This is important: if your using any paths to existing files given above in your development plan always choose from the above paths and use the given paths as it is** 
# {{ project_tasks }}

# -----------output-format-----------------------------
# {
#   "plan": [<task1>, <task2>, ...],
#   "status": "todo",
# }
# -----------end-of-outputformat-----------------------
# YOUR RESPONSE:
# """
