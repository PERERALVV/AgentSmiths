IMPLEMENT_CHANGES="""
You are working on a project and your job is to implement new code changes based on given instructions.
Now you have to implement ALL changes that are related to `{{ file_name }}` having the path `{{ file_path }}` described in development instructions listed below.
Make sure you don't make any mistakes, especially ones that could affect rest of project. Your changes will be reviewed by very detailed reviewer. Because of that, it is extremely important that you are STRICTLY following ALL the following rules while implementing changes:

{{ coding_rules }}

You are currently working on this task with the following description:
```
{{ development_tasks[current_task_index]['description'] }}
```

{{ user_feedback }}

Here are development instructions and now you have to focus only on changes in `{{ file_name }}` having the path `{{ file_path }}`:
---start_of_development_instructions---

{{ instructions }}

---end_of_development_instructions---

{% if rework_feedback is defined %}
You previously made changes to file `{{ file_name }}` having the path `{{ file_path }}` but not all changes were accepted, and the reviewer provided feedback on the changes that you must rework:
{{ rework_feedback }}
Please update the file accordingly and output the full new version of the file.

The reviewer accepted some of your changes, and the file now looks like this:
```
{{ file_content }}
```
{% elif file_content %}
Here is how `{{ file_name }}` having the path `{{ file_path }}` looks like currently:
```
{{ file_content }}
```
{% else %}
You need to create a new file `{{ file_name }}` having the path `{{ file_path }}`.
{% endif %}

{{ files_list }}
**IMPORTANT: include only the code in your response no need to specify content type or attach any other preamble**
**IMPORTANT: include only the full contents of the file, without skipping over any content in your response no need to specify content type or pragamming langague or attach any other preamble**
-----------output-format-----------------------------
```<YOUR FULLY FUNCTIONAL CODE GOES HERE>
```
-----------end-of-outputformat-----------------------
YOUR OUTPUT:
"""

CODE_REWORK="""
Your changes have been reviewed.
{% if content != original_content %}
The reviewer approved and applied some of your changes, but requested you rework the others.

Here's the file with the approved changes already applied:
```
{{ content }}
```

Here's the reviewer's feedback:
{% else %}
The reviewer requested that you rework your changes, here's the feedback:
{% endif %}

reason for rework: {{ reason_for_rework }}
review notes: {{ review_notes }}

Based on this feedback and the original instructions, think carefully, make the correct changes, and output the entire file again. Remember, Output ONLY the content for this file, without additional explanation, suggestions or notes. Your output MUST start with ``` and MUST end with ``` and include only the complete file contents.

**IMPORTANT: include only the code in your response no need to specify content type or attach any other preamble**
**IMPORTANT: include only the full contents of the file, without skipping over any content in your response no need to specify content type or pragamming langague or attach any other preamble**
-----------output-format-----------------------------
```<YOUR FULLY FUNCTIONAL CODE GOES HERE>
```
-----------end-of-outputformat-----------------------
YOUR OUTPUT:
"""