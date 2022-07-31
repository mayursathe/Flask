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
3. forgot_password.html - Template to let user enter email so that a new password can be sent. (This is just a placeholder template and has no functionality added to it)
4. success.html - This is the final page where the user is greeted after successful login.

# Libraries used :
1. flask - Contains all the keywords used to create flask application
2. flask_sqlalchemy - Used to connect flask application to sqlite database
3. flask_bcrypt - Used to salt and hash passwords in the application
4. flask_login - Used for user session management for 'remember me' functionality
5. wtforms - Used to validate input form data such as input size, datatype, etc.

# Functionalities Created :
1. Login Authentication
    1. Reads the username and password as input from HTML form.
    2. Searches for username in database and returns the first one it finds (username is unique so only one can be found).
    3. If not found, throws an error 'Username/Password is not valid.'.
    4. If found, compares the password in database with input.
    5. If not matched, throws an error 'Username/Password is not valid.'.
    6. If matched, routes to successful login page with 'welcome {username}' message.

2. Remember Me
    1. If checked, saves the username, email and password in cookie.
    2. The next time user comes to login page, the username and password will be pre-filled.
    3. If not checked, clears the cookie.

3. Forgot Password
    1. Routes to forgot_password page.
    2. E-mail input is given, but this page is just a placeholder.