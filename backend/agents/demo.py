from agent import dev_agent

# create the agent
WebDev = dev_agent()

# create the input
input = {}
input["project"] = "hotel booking system"
input["webpage"] = "login page"
input["description"] = '''
I would like the login page of my hotel booking system website to have the following features:

* **Clean and user-friendly design:** The login page should have a simple and intuitive layout that is easy to navigate, even for first-time users. It should also be visually appealing and reflect the overall branding of my hotel booking website.

* **Secure login:** The login page should use SSL encryption and other security measures to protect user data. I would also like to have the option to enable two-factor authentication for added security.

* **Multiple login options:** In addition to the traditional username and password login, I would like to offer social media login options (e.g., Facebook, Google, Twitter) for added convenience.

* **Forgot password feature:** I want to make it easy for users to reset their passwords if they forget them. The login page should have a prominent link to a password reset page where users can enter their email address to receive a password reset link.

* **Create an account link:** If I allow new user registrations on my website, I want to include a clear and visible link to a registration page where users can create an account.

* **Informative error messages:** If a user enters incorrect login credentials or encounters any other errors, the login page should display informative error messages that help them identify and resolve the issue.

* **Customization options:** I would like the ability to customize the login page to match the specific needs and branding of my hotel booking website. This may include changing the color scheme, adding custom logos or images, and modifying the text and error messages.

Overall, I expect the login page of my hotel booking system website to be secure, user-friendly, and customizable to meet the unique requirements of my business.
'''
result = WebDev.chainquery(input)
print(result)
