# TENSORIOT

# Tasks to be done : 
1. Refer figma project here https://www.figma.com/file/bn2U7kKDRMSE4VtXVkIFk2/Task
2. Develop the Authentication logic for the UI design provided
3. Develop the api code using Flask micro-framework
4. Use JWT/salted passwords for Authenticating the Users
5. SQLite for any database operations
6. Write Detailed README file for running the application locally.

# Files used :
1. app.py - Contains required initializations and global settings for application
2. db.py - Contains schema for user table and can be run independently to add rows into the user table
3. models.py - Contains classes for FlaskForm
4. urls.py - Contains all routing information and authentication logic. This is the main file that is to be run to start the application.

# Templates used :
1. login.html - Template to show the main login page.
2. check_user_data.html - Template to show failed login state in case of unsuccessful login attempt.
3. forgot_password.html - Template to let user enter email so that a new password can be sent. (This is just a placehlder template and has no functionality added to it)
4. success.html - This is the final page where the user is greeted after successful login.