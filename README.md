
#AirBnB Clone - The Console

#Description:
This project is a simplified version of the AirBnB website, focusing on the backend functionality. The core component of this project is the command-line interpreter, or console, which allows users to interact with the underlying data models of the application.

#Command Interpreter:

Starting the Console:
To start the console, follow these steps:

Clone the project repository from GitHub.
Navigate to the directory containing the project files.
Run the console.py file using Python 3.

$ python3 console.py

#Using the Console:
Once the console is running, you can use various commands to interact with the data models. Here are the available commands:

create: Create a new instance of a data model and save it to the database.
show: Display the details of a specific instance based on its ID.

destroy: Delete a specific instance based on its ID.
all: Display details of all instances of a specific data model or of all data models.

update: Update the attributes of a specific instance.

#Examples:

To create a new User instance:

(hbnb) create User

To show details of a specific User instance with ID "123":

(hbnb) show User 123

To delete a specific User instance with ID "123":

(hbnb) destroy User 123

To display details of all instances of the User class:

(hbnb) all User

To update the email attribute of a specific User instance with ID "123":

(hbnb) update User 123 email "new_email@example.com"

These are just a few examples of how you can use the console to interact with the data models. Feel free to explore other commands and functionalities!

#Authors 👩‍💻
@NacimSaafi
