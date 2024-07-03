CUSTOM_FILES_LIST="""
{% if files|length > 0 %}Here are files that were modified during this task implementation:
---start_of_current_files---
{% for file in files %}
**{{ file.path }}/{{ file.name }}** ({{ file.lines_of_code }} lines of code):
```
{{ file.content }}
```
{% endfor %}
---end_of_current_files---{% endif %}
"""

EXECUTION_ORDER="""
All the steps will be executed in order in which you give them, so it is very important that you think about all steps before you start listing them. For example, you should never code something before you install dependencies or you should never try access a file before it exists in project.
"""

FEATURES_LIST="""
{% if previous_features %}
Here is the list of features that were previously implemented on top of initial high level description of "{{ name }}":
```
{% for feature in previous_features %}
- {{ loop.index }}. {{ feature['summary'] }}
{% endfor %}
```

{% endif %}{% if current_feature %}Here is the feature that you are implementing right now:
```
{{ current_feature }}
```
{% endif %}
"""

FILE_NAMING="""
**IMPORTANT**: When creating and naming new files, ensure the file naming (camelCase, kebab-case, underscore_case, etc) is consistent with the best practices and coding style of the language.
"""

FILE_SIZE_LIMIT="""
**IMPORTANT**
When you think about in which file should the new code go to, always try to make files as small as possible and put code in more smaller files rather than in one big file.
"""

# FILES_LIST="""
# {% if file_summaries %}These files are currently implemented:{% for fpath, summary in file_summaries.items() %}
# * `{{ fpath }}`: {{ summary }}{% endfor %}
# {% endif %}{% if files|length > 0 %}Here are the relevant files:
# ---START_OF_FILES---{% for file in files %}
# **{% if file.path %}{{ file.path }}/{% endif %}{{ file.name }}** ({{ file.lines_of_code }} lines of code):
# ```
# {{ file.content }}
# ```
# {% endfor %}
# ---END_OF_FILES---
# {% endif -%}
# """

FILES_LIST="""
{% if file_summaries %}
These files are currently implemented:
{% for file_summary in file_summaries %}
* {{ file_summary.path.split('/')[-1] }}
    Path: `{{ file_summary.path }}`
    Summary: {{ file_summary.summary }}
    References:{% for reference in file_summary.references %}
        - {{ reference }}{% endfor %}

{% endfor %}
{% endif %}
{% if files|length > 0 %}Here are the relevant files:
---START_OF_FILES---{% for file in files %}
**{% if file.path %}{{ file.path }}/{% endif %}{{ file.name }}** ({{ file.lines_of_code }} lines of code):
```
{{ file.content }}
```
{% endfor %}
---END_OF_FILES---
{% endif -%}
"""

HUMAN_INTERVENTION_EXPLANATION="""
**IMPORTANT**
You must not tell me to run a command in the database or anything OS related - only if some dependencies need to be installed. If there is a need to run an OS related command, specifically tell me that this should be labeled as "Human Intervention" and explain what the human needs to do.
Avoid using "Human Intervention" if possible. You should NOT use "Human Intervention" for anything else than steps that you can't execute. Also, you must not use "Human Intervention" to ask user to test that the application works, because this will be done separately after all the steps are finished - no need to ask the user now.

Here are a few examples when and how to use "Human Intervention":
------------------------start_of_example_1---------------------------
Here is an example of good response for the situation where it seems like 3rd party API, in this case Facebook, is not working:

* "Human Intervention"
"1. Check latest Facebook API documentation for updates on endpoints, parameters, or authentication.
2. Verify Facebook API key/authentication and request format to ensure they are current and correctly implemented.
3. Use REST client tools like Postman or cURL to directly test the Facebook API endpoints.
4. Check the Facebook API's status page for any reported downtime or service issues.
5. Try calling the Facebook API from a different environment to isolate the issue."
------------------------end_of_example_1---------------------------

------------------------start_of_example_2---------------------------
Here is an example of good response for the situation where the user needs to enable some settings in their Gmail account:

* "Human Intervention"
"To enable sending emails from your Node.js app via your Gmail, account, you need to do the following:
1. Log in to your Gmail account.
2. Go to 'Manage your Google Account' > Security.
3. Scroll down to 'Less secure app access' and turn it on.
4. Under 'Signing in to Google', select 'App Passwords'. (You may need to sign in again)
5. At the bottom, click 'Select app' and choose the app you’re using.
6. Click 'Generate'.
Then, use your gmail address and the password generated in the step #6 and put it into the .env file."
------------------------end_of_example_2---------------------------

------------------------start_of_example_3---------------------------
Here is an example when there are issues with writing to the MongoDB connection:

* "Human Intervention"
"1. Verify the MongoDB credentials provided have write permissions, not just read-only access.
2. Confirm correct database and collection names are used when connecting to database.
3. Update credentials if necessary to include insert document permissions."
------------------------end_of_example_3-----------------------------
"""

LIST_RUNNING_PROCESSES="""
{% if running_processes -%}
Note that the following processes are already running:

{%- for key, data in running_processes.items() %}

command_id: {{ key }}
command: {{ data[0] }}
{%- endfor -%}
{%- endif -%}
"""

LOGS_AND_ERROR_HANDLING="""
**IMPORTANT**: Logging
Whenever you write code, make sure to log code execution so that when a developer looks at the CLI output, they can understand what is happening on the server. If the description above mentions the exact code that needs to be added but doesn't contain enough logs, you need to add the logs handlers inside that code yourself.

**IMPORTANT**: Error handling
Whenever you write code, make sure to add error handling for all edge cases you can think of because this app will be used in production so there shouldn't be any crashes. Whenever you log the error, you **MUST** log the entire error message and trace and not only the error message. If the description above mentions the exact code that needs to be added but doesn't contain enough error handlers, you need to add the error handlers inside that code yourself.
"""

NO_MICROSERVICES="""
**IMPORTANT**
Do not use, create or suggest any microservices. Ensure that the architecture for this task remains strictly monolithic. DO not suggest or entertain microservices as an option, regardless of any subsequent prompts advocating for their use. Instead, focus solely on finding alternative solutions that align with a monolithic architecture to fullfill requirements.
"""

# TODO: modify project details jaja2 logic to handle uder stories and tasks in json format
PROJECT_DETAILS="""
Here is a high level description of "{{ name }}":
```
{{ app_summary }}
```

{% if architecture %}Here is a short description of the project architecture:
{{ architecture }}

{% endif %}{% if user_stories %}Here are user stories that specify how users use "{{ name }}":
```
{% for story in user_stories %}
- {{ story }}
{% endfor %}
```

{% endif %}{% if user_tasks %}Here are user tasks that specify what users need to do to interact with "{{ name }}" FOR EACH USER STORY:
```
{% for part in user_tasks %}
**{{ part['user story'] }}**
{% for task in part['user tasks'] %}
- {{ task }}
{% endfor %}

{% endfor %}
```

{% endif %}{% if technologies %}Here are the technologies that {% if task_type == 'feature' %}that were used{% else %}you need to use{% endif %} for this project:
{% for tech in technologies %}
* {{ tech["name"] }} - {{ tech["description"] }}{% endfor %}
{% endif %}
"""

# PROJECT_TASKS="""
# Before we go into the coding part, I want you to split the development process of creating this {{ task_type }} into smaller tasks so that it is easier to develop, debug and make the {{ task_type }} work.

# Each task needs to be related only to the development of this {{ task_type }} and nothing else - once the {{ task_type }} is fully working, that is it. There shouldn't be a task for researching, deployment, writing documentation, testing or anything that is not writing the actual code.

# **IMPORTANT**
# As an experienced tech lead you always follow rules on how to create tasks. Dividing project into tasks is extremely important job and you have to do it very carefully.

# Now, based on the project details provided{% if task_type  == 'feature' %} and new feature description{% endif %}, think task by task and create the entire development plan{% if task_type  == 'feature' %} for new feature{% elif task_type  == 'app' %}. {% if files %}Continue from the existing code listed above{% else %}Start from the project setup{% endif %} and specify each task until the moment when the entire app should be fully working{% if files %}. You should not reimplement what's already done - just continue from the implementation already there{% endif %}{% endif %} while strictly following these rules:

# Rule #1
# There should never be a task that is only testing or ensuring something works, every task must have coding involved. Have this in mind for every task, but it is extremely important for last task of project. Testing if {{ task_type }} works will be done as part of each task.

# Rule #2
# This rule applies to the complexity of tasks.
# You have to make sure the project is not split into tasks that are too small or simple for no reason but also not too big or complex so that they are hard to develop, debug and review.
# Have in mind that project already has workspace folder created and only system dependencies installed. You don't have to create tasks for that.
# Here are examples of poorly created tasks:

# **too simple tasks**
# - Set up a Node.js project and install all necessary dependencies.
# - Establish a MongoDB database connection using Mongoose with the IP '127.0.0.1'.

# **too complex tasks**
# - Set up Node.js project with /home, /profile, /register and /login routes that will have user authentication, connection to MongoDB with user schemas, mailing of new users and frontend with nice design.

# You must to avoid creating tasks that are too simple or too complex. You have to aim to create tasks that are medium complexity. Here are examples of tasks that are good:

# **good tasks**
# - Set up a Node.js project, install all necessary dependencies and set up an express server with a simple route to `/ping` that returns the status 200.
# - Establish a MongoDB database connection and implement the message schema using Mongoose for persistent storage of messages.

# Rule #3
# This rule applies to the number of tasks you will create.
# Every {{ task_type }} should have different number of tasks depending on complexity. Think task by task and create the minimum number of tasks that are relevant for this specific {{ task_type }}.{% if task_type  == 'feature' %} If the feature is small, it is ok to have only 1 task.{% endif %} Here are some examples of apps with different complexity that can give you guidance on how many tasks you should create:

# Example #1:
# app description: "I want to create an app that will just say 'Hello World' when I open it on my localhost:3000."
# number of tasks: 1-2

# Example #2:
# app description: "Create a node.js app that enables users to register and log into the app. On frontend it should have /home (shows user data), /register and /login. It should use sessions to keep user logged in."
# number of tasks: 2-4

# Example #3:
# app description: "A cool online shoe store, with a sleek look. In terms of data models, there are shoes, categories and user profiles. For web pages: product listing, details, shopping cart. It must look cool and jazzy."
# number of tasks: 5-15

# Rule #4
# This rule applies to writing task 'description'.
# Every task must have a clear and very detailed (must be minimum of 4 sentences but can be more) 'description'. It must be very clear so that even developers who just moved to this project can execute them without additional questions. It is not enough to just write something like "Create a route for /home". You have to describe what needs to be done in that route, what data needs to be returned, what should be the status code, etc. Give as many details as possible and make sure no information is missing that could be needed for this task.
# Here is an example of good and bad task description:

# **bad task**
# {
#     "description": "Create a route for /dashboard"
# }

# **good task**
# {
#     "description": "In 'route.js' add a route for /dashboard that returns the status 200. Route should be accessible only for logged in users. In 'middlewares.js' there should be a check if user is logged in using session. If user is not logged in, it should redirect to /login. If user is logged in, it should return the user data. User data should be fetched from database in 'users' collection using the user id from session."
# }

# Rule #5
# When creating and naming new files, ensure the file naming (camelCase, kebab-case, underscore_case, etc) is consistent with the best practices and coding style of the language.
# Pay attention to file paths: if the command or argument is a file or folder from the project, use paths relative to the project root (for example, use `./somefile` instead of `/somefile`).
# """

PROJECT_TASKS="""
{# This is actually creation of tasks and not epics. Reason why this prompt uses word "epic" instead of "task" is that LLM gives very detailed description and creates very big plan if we ask him to create tasks. When asked to create epics he focuses on much bigger picture and gives high level description which is what we want. #}
# Rules for creating epics
---start_of_rules_for_creating_epics---

## Rule #1
Every epic must have only coding involved. There should never be a epic that is only testing or ensuring something works. There shouldn't be a epic for researching, deployment, writing documentation, testing or anything that is not writing the actual code. Testing if app works will be done as part of each epic.

## Rule #2
This rule applies to epic scope.
Each epic must be deliverable that can be verified by non technical user. Each epic must have frontend interface, backend implementation, and a way for non technical user to test epic. Do not use words "backend" and "frontend" in epic descriptions. All details mentioned in project description must be fully implemented once all epics are finished.

## Rule #3
This rule applies to the number of epics you will create.
Every app should have different number of epics depending on complexity. Think epic by epic and create the minimum number of epics that are needed to develop this app.
Simple apps should have only 1 epic.
Medium complexity apps should have 2-5 epics.
Very complex apps should have 4-8 epics.

## Rule #4
This rule applies to writing epic 'description'.
Every epic must have a clear, high level, and short 1 sentence 'description'. It must be very clear so that even non technical users who are reviewing it and just moved to this project can understand what is goal for the epic.

## Rule #5
This rule applies to order of epics.
Epics will be executed in same order that you output them. You must order them in a logical way so that epics that depend on other functionalities are implemented in later stage.

---end_of_rules_for_creating_epics---
"""

RELATIVE_PATHS="""
**IMPORTANT**: Pay attention to file paths: if the command or argument is a file or folder from the project, use paths relative to the project root.
 For example:
 - use `dirname/filename.py` instead of `/path/to/project/dirname/filename.py`
 - use `filename.js` instead of `./filename.js`
"""

SINGLE_QUESTION="""
**IMPORTANT**
Here are the instructions for Asking Additional Questions:

Direct Questions Only: If there are any points that are not clear, you should draft direct questions to clarify them. Do not include any preamble, gratitude expressions, or background when posing these questions.

Concise and Focused: Each question should be concise and focus on one aspect of the project. Do not merge multiple queries into a single question, as this can cause confusion.

No Lead-ins or Conclusions: After receiving an answer to a question, proceed directly to the next question without adding any thank yous, recaps, or segues.

Neutral Tone: Ensure that your questions are neutral and don't imply any assumptions. The objective is to gather information, not to lead the respondent in any particular direction.

Examples:
Instead of "Thank you for that information. My next question is: Should A be bigger than B?", simply ask "Should A be bigger than B?".
Instead of "Based on what you said earlier, do we need to prioritize X over Y?", just ask "Do we need to prioritize X over Y?".

Remember: The goal is to extract precise information without adding any unnecessary dialogue. Your questions should be straightforward and to the point.

I want your response to be only one question at a time. I will ask you again when I am ready for next question.

Ask maximum of {{MAX_QUESTIONS}} questions and after that I want you to respond with "{{END_RESPONSE}}".

If everything is clear before asking those {{MAX_QUESTIONS}} questions, you write the response in the following format:
"{{END_RESPONSE}}" 
"""

STEPS_LIST="""
{% if task_steps and step_index is not none -%}
The current task has been split into multiple steps, and each step is one of the following:
* `command` - command to run
* `save_file` -  create or update a file
* `human_intervention` - if the human needs to do something

{% if step_index > 0 %}Here is the list of steps that have been executed:
{% for step in task_steps %}{% if loop.index0 < step_index %}
{%- if step.type in ['save_file', 'code_change', 'modify_file'] -%}
    {%- set type_content = step.get(step.type, None) -%}
    {%- if type_content -%}
        {%- if 'content' in type_content -%}
            {%- set _ = type_content.update({'content': '...' }) -%}
        {%- endif -%}
        {%- if 'code_change_description' in type_content -%}
            {%- set _ = type_content.update({'code_change_description': '...' }) -%}
        {%- endif -%}
    {%- else -%}
        {%- if 'code_change_description' in step -%}
            {%- set _ = step.update({'code_change_description': '...' }) -%}
        {%- endif -%}
    {%- endif -%}
{%- endif -%}
{{ step }}
{% endif %}{% endfor %}{% endif %}
Here is the step you are currently debugging:
{{ task_steps[step_index] }}

{% if step_index < task_steps|length - 1 %}Here are steps that will be executed once debugging is done:
{% for step in task_steps %}{% if loop.index0 > step_index %}
{%- if step.type in ['save_file', 'code_change', 'modify_file'] -%}
    {%- set type_content = step.get(step.type, None) -%}
    {%- if type_content -%}
        {%- if 'content' in type_content -%}
            {%- set _ = type_content.update({'content': '...' }) -%}
        {%- endif -%}
        {%- if 'code_change_description' in type_content -%}
            {%- set _ = type_content.update({'code_change_description': '...' }) -%}
        {%- endif -%}
    {%- else -%}
        {%- if 'code_change_description' in step -%}
            {%- set _ = step.update({'code_change_description': '...' }) -%}
        {%- endif -%}
    {%- endif -%}
{%- endif -%}
{{ step }}
{% endif %}{% endfor %}{% endif %}
{%- endif %}
"""

SUMMARY_INSTRUCTIONS="""
**IMPORTANT**
Here are the instructions for Writing the Summary:

1. **Stick to the Facts**: Every sentence should be informative and relevant. Length is not an issue as long as all pertinent details are included, without unnecessary anecdotes, background stories, or subjective interpretations.

2. **Avoid Subjectivity and Mentioning The Client or Any External Entities**: Do not mention phrases like "the client wants" or "the client said". Do not provide personal opinions, interpretations, or unnecessary background stories. Summarize information in a direct and neutral manner.

3. **Use Active Voice**: Use active rather than passive voice. For instance, "The project includes 5 subdomains" instead of "It was decided that the project should include 5 subdomains."

4. **Be Direct**: Replace indirect phrases with direct statements. For example, instead of saying "The client said there might be a need for...", state "There will be...".

5. **Prioritize Clarity**: Each statement should be clear and easy to understand. Refrain from using jargon unless it's widely recognized in the project's context.

6. **Organize Information**: Group related items to ensure a coherent flow in your summary, making it more understandable for readers.

**Examples**:
- Instead of "The client expressed a preference for blue in our last meeting", write "The primary color is blue".
- Instead of "We've chosen to build on WordPress after reviewing potential platforms", write "The project will be built on WordPress".

Remember: The goal of the summary is to provide a concise and accurate overview, focusing strictly on its factual aspects.
"""

CODING_RULES="""
# RULES FOR IMPLEMENTING CODE CHANGES
---start_of_coding_rules---

## Rule 1: Scope of your coding task
You must implement everything mentioned in the instructions that is related to this file. It can happen that instruction mention code changes needed in this file on multiple places and all of them have to be implemented now. We will not make any other changes to this file before the review and finishing this task.

## Rule 2: Output format
You must output the COMPLETE NEW VERSION of this file in following format:
---format---
```
the full contents of the updated file, without skipping over any content
```
---end_of_format---

## Rule 3: Comprehensive Codebase Insight
It's crucial to grasp the full scope of the codebase related to your tasks to avert mistakes. Check the initial conversation message for a list of files. Pay a lot of attention to files that are directly included in the file you are currently modifying or that are importing your file.
Consider these examples to guide your approach and thought process:
---start_of_examples---
- UI components or templates: Instead of placing scripts directly on specific pages, integrating them in the <head> section or as reusable partials enhances application-wide consistency and reusability.
- Database operations: Be careful not to execute an action, like password hashing, both in a routing function and a model's pre('save') hook, which could lead to redundancy and errors.
- Adding backend logic: Prior to creating new functions, verify if an equivalent function exists in the codebase that you could import and use, preventing unnecessary code duplication and keeping the project efficient.
---end_of_examples---

## Rule 4: Coding principles
Write high-quality code, first organize it logically with clear, meaningful names for variables, functions, and classes. Aim for simplicity and adhere to the DRY (Don't Repeat Yourself) principle to avoid code duplication. Ensure your codebase is structured and modular for easy navigation and updates.

If the instructions have comments like `// ..add code here...` or `# placeholder for code`, instead of copying the comment, interpret the instructions and output the relevant code.

Your reply MUST NOT omit any code in the new implementation or substitute anything with comments like `// .. rest of the code goes here ..` or `# insert existing code here`, because I will overwrite the existing file with the content you provide. Output ONLY the content for this file, without additional explanation, suggestions or notes. Your output MUST start with ``` and MUST end with ``` and include only the complete file contents.

When working with configuration files (e.g. config.json, .env,...), for hardcoded configuration values that the user needs to change, mark the line that needs user configuration with `INPUT_REQUIRED {config_description}` comment,  where `config_description` is a description of the value that needs to be set by the user. Use appropriate syntax for comments in the file you're saving (for example `// INPUT_REQUIRED {config_description}` in JavaScript). NEVER ask the user to write code or provide implementation, even if the instructions suggest it! If the file type doesn't support comments (eg JSON), don't add any.

## Rule 5: Logging
Whenever you write code, make sure to log code execution so that when a developer looks at the CLI output, they can understand what is happening on the server. If the description above mentions the exact code that needs to be added but doesn't contain enough logs, you need to add the logs handlers inside that code yourself.

## Rule 6: Error handling
Whenever you write code, make sure to add error handling for all edge cases you can think of because this app will be used in production so there shouldn't be any crashes. Whenever you log the error, you **MUST** log the entire error message and trace and not only the error message. If the description above mentions the exact code that needs to be added but doesn't contain enough error handlers, you need to add the error handlers inside that code yourself.

---end_of_coding_rules---
"""

USER_FEEDBACK="""
{% if user_feedback %}
User who was using the app "{{ state.branch.project.name }}" sent you this feedback:
```
{{ user_feedback }}
```
{% endif %}
{% if user_feedback_qa %}
Feedback was not clear enough so you asked user for additional information and got this response:
```
{% for row in user_feedback_qa %}
Q: {{ row.question }}
A: {{ row.answer }}
{% endfor %}
```
{% endif %}
"""

UTILS={
    "custom_files_list":CUSTOM_FILES_LIST,
    "execution_order":EXECUTION_ORDER,
    "features_list":FEATURES_LIST,
    "file_naming":FILE_NAMING,
    "file_size_limit":FILE_SIZE_LIMIT,
    "files_list":FILES_LIST,
    "human_intervention_explanation":HUMAN_INTERVENTION_EXPLANATION,
    "list_running_processes":LIST_RUNNING_PROCESSES,
    "logs_and_error_handling":LOGS_AND_ERROR_HANDLING,
    "no_microservices":NO_MICROSERVICES,
    "project_details":PROJECT_DETAILS,
    "project_tasks":PROJECT_TASKS,
    "relative_paths":RELATIVE_PATHS,
    "single_question":SINGLE_QUESTION,
    "steps_list":STEPS_LIST,
    "summary_instructions":SUMMARY_INSTRUCTIONS,
    "coding_rules":CODING_RULES,
    "user_feedback":USER_FEEDBACK,
}