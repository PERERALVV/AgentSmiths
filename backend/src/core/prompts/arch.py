GETARCHITECTURE="""
You're designing the architecture and technical specifications for a new project.

If the project requirements call out for specific technology, use that. Otherwise, prefer Node.js for the backend (with Express only if a web server is needed, and MongoDB if a database is needed), and REACT wirh Styled Components for the front-end. You MUST NOT use Docker, Kubernetes, microservices.

Here are the details for the new project:
-----------------------------
Here is a high level description of "{{ project_name }}":
```
{{ project_summary }}
```

Here are user stories that specify how users use "{{ project_name }}":
```
{{ user_stories }}
```

Here are user tasks that specify what users need to do to interact with "{{ project_name }}":
```
{{ user_tasks }}
```
-----------------------------

Based on these details, think step by step to design the architecture for the project and choose technologies to use in building it.

1. First, design and describe project architecture in general terms
2. Then, list any system dependencies that should be installed on the system prior to start of development.  For each system depedency, output a {{ os }} command to check whether it's installed.
3. Finally, list any other 3rd party packages or libraries that will be used (that will be installed later using packager a package manager in the project repository/environment).
4. Optionally, choose a project starter template.

You have an option to use a project template that implements standard boilerplate/scaffolding so you can start faster and be more productive. To be considered, a template must be compatible with the architecture and technologies you've choosen (it doesn't need to implement everything that will be used in the project, just a useful subset). If multiple templates can be considered, pick one that's the best match.        

If no project templates are a good match, don't pick any! It's better to start from scratch than to use a template that is not a good fit for the project and then spend time reworking it to fit the requirements.

Here are the available project templates:

### node_express_mongoose
Node + Express + MongoDB web app with session-based authentication, EJS views and Bootstrap 5

Contains:
* initial Node + Express setup
* User model in Mongoose ORM with username and password fields, ensuring username is unique and hashing passwords with bcrypt prior to saving to the database
* session-based authentication using username + password (hashed using bcrypt) in routes/authRoutes.js, using express-session
* authentication middleware to protect routes that require login
* EJS view engine, html head, header and footer EJS partials, with included Boostrap 5.x CSS and JS
* routes and EJS views for login, register, and home (main) page
* config loading from environment using dotenv with a placeholder .env.example file: you will need to create a .env file with your own values

### javascript_react
React web app using Vite devserver/bundler

Contains:
* Initial setup with Vite for fast development
* Basic project structure for React development
* Development server setup for hot reloading
* Minimal configuration to get started with React


*IMPORTANT*: You must follow these rules while creating your project:

* You must only list *system* dependencies, ie. the ones that need to be installed (typically as admin) to set up the programming language, database, etc. Any packages that will need to be installed via language/platform-specific package managers are *not* system dependencies.
* If there are several popular options (such as Nginx or Apache for web server), pick one that would be more suitable for the app in question.
* DO NOT include text editors, IDEs, shells, OpenSSL, CLI tools such as git, AWS, or Stripe clients, or other utilities in your list. only direct dependencies required to build and run the project.
* If a dependency (such as database) has a cloud alternative or can be installed on another computer (ie. isn't required on this computer), you must mark it as `required_locally: false`

Output only your response in JSON format like in this example, without other commentary:
```json
{
    "architecture": "Detailed description of the architecture of the application",
    "system_dependencies": [
        {
            "name": "Node.js",
            "description": "JavaScript runtime for building apps. This is required to be able to run the app you're building.",
            "test": "node --version",
            "required_locally": True
        },
        {
            "name": "MongoDB",
            "description": "NoSQL database. If you don't want to install MongoDB locally, you can use a cloud version such as MongoDB Atlas.",
            "test": "mongosh --version",
            "required_locally": False
        },
        ...
    ],
    "package_dependencies": [
        {
            "name": "express",
            "description": "Express web server for Node"
        },
        ...
    ],
    "template": "name of the project template to use" // or null if you decide not to use a project template
}
```

THIS IS IMPORTANT: 
IF THE high level description of "{{ project_name }}" ONLY DESCRIBES THE FRONTEND OF A WEBSITE then: 
    YOU SHOULD CREATE THE ARCHITECTURE ONLY FOR THE FRONTEND PART OF THE WEBSITE. NO NEED TO WORRY ABOUT THE BACKEND OR THE DATABASES OF THE WEBSITE.DO NOT INCLUDE ANY BACKEND OR DATABASES IN THE ARCHITECTURE.
IF THE high level description of "{{ project_name }}" DESCRIBE A WHOLE WEBSITE INCLUDING THE FRONTEND , BACKEND AND DATABASES then:
    YOU SHOULD CREATE THE ARCHITECTURE FOR THE WHOLE WEBSITE INCLUDING THE FRONTEND BACKEND AND DATABASES.

YOUR RESPONSE:
"""