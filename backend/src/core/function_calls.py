ARCHITECTURE = {
    'function_declarations': [
        {
            'name': 'process_architecture',
            'description': "Get architecture and the list of system dependencies required for the project.",
            'parameters': {
                'type_': 'OBJECT',
                "properties": {
                    "architecture": {
                        "type_": "STRING",
                        "description": "General description of the app architecture.",
                    },
                    "system_dependencies": {
                        "type_": "ARRAY",
                        "description": "List of system dependencies required to build and run the app.",
                        "items": {
                            "type_": "OBJECT",
                            "properties": {
                                "name": {
                                    "type_": "STRING",
                                    "description": "Name of the system dependency, for example Node.js or Python."
                                },
                                "description": {
                                    "type_": "STRING",
                                    "description": "One-line description of the dependency.",
                                },
                                "test": {
                                    "type_": "STRING",
                                    "description": "Command line to test whether the dependency is available on the system.",
                                },
                                "required_locally": {
                                    "type_": "BOOLEAN",
                                    "description": "Whether this dependency must be installed locally (as opposed to connecting to cloud or other server)",
                                }
                            },
                            "required": ["name", "description", "test", "required_locally"],
                        },
                    },
                    "package_dependencies": {
                        "type_": "ARRAY",
                        "description": "List of framework/language-specific packages used by the app.",
                        "items": {
                            "type_": "OBJECT",
                            "properties": {
                                "name": {
                                    "type_": "STRING",
                                    "description": "Name of the package dependency, for example Express or React."
                                },
                                "description": {
                                    "type_": "STRING",
                                    "description": "One-line description of the dependency.",
                                }
                            },
                            "required": ["name", "description"],
                        },
                    },
                    'template': {
                        'type_': 'STRING',
                        'description': 'One of the available project templates.',
                    },
                },
                "required": ["architecture", "system_dependencies", "package_dependencies"],
            },
        },
    ]
}

DEVELOPMENT_PLAN = {
    'function_declarations': [{
        'name': 'implement_development_plan',
        'description': 'Implements the development plan.',
        'parameters': {
            'type_': 'OBJECT',
            "properties": {
                "plan": {
                    "type_": "ARRAY",
                    "description": 'List of development tasks that need to be done to implement the entire plan.',
                    "items": {
                        "type_": "OBJECT",
                        'description': 'Development task that needs to be done to implement the entire plan. It contains all details that developer who is not familiar with project needs to know to implement the task.',
                        'properties': {
                            'description': {
                                'type_': 'STRING',
                                'description': 'Very detailed description of the development task that needs to be done to implement the entire plan.',
                            }
                        },
                        'required': ['description'],
                    },
                },
            },
            "required": ['plan'],
        },
    }]
}

LIST_RELEVANT_FILES = {
    'function_declarations': [{
        'name': 'list_relevant_files',
        'description': 'List of relevant files for the current task.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "relevant_files": {
                    "type": "ARRAY",
                    "items": {
                        "type": "STRING",
                        "description": "Path to the file that is relevant for the current task, relative to the project root."
                    },
                }
            },
            "required": ["relevant_files"],
        }
    }]
}

SUMMARIZE_FILES = {
    'function_declarations': [{
        'name': 'describe_file',
        'description': 'Describe the content of the file.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "summary": {
                    "type": "STRING",
                    "description": "Describe in detail the functionality being defined or implemented in this file. Be as detailed as possible."
                },
                "references": {
                    "type": "ARRAY",
                    "items": {
                        "type": "STRING",
                        "description": "Path to a file that is referenced in the current file, relative to the project root.",
                    },
                    "description": "List of file references."
                }
            },
            "required": ["summary", "references"],
        }
    }]
}

PARSE_TASK = {
  'function_declarations': [
    {
      'name': 'save_file',
      'description': 'Saves a file to the specified path.',
      'parameters': {
        "type": "OBJECT",
        "properties": {
          "path": {
            "type": "STRING",
            "description": "Path to the file relative to the project root.",
          },
          "code_change_description": {
            "type": "STRING",
            "description": "Optional description of the code change made to the file."
          }
        },
        "required": ["path"],
      }
    },
    {
      'name': 'command',
      'description': 'Executes a command.',
      'parameters': {
        "type": "OBJECT",
        "properties": {
          "command": {
            "type": "STRING",
            "description": "Command to execute."
          },
          "timeout": {
            "type": "INTEGER",
            "description": "Maximum time in milliseconds to allow the command to run before timing out. Default is 5000 milliseconds (5 seconds)."
          },
          "success_message": {
            "type": "STRING",
            "description": "Message to display if the command succeeds."
          },
          "command_id": {
            "type": "STRING",
            "description": "Optional identifier for the command."
          }
        },
        "required": ["command"],
      }
    },
    {
        'name': 'human_intervention',
        'description': 'Requires human intervention to complete the development step.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "human_intervention_description": {
                "type": "STRING",
                "description": "A very clear description of the step requiring human intervention."
                }
            },
        "required": ["human_intervention_description"]
        }
    }
  ]
}

REVIEW_CHANGES = {
    'function_declarations': [{
        'name': 'summarize_review',
        'description': 'Summarize the review feedback.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "hunks": {
                    "type": "ARRAY",
                    "items": {
                        "type": "OBJECT",
                        "properties": {
                            "number": {
                                "type": "INTEGER",
                                "description": "Number of the hunk in the pull request."
                            },
                            "reason": {
                                "type": "STRING",
                                "description": "Reason for applying or ignoring this hunk, or for asking for it to be reworked."
                            },
                            "decision": {
                                "type": "STRING",
                                "description": "Decision for the hunk. Can be 'Apply', 'Ignore', or 'Rework'."
                            }
                        },
                        "required": ["number", "reason", "decision"]
                    },
                    "description": "List of hunks with their decisions and reasons."
                },
                "review_notes": {
                    "type": "STRING",
                    "description": "Additional review notes."
                }
            },
            "required": ["hunks"]
        }
    }]
}

ASK_QUESTIONS={
    'function_declarations': [{
        'name': 'process_question_or_specification',
        'description': 'Processes a question or specification.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "state": {
                    "type": "STRING",
                    "description": "Indicates whether the content is a 'Question' or 'Specification'."
                },
                "content": {
                    "type": "STRING",
                    "description": "The content of the question or specification."
                }
            },
            "required": ["state", "content"]
        }
    }]
}

REVIEW_SPEC={
    'function_declarations': [{
        'name': 'summarize_review',
        'description': 'Summarize the review feedback.',
        'parameters': {
            "type": "OBJECT",
            "properties": {
                "type": {
                    "type": "STRING",
                    "description": "Type of review feedback. Can be 'MISSING-INFORMATION' or 'APPROVE'."
                },
                "content": {
                    "type": "STRING",
                    "description": "The information that is missing or the approval message."
                }
            },
            "required": ["type", "content"]
        }
    }]
}

USER_TASKS = {
    'function_declarations': [{
        'name': 'implement_user_stories',
        'description': 'Implements the user stories.',
        'parameters': {
            'type_': 'ARRAY',
            "description": 'List of user stories to implement',
            "items": {
                "type_": "OBJECT",
                'description': 'User story that needs to be implemented.',
                'properties': {
                    'user_story': {
                        'type_': 'STRING',
                        'description': 'Detailed description of the user story that needs to be implemented.',
                    },
                    'user_tasks': {
                        "type_": "ARRAY",
                        "description": 'List of user tasks that needs to be done to implement the user story.',
                        "items": {
                            "type_": "STRING",
                            'description': 'User task that needs to be done to implement the user story.',
                        },
                    },
                },
                'required': ['user_story', 'user_tasks'],
            },
        },
    }]
}

USER_STORIES = {
    'function_declarations': [{
        'name': 'create_user_stories',
        'description': 'Creates user stories for a project.',
        'parameters': {
            'type_': 'ARRAY',
            "description": 'List of user stories that need to be created for the project.',
            "items": {
                "type_": 'STRING',
                'description': 'User story that needs to be created for the project.',
            },
        },
    }]
}

GET_COMMANDS={
    'function_declarations': [
        {
            'name': 'generate_commands',
            'description': 'generate a list of commands to be executed.',
            'parameters': {
                'type_': 'ARRAY',
                "description": "List of commands to execute.",
                "items": {
                    "type_": "OBJECT",
                    "properties": {
                        "command": {
                            "type_": "STRING",
                            "description": "Command to execute."
                        },
                        "timeout": {
                            "type_": "INTEGER",
                            "description": "Maximum execution time in milliseconds."
                        },
                        "success_message": {
                            "type_": "STRING",
                            "description": "Message that will displayed upon successful execution."
                        },
                        "command_id": {
                            "type_": "STRING",
                            "description": "Unique identifier for the command."
                        }
                    },
                    "required": ["command", "timeout", "command_id"]
                },
            },
        },
    ]
}