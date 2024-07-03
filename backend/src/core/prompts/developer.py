IMPLEMENT_TASK="""
You are working on a {{ app_type }} called "{{ name }}" and you need to write code for the entire {{ task_type }} based on the tasks that the tech lead gives you. So that you understand better what you're working on, you're given other specs for "{{ name }}" as well.

{{ project_details }}
{{ features_list }}
{{ files_list }}

We've broken the development of this {{ task_type }} down to these tasks:
```{% for task in development_tasks %}
{{ loop.index }}. {{ task['description'] }}
{% endfor %}
```

You are currently working on task #{{ current_task_index + 1 }} with the following description:
```
{{ development_tasks[current_task_index]['description'] }}
```
{% if current_task_index != 0 %}All previous tasks are finished and you don't have to work on them.{% endif %}

Now, tell me all the code that needs to be written to implement ONLY this task and have it fully working and all commands that need to be run to implement this task.

**IMPORTANT**
{%- if task_type == 'app' %}
Remember, I created an empty folder where I will start writing files that you tell me and that are needed for this app.
{% endif %}
{{ relative_paths }}
DO NOT specify commands to create any folders or files, they will be created automatically - just specify the relative path to each file that needs to be written.

{{ file_naming }}

{{ execution_order }}

{{ human_intervention_explanation }}

{{ file_size_limit }}

{% if ports %}
Never use the ports {{ ports }} to run the app, it's reserved.
{% endif %}
"""

FILTER_FILES="""
You are working on a {{ app_type }} called "{{ name }}", writing the code for the entire application.

Here is a high level description of "{{ name }}":
```
{{ app_summary }}
```
{{ features_list }}

{% if development_tasks and current_task %}
Development process of this app was split into smaller tasks. Here is the list of all tasks:
```{% for task in development_tasks %}
{{ loop.index }}. {{ task['description'] }}
{% endfor %}
```
You are currently working on task "{{ current_task.description }}" and you have to focus only on that task.
{% endif %}
A part of the app is already finished.

The app currently contains the following files:
{% if file_summaries %}
{% for file_summary in file_summaries %}
* {{ file_summary.path.split('/')[-1] }}
    Path: `{{ file_summary.path }}`
    Summary: {{ file_summary.summary }}
    References:{% for reference in file_summary.references %}
        - {{ reference }}{% endfor %}
{% endfor %}{% endif %}
{# {% if user_feedback %}
User who was using the app "{{ name }}" sent you this feedback:
```
{{ user_feedback }}
```
{% endif %} #}
{% if next_solution_to_try %}
Focus on solving this issue in the following way:
```
{{ next_solution_to_try }}
```
{% endif %}
Now, before you can work on this, you need to select which files from the above list are relevant to this task. Output the relevant files in a JSON list.
{% if directory_tree %}
Here is the DIRECTORY STRUCTURE of the app:
```
{{ directory_tree }}
```
{% endif %}
**THIS IS IMPORTANT MAKE SURE WHEN YOU ARE ONLY CHOOSING A PATH FROM THE GIVEN PATHS AS IT IS IN THE DIRECTORY STRUCTURE.DO NOT CHANGE ANY PATHS,THE PATHS YOU CHOOSE SHOULD BE EXACTLY SAME AS IT IS IN THE DIRECTORY STRUCTURE**
{{ relative_paths }}

"""

PARSE_TASK="""
Ok, now, take your previous message that starts with `{{ instructions_prefix }}` and ends with `{{ instructions_postfix }}` and convert it to a list of actionable steps that will be executed by a machine. Analyze the entire message, think step by step and make sure that you don't omit any information when converting this message to steps.

Each step can be either:

* `command` - command to run (must be able to run on a {{ os }} machine, assume current working directory is project root folder)
* `save_file` - create or update ONE file
* `human_intervention` - if you need the human to do something, use this type of step and explain in details what you want the human to do. NEVER use `human_intervention` for testing, as testing will be done separately by a dedicated QA after all the steps are done. Also you MUST NOT use `human_intervention` to ask the human to write or review code.

**IMPORTANT**: In `code_change_description` field of `save_file` step, you must provide empty string. If multiple changes are required for same file, you must provide single `save_file` step for each file.

{{ file_naming }}

{{ relative_paths }}

{{ execution_order }}

{{ human_intervention_explanation }}

**IMPORTANT**: Remember, NEVER output human intervention steps to do manual tests or coding tasks, even if the previous message asks for it! The testing will be done *after* these steps and you MUST NOT include testing in these steps.

Examples:
------------------------example_1---------------------------
```
{
  "tasks": [
    {
      "type": "save_file",
      "save_file": {
        "path": "./server.js",
        "code_change_description": "",
      },
    },
    {
      "type": "command",
      "command": {
        "command": "mv ./index.js ./public/index.js"",
        "timeout": "5000",
        "success_message": "",
        "command_id": "move_index_file"
      }
    }
  ]
}
```
------------------------end_of_example_1---------------------------
"""

