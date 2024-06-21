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
            # "additionalProperties": False #not sure about compatibility fo this line with gemini
        }
    }],
}