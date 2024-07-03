USERSTORIES="""I want you to create WEBSITE called "{{ name }}") that can be described as follows:
```
{{ BaSpec }}
```

Think step by step about the description for the WEBSITE "{{ name }}" and the provided questions and answers and create a list of all user stories. A user story is a description of how a user can interact with the WEBSITE. For example, if an app's description is `Create a script that finds Youtube channels with the word "test" inside the channel name`, user stories could be:
- `user runs the script from the CLI`
- `user gets the list of returned channels in a CSV file`

IMPORTANT:
-your output should be in json format
- only return the user stories

-----------output-format-----------------------------
["user story 1","user story 2",...]
-----------end-of-outputformat-----------------------
YOUR RESPONSE:
"""

USERTASKS="""
you are provided with the following user stories:
{{ userStories }}

Break each user story you created into user tasks that a user needs to do to interact with the WEBSITE.

For example, if the user story is `user login to account`, the user tasks could be:
- `user enters username`
- `user enters password`
- `user clicks on login button`



IMPORTANT:
-your output should be in json format
- only return the user tasks

-----------output-format-----------------------------
[
    {
    "user story": "<user story 1>",
    "user tasks": [<user task 1>, <user task 2>, ...],
    },
    {"user story": "<user story 2>",
    "user tasks": [<user task 1>, <user task 2>, ...],
    },
    ...
]
-----------end-of-outputformat-----------------------
YOUR RESPONSE:"""