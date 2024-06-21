import importlib
project=getattr(importlib.import_module('models.project'), 'Project')()
project.name="hondahitha hotels"
project.BaSpecification="""
A simple hotel website with a static menu for food ordering.

The website will have the following pages:

* Home page: 
    * Displays a brief description of the hotel (e.g., location, amenities, contact information).
    * Links to the food menu and contact page.
* Food menu page:
    * Displays a static menu of the hotel's restaurant. 
    * The menu will only feature one type of pizza, with no variations.
    * Users can submit their order (with their name and phone number) for pickup or delivery.
    * The order submission form will not allow users to select a specific time for pickup or delivery.
* Contact page:
    * Displays the hotel's phone number (0771234567).

The website will be built using the following technologies:

* Backend: Node.js with Express framework.
* Database: MongoDB with Mongoose ORM.
* Frontend: EJS view engine, Bootstrap for styling, and vanilla JavaScript.

The website will be implemented in the following way:

* Home page: The home page will be a simple HTML page with a few paragraphs of text and links to other pages.
* Food menu page: The menu items (in this case, only one pizza) will be stored in a MongoDB collection. The website will retrieve the menu items from the database and display them on the page. The order submission form will be handled by an Express route, collecting user name and phone number and storing this data in the database. The user will not receive any confirmation of their order after submitting it.
* Contact page: The contact page will be a simple HTML page with the hotel's phone number.

The website will not have any user authentication or registration functionality, images or videos. The website will have a basic design with no specific color scheme or font preferences.
"""
project.BaSpecification="""
## Frontend Specification\n\nA simple hotel website with a static menu for food ordering.\n\nThe website will have the following pages:\n\n* **Home page:**\n    * Displays a brief description of the hotel (e.g., location, amenities, contact information).\n    * Links to the food menu and contact page.\n* **Food menu page:**\n    * Displays a static menu of the hotel's restaurant. \n    * The menu will only feature one type of pizza, with no variations.\n    * Users can submit their order (with their name and phone number) for pickup or delivery.\n    * The order submission form will not allow users to select a specific time for pickup or delivery.\n* **Contact page:**\n    * Displays the hotel's phone number (0771234567).\n\nThe website will be built using the following technologies:\n\n* **Frontend:** ReactJS framework, styled-components for styling, and vanilla JavaScript.\n\nThe website will be implemented in the following way:\n\n* **Home page:** The home page will be a React component with a simple layout, including paragraphs of text and links to other pages.\n* **Food menu page:** The menu items (in this case, only one pizza) will be hardcoded into the React component. The website will display the menu items on the page. The order submission form will be handled by a React component, collecting user name and phone number and sending this data to the backend API. The user will not receive any confirmation of their order after submitting it.\n* **Contact page:** The contact page will be a React component with a simple layout, displaying the hotel's phone number.\n\nThe website will not have any user authentication or registration functionality, images or videos. The website will have a basic design with no specific color scheme or font preferences. \n
"""
project.userStories=[
    "As a user, I want to visit the home page to learn about the hotel, including its location, amenities, and contact information.",
    "As a user, I want to navigate to the food menu page from the home page to view the available food options.",
    "As a user, I want to view the hotel's food menu, which includes a single pizza option.",
    "As a user, I want to submit an order for the pizza, including my name and phone number.",
    "As a user, I want to choose between pickup or delivery for my order.",
    "As a user, I want to submit my order without specifying a specific pickup or delivery time.",
    "As a user, I want to navigate to the contact page from the home page to find the hotel's phone number.",
    "As a user, I want to view the hotel's phone number on the contact page."
  ]
project.userTasks=[
    {
      "user story": "As a user, I want to visit the home page to learn about the hotel, including its location, amenities, and contact information.",
      "user tasks": [
        "user navigates to the hotel's website home page",
        "user views the hotel's location information",
        "user views the hotel's amenities information",
        "user views the hotel's contact information"
      ]
    },
    {
      "user story": "As a user, I want to navigate to the food menu page from the home page to view the available food options.",
      "user tasks": [
        "user navigates to the hotel's website home page",
        "user clicks on the 'Food Menu' link or button"
      ]
    },
    {
      "user story": "As a user, I want to view the hotel's food menu, which includes a single pizza option.",
      "user tasks": [
        "user navigates to the food menu page",
        "user views the pizza option on the menu"
      ]
    },
    {
      "user story": "As a user, I want to submit an order for the pizza, including my name and phone number.",
      "user tasks": [
        "user navigates to the food menu page",
        "user selects the pizza option",
        "user enters their name",
        "user enters their phone number",
        "user clicks on the 'Submit Order' button"
      ]
    },
    {
      "user story": "As a user, I want to choose between pickup or delivery for my order.",
      "user tasks": [
        "user navigates to the food menu page",
        "user selects the pizza option",
        "user selects either 'Pickup' or 'Delivery' option"
      ]
    },
    {
      "user story": "As a user, I want to submit my order without specifying a specific pickup or delivery time.",
      "user tasks": [
        "user navigates to the food menu page",
        "user selects the pizza option",
        "user selects either 'Pickup' or 'Delivery' option",
        "user clicks on the 'Submit Order' button"
      ]
    },
    {
      "user story": "As a user, I want to navigate to the contact page from the home page to find the hotel's phone number.",
      "user tasks": [
        "user navigates to the hotel's website home page",
        "user clicks on the 'Contact' link or button"
      ]
    },
    {
      "user story": "As a user, I want to view the hotel's phone number on the contact page.",
      "user tasks": [
        "user navigates to the contact page",
        "user views the hotel's phone number"
      ]
    }
  ]
project.architecture_desc="""
The application will be a single-page application (SPA) built with ReactJS. The frontend will handle all user interactions and display dynamic content. The application will not require a backend server or database, as all data will be hardcoded into the React components. The frontend will be built using ReactJS, styled-components for styling, and vanilla JavaScript. The application will be deployed to a static hosting service, such as Netlify or Vercel.
"""
project.system_dependencies=[
      {
        "name": "Node.js",
        "description": "JavaScript runtime for building apps. This is required to be able to run the app you're building.",
        "test": "node --version",
        "required_locally": True
      }
    ]

project.package_dependencies=[
      {
        "name": "react",
        "description": "JavaScript library for building user interfaces"
      },
      {
        "name": "react-dom",
        "description": "React library for rendering components to the DOM"
      },
      {
        "name": "styled-components",
        "description": "CSS-in-JS library for styling React components"
      },
      {
        "name": "vite",
        "description": "Fast development server and build tool for React"
      }
    ]
project.template_name="javascript_react"
project.dev_plan={
  "plan": [
    {
      "description": "Create a React component for the home page, named `HomePage.jsx`, located in `src/components/HomePage.jsx`. The component should display a brief description of the hotel, including its location, amenities, and contact information. The description should be hardcoded into the component. The component should also include links to the food menu and contact pages. The links should be implemented using React Router. The component should be styled using styled-components to match the basic design requirements. The component should be tested to ensure that it renders correctly and that the links work as expected."
    },
    {
      "description": "Create a React component for the food menu page, named `FoodMenuPage.jsx`, located in `src/components/FoodMenuPage.jsx`. The component should display a static menu of the hotel's restaurant. The menu should only feature one type of pizza, with no variations. The menu items should be hardcoded into the component. The component should also include an order submission form. The form should collect the user's name and phone number. The form should allow the user to choose between pickup or delivery. The form should not allow the user to select a specific time for pickup or delivery. The form should be handled by a React component, named `OrderForm.jsx`, located in `src/components/OrderForm.jsx`. The `OrderForm.jsx` component should collect the user's name and phone number and send this data to the backend API. The user will not receive any confirmation of their order after submitting it. The component should be styled using styled-components to match the basic design requirements. The component should be tested to ensure that it renders correctly and that the form works as expected."
    },
    {
      "description": "Create a React component for the contact page, named `ContactPage.jsx`, located in `src/components/ContactPage.jsx`. The component should display the hotel's phone number. The phone number should be hardcoded into the component. The component should be styled using styled-components to match the basic design requirements. The component should be tested to ensure that it renders correctly."
    },
    {
      "description": "Create a React component for the main app, named `App.jsx`, located in `src/App.jsx`. The component should be the root component of the application. The component should use React Router to route between the home page, food menu page, and contact page. The component should be styled using styled-components to match the basic design requirements. The component should be tested to ensure that it renders correctly and that the routing works as expected."
    },
    {
      "description": "Update the `index.html` file, located in `public/index.html`, to include the necessary HTML structure for the application. The HTML structure should include a `div` element with the id `root`, which will be used to mount the React application. The HTML structure should also include the necessary links to the CSS files for the application. The HTML structure should be tested to ensure that it renders correctly."
    },
    {
      "description": "Update the `main.jsx` file, located in `src/main.jsx`, to render the `App` component. The `main.jsx` file should also include the necessary imports for the `App` component and the `ReactDOM` library. The `main.jsx` file should be tested to ensure that it renders the `App` component correctly."
    }
  ],
  "status": "todo"
}

plan=getattr(importlib.import_module('core.actions.plan_development'), 'plan_development')()
apply_template=getattr(importlib.import_module('core.actions.apply_template'), 'apply_template')()
filter_relevant_files=getattr(importlib.import_module('core.actions.filter_relevant_files'), 'filter_relevant_files')()
implement_task=getattr(importlib.import_module('core.actions.implement_task'), 'implement_task')()

get_root=getattr(importlib.import_module('const.ProjectConst'), 'get_root')
project.clientID='6546465465616515362'
project.root_path=get_root(clientID=project.clientID,project_name=project.name)

import asyncio
import json
async def run_plan():
    result = await apply_template.run(project)
    # result = await plan.run(result)
    project.current_task_index=0
    result= await filter_relevant_files.run(project)
    # print(json.dumps(result.existing_files,indent=4))
    result= await implement_task.run(result)
    return result


asyncio.run(run_plan())

