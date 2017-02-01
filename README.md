# Short Url Demo

This project is part of a technical interview. The challenge was:

Create a URL shortener API.
Requirements

These are the business rules that need to be fulfilled.
 - User should be able to submit any URL and get a standardized, shortened URL back
 - User should be able to configure a shortened URL to redirect to different targets based on the device type (mobile, tablet, desktop) of the user navigating to the shortened URL
 - Navigating to a shortened URL should redirect to the appropriate target URL
 - User should be able to retrieve a list of all existing shortened URLs, including time since creation and target URLs (each with number of redirects)
 - API requests and responses should be JSON formatted.
 - Write tests to prove functionality.

Considerations
These are some guidelines for scope and technology choice.

 - Don't worry about any user registration or authentication.
 - Use PHP, Python, or JavaScript with whatever web framework you prefer.
 - Use a relational database; I recommend SQLite for ease of use.
 - Please share this via a Github repository that we can clone.
 - Please provide instructions to set up, test and run the API in a local environment on Linux or Mac in a README file.
 - Building a front-end client for this API is not part of the assignment.
 - Deploying this API is not part of the assignment.


# Solution
 - The project has been developed using python and django
 - For the processing the user-agent I've use an external library of python
 - The Doc for the api can be found at /api/v1 of your running project. Exmples of how to interact with it can be found there
 - The Short urls created can be access at /url/<hash-of-the-url>
 - To test the project run "python manage.py test" from the root folder of the project. This can't be done with a docker running.

# Traditional Installation with virtualenv
 Installation can be done in the traditional way of using a virtual environment. In that case:
  1. Create a virtualenv for python3
  2. Install pip in your environment
  3. run pip install -r requirement.txt from the root folder of the project
  4. run "python manage.py runserver" This leaves the project runnning on port 8000

