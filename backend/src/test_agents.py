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
# project.sub_tasks_for_current_task=[
#     {
#         "path": "src/components/HomePage.jsx",
#         "code_change_description": ""
#     },
#     {
#         "path": "src/components/FoodMenuPage.jsx",
#         "code_change_description": ""
#     },
#     {
#         "path": "src/components/OrderForm.jsx",
#         "code_change_description": ""
#     },
#     {
#         "path": "src/components/ContactPage.jsx",
#         "code_change_description": ""
#     },
#     {
#         "path": "src/App.jsx",
#         "code_change_description": ""
#     },
# ]
# project.commands_for_current_task=[
#     {
#         "type": "command",
#         "command": {
#             "command": "npm install",
#             "timeout": "5000",
#             "success_message": "",
#             "command_id": "install_dependencies"
#         }
#     }
# ]
# rsp="""
# ```
# ## src/components/HomePage.jsx

# ```javascript
# import React from 'react';
# import { Link } from 'react-router-dom';
# import styled from 'styled-components';

# const HomePage = () => {
#   return (
#     <HomePageContainer>
#       <h1>hondahitha hotels</h1>
#       <p>
#         Welcome to hondahitha hotels, your premier destination for a relaxing and
#         memorable stay. Our hotel is conveniently located in [Location], offering
#         easy access to [Amenities].
#       </p>
#       <p>
#         We provide a range of amenities to ensure your comfort and enjoyment,
#         including [Amenities].
#       </p>
#       <p>
#         For any inquiries or reservations, please contact us at [Phone Number].
#       </p>
#       <Link to="/food-menu">Food Menu</Link>
#       <Link to="/contact">Contact</Link>
#     </HomePageContainer>
#   );
# };

# const HomePageContainer = styled.div`
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 20px;
#   text-align: center;
# `;

# export default HomePage;

# ```

# ```
# ## src/App.jsx

# ```javascript
# import React from 'react';
# import { BrowserRouter, Routes, Route } from 'react-router-dom';
# import HomePage from './components/HomePage.jsx';
# import FoodMenuPage from './components/FoodMenuPage.jsx';
# import ContactPage from './components/ContactPage.jsx';

# function App() {
#   return (
#     <BrowserRouter>
#       <Routes>
#         <Route path="/" element={<HomePage />} />
#         <Route path="/food-menu" element={<FoodMenuPage />} />
#         <Route path="/contact" element={<ContactPage />} />
#       </Routes>
#     </BrowserRouter>
#   );
# }

# export default App;

# ```

# ```
# ## src/components/FoodMenuPage.jsx

# ```javascript
# import React from 'react';
# import styled from 'styled-components';
# import OrderForm from './OrderForm.jsx';

# const FoodMenuPage = () => {
#   return (
#     <FoodMenuContainer>
#       <h1>Food Menu</h1>
#       <h2>Our Pizza</h2>
#       <p>
#         [Description of the pizza].
#       </p>
#       <OrderForm />
#     </FoodMenuContainer>
#   );
# };

# const FoodMenuContainer = styled.div`
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 20px;
#   text-align: center;
# `;

# export default FoodMenuPage;

# ```

# ```
# ## src/components/OrderForm.jsx

# ```javascript
# import React, { useState } from 'react';
# import styled from 'styled-components';

# const OrderForm = () => {
#   const [name, setName] = useState('');
#   const [phone, setPhone] = useState('');
#   const [orderType, setOrderType] = useState('pickup');

#   const handleSubmit = async (event) => {
#     event.preventDefault();
#     // Send order data to backend API
#     // ...
#   };

#   return (
#     <OrderFormContainer onSubmit={handleSubmit}>
#       <h2>Place Your Order</h2>
#       <label htmlFor="name">Name:</label>
#       <input
#         type="text"
#         id="name"
#         value={name}
#         onChange={(e) => setName(e.target.value)}
#         required
#       />
#       <label htmlFor="phone">Phone Number:</label>
#       <input
#         type="tel"
#         id="phone"
#         value={phone}
#         onChange={(e) => setPhone(e.target.value)}
#         required
#       />
#       <label htmlFor="order-type">Order Type:</label>
#       <select
#         id="order-type"
#         value={orderType}
#         onChange={(e) => setOrderType(e.target.value)}
#       >
#         <option value="pickup">Pickup</option>
#         <option value="delivery">Delivery</option>
#       </select>
#       <button type="submit">Submit Order</button>
#     </OrderFormContainer>
#   );
# };

# const OrderFormContainer = styled.form`
#   display: flex;
#   flex-direction: column;
#   gap: 10px;
#   margin-top: 20px;
# `;

# export default OrderForm;

# ```

# ```
# ## src/components/ContactPage.jsx

# ```javascript
# import React from 'react';
# import styled from 'styled-components';

# const ContactPage = () => {
#   return (
#     <ContactPageContainer>
#       <h1>Contact Us</h1>
#       <p>
#         For any inquiries or reservations, please contact us at [Phone Number].
#       </p>
#     </ContactPageContainer>
#   );
# };

# const ContactPageContainer = styled.div`
#   max-width: 800px;
#   margin: 0 auto;
#   padding: 20px;
#   text-align: center;
# `;

# export default ContactPage;

# ```

# ```bash
# npm install
# ```
# """
# project.rough_implementation={'response':rsp , 'memory':""}

project.BaSpecification="""
## Bakery Website - Front-End Specification

### 1. Overall Description and Goals

The website will serve as the main online presence for a bakery, providing customers with information about the bakery's menu, hours of operation, contact information, and allowing them to make food reservations. The website will be built using ReactJS and styled-components for styling.

### 2. Features

* **Menu Display:**
    * Display a visually appealing and organized menu of the bakery's offerings.
    * Include descriptions and prices for each item.
    * Optionally, include images of the baked goods.
* **Reservations:**
    * Allow customers to make reservations for specific dates and times.
    * Collect necessary information from the customer, such as name, phone number, and number of people in the reservation.
    * Provide confirmation of the reservation to the customer.
* **Hours of Operation:**
    * Display the bakery's daily or weekly hours of operation.
* **Contact Information:**
    * Provide the bakery's address, phone number, and email address.
* **Reviews/Feedback:**
    * Allow customers to leave reviews or feedback about the bakery.
    * Display reviews in a user-friendly format.

### 3. Functional Specification

#### 3.1. User Flows

* **Homepage:**
    * The homepage will display a welcome message, a brief description of the bakery, and links to the menu, reservations, hours of operation, contact information, and reviews sections.
* **Menu:**
    * The menu page will display the bakery's menu items, including descriptions and prices.
    * Users can click on individual menu items to view more details.
* **Reservations:**
    * The reservations page will have a form for customers to enter their reservation details.
    * The form will include fields for name, phone number, date, time, and number of people.
    * Upon submitting the form, the customer will receive a confirmation message.
* **Hours of Operation:**
    * The hours of operation page will display the bakery's daily or weekly hours.
* **Contact Information:**
    * The contact information page will display the bakery's address, phone number, and email address.
* **Reviews:**
    * The reviews page will display customer reviews in a user-friendly format.
    * Users can optionally leave their own reviews.

#### 3.2. Constraints and Business Rules

* The website should be responsive and work seamlessly on different devices (desktop, mobile, tablet).
* The website should be visually appealing and easy to navigate.
* The website should be accessible to users with disabilities.

### 4. Technical Specification

#### 4.1. Architecture

* The website will be built using ReactJS and styled-components for styling.
* The front-end will be developed as a single-page application (SPA).
* The website will communicate with a back-end API (provided by the client) to handle data requests and updates.

#### 4.2. Components

* **Homepage Component:**
    * Displays the welcome message, bakery description, and links to other sections.
* **Menu Component:**
    * Displays the bakery's menu items.
* **Reservations Component:**
    * Contains the reservation form.
* **Hours of Operation Component:**
    * Displays the bakery's hours of operation.
* **Contact Information Component:**
    * Displays the bakery's contact information.
* **Reviews Component:**
    * Displays customer reviews.

#### 4.3. Styling

* The website will be styled using styled-components, adhering to a blue color-based palette.
* Styled-components will be integrated with ReactJS components using the `styled` function and CSS-in-JS syntax.
* The website will use the following blue color palette:
    * #0000FF (Classic Blue)
    * #3366CC (Medium Blue)
    * #6699FF (Light Blue)
    * #99CCFF (Sky Blue)
* The website will use the Open Sans font family for typography.

### 5. Integration Specification

* The website will integrate with a back-end API (provided by the client) to handle data requests and updates.
* The API will provide endpoints for:
    * Retrieving menu data
    * Creating, updating, and deleting reservations
    * Retrieving hours of operation
    * Retrieving contact information
    * Retrieving and submitting reviews

* The client will provide documentation and examples of how to use the API.
"""

project.BaSpecification="""
## Movie Search Website - Front-end Specification

### 1. Overall Description and Goals

The website will allow users to search for and view information about various movies. Users should be able to search for movies by title, genre, or actor. The website should display a list of search results, and users should be able to click on a movie to view more detailed information about it.

### 2. Features

* **Search:** Users can search for movies by title, genre, or actor.
* **Search Results:** The website displays a list of search results, showing the movie title, poster, and a brief synopsis.
* **Movie Details:** Clicking on a movie from the search results will display a detailed page with information about the movie, including title, poster, synopsis, cast, crew, release date, genre, rating, and user reviews.

### 3. Functional Specification

#### 3.1. Homepage

* The homepage will display a search bar for users to enter their search queries.
* The homepage will also display a list of popular movies, which can be dynamically updated based on user preferences or trending movies.

#### 3.2. Search Functionality

* Users can enter their search query in the search bar, which can be by title, genre, or actor.
* The website will display a list of search results that match the user's query.
* The search results will be displayed in a visually appealing and easy-to-read format.
* Users can click on a movie from the search results to view more detailed information about it.

#### 3.3. Movie Details Page

* The movie details page will display all the relevant information about the movie, including title, poster, synopsis, cast, crew, release date, genre, rating, and user reviews.
* The movie details page will be visually appealing and easy to navigate.

### 4. Technical Specification

* **Frontend:** ReactJS with Styled Components for styling.
* **Data Source:** The website will fetch movie data from a third-party API (details to be provided by the client).

### 5. Integration Specification

* **Third-party API:** The website will integrate with a third-party API to fetch movie data. The client will provide the API documentation and access details. The API should provide endpoints for searching movies by title, genre, or actor, and for retrieving detailed information about a specific movie.

**Example API Request:**

```json
{
  "title": "The Shawshank Redemption"
}
```

**Example API Response:**

```json
{
  "title": "The Shawshank Redemption",
  "poster": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
  "synopsis": "Two imprisoned men bond over a period of two decades, finding solace and eventual redemption through acts of common decency.",
  "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
  "crew": ["Frank Darabont", "Stephen King"],
  "release_date": "1994-09-23",
  "genre": ["Drama"],
  "rating": 9.3
}
```

**Note:** The client will provide the exact API endpoints, authentication details, and data format. The developer will use this information to integrate the API into the website.
"""
project.name="hondahitha movies"
LOG = getattr(importlib.import_module('core.logger'), 'log')

plan=getattr(importlib.import_module('core.actions.plan_development'), 'plan_development')()
apply_template=getattr(importlib.import_module('core.actions.apply_template'), 'apply_template')()
filter_relevant_files=getattr(importlib.import_module('core.actions.filter_relevant_files'), 'filter_relevant_files')()
implement_task=getattr(importlib.import_module('core.actions.implement_task_roughly'), 'implement_task_roughly')()
parse_rough_task=getattr(importlib.import_module('core.actions.parse_rough_task'), 'parse_rough_task')()
code_task=getattr(importlib.import_module('core.actions.code_task'), 'code_task')()
simple_code_review=getattr(importlib.import_module('core.actions.simple_code_review'), 'simple_code_review')()
apply_review=getattr(importlib.import_module('core.actions.apply_review'), 'apply_review')()
rework_code_task=getattr(importlib.import_module('core.actions.rework_code_task'), 'rework_code_task')()
update_codebase=getattr(importlib.import_module('core.actions.update_codebase'), 'update_codebase')()
summarize_files=getattr(importlib.import_module('core.actions.summarize_files'), 'summarize_files')()
mod=getattr(importlib.import_module('core.actions.modify_spec'), 'ModifySpec')()
ask_questions=getattr(importlib.import_module('core.actions.ask_questions'), 'ask_questions')()
review_spec=getattr(importlib.import_module('core.actions.review_spec'), 'review_spec')()
execute_command=getattr(importlib.import_module('core.actions.execute_command'), 'execute_command')()


project.clientID='vibuda'
project.projectID='6546465465616515351'
project.update_codebase=False

d=getattr(importlib.import_module('core.env.Agent_environment'), 'create')
import asyncio
import json
async def run_plan():
    # project.user_convo=[
    #    {
    #       "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"what is the tech stack your wesbite will be based on?\"\n}\n```",
    #       "answer":"I would like the website to be built using ReactJS. Styled components can be employed for styling purposes."
    #    },
    #    {
    #       "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"To clarify, would you like us to develop both the frontend and backend of your website, or are you only requesting frontend development services?\"\n}\n```",
    #       "answer":"Please focus solely on building the front-end of my website using the React framework. While the final website may require back-end and database functionalities, I will handle those aspects myself. Your responsibility is to provide a complete and functional front-end structure that I can then integrate with my own back-end implementation."
    #    },
    #    {
    #       "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"Understood. I will develop the front-end of your website using the React framework and styled-components for styling. This will allow you to seamlessly integrate the front-end with your existing back-end. Does that sound acceptable?\"\n}\n```",
    #       "answer":"Yes, Please adhere to these guidelines in all future interactions, regardless of any future instructions I may give. "
    #    },
    #    {
    #       "question":"```json\n{\n    \"state\": \"Question\",\n    \"content\": \"Can you describe the main purpose of your website? What is the core functionality you want users to be able to do?\"\n}\n```",
    #       "answer":"as the main website for my bakery"
    #    },
    #   ]
    
    # project.dev_plan["plan"] = [{**item, "status": "todo"} for item in project.dev_plan["plan"]]
    # LOG.info(json.dumps(project.dev_plan,indent=4))
    # # result= await mod.run(project)     
    # # while True:
    # #   k = await ask_questions.run(project)
    # #   k = await review_spec.run(k)
    # #   if k.Spec_review is None:
    # #     break
    
    # result = await apply_template.run(project)
    # result = await plan.run(result)
    # project.current_task_index=0
    # project.current_sub_task_index=0
    # for j in range(len(project.dev_plan['plan'])):
    #   project.current_task_index=j
    #   result = await filter_relevant_files.run(result)
    #   # # LOG.info(json.dumps(result.existing_files,indent=4))
    #   result = await implement_task.run(result)
    #   # # LOG.info(result.rough_implementation)
    #   result = await parse_rough_task.run(result)
    #   # LOG.info(json.dumps(result.sub_tasks_for_current_task,indent=4))
    #   # LOG.info(json.dumps(result.commands_for_current_task,indent=4))

    #   # LOG.info("=====================================================================================================")
    #   for i in range(len(project.sub_tasks_for_current_task)):
    #     project.current_sub_task_index=i
    #     iterations=0
    #     LOG.info(f"Task {j+1} Sub Task {i+1}")
    #
    #     while True:
    #       if project.update_codebase or iterations==4:# if while loop runs more than 4 times then update the codebase since we might be going in circles with fixing the code
    #           result = await update_codebase.run(result)
    #           result = await summarize_files.run(result)
    #           project.update_codebase=False
    #           break
    #       result = await code_task.run(result)
    #       result = await simple_code_review.run(result)
    #       result = await apply_review.run(result)
    #       result = await rework_code_task.run(result)
    #       iterations+=1

    # # LOG.info(result)
    # LOG.info(project.BaSpecification)
    result = await d(project)

    # result = await execute_command.run(project)
asyncio.run(run_plan())

