# ge0de's Notepad App
## Description:
***This project is a personalized notepad web application that I built using Flask, a lightweight Python web framework, and SQLite for database management. The purpose of this Notepad app is to allow users to create, store, and manage their own notes in a secure and user-friendly environment.***

***The Notepad application uses Flask for routing and handling requests. Flask makes it easy to manage dynamic content like users' account registration, login, and note creation. SQLite, a serverless relational database, stores user data, including usernames, passwords, and notes. The app utilizes Flask’s session management to ensure that users remain logged in and that their notes are linked to their unique account.***

***Users can simply register with a username and password. Upon successful registration, they are redirected to the login page where they can enter their credentials. If authenticated, they gain access to the main dashboard, where they can view, add, edit, or delete notes. The notes are displayed in a listed format, with each note having options to be edited or deleted. The notes are stored in the database, allowing for persistence across sessions.***

***I designed the front-end of this application using HTML, CSS, and Bootstrap. Bootstrap ensures the app has a responsive and clean layout, making it accessible on both desktop and mobile devices. The styling is kept minimal, focusing on functionality and user experience. Forms are used for adding new notes, with each note stored in a database and displayed dynamically when the user revisits the dashboard.***

***This Notepad app is secure, using hashed passwords with Flask’s Werkzeug library to prevent storing plain text passwords. This ensures users' credentials are safe. Overall, this project showcases my proven fundamental web development skills, including backend (Flask, SQLite) and frontend (HTML, CSS, Bootstrap) technologies, as well as secure authentication practices.***


# What each file does:

## app.py
***main Python file where the Flask application is set up. It contains routes for user registration, login, dashboard, note creation, editing, and deletion. It also manages session handling and interacts with the SQLite database.***

## requirements.txt
***Lists all the dependencies required for the project, including Flask and other necessary Python libraries. This file is used for setting up the environment using pip install -r requirements.txt, which is what I have done.***

## static/style.css
***Custom styles for the application to enhance the user interface, such as fonts, colors, margins, and other layout adjustments.***

## templates/index.html
***The base template that contains the common structure of the pages, like the header, footer, and the link to style.css. Other HTML files extend this base template.***

## templates/login.html
***The login page template where users can enter their credentials to log in.***

## templates/register.html
***The registration page template where users can create a new account by entering their username and password.***

## templates/dashboard.html
***Displays the user's dashboard after logging in, where they can add, view, edit, or delete their notes.***

## templates/notepad.html
***Displays the form for creating and editing notes. It allows users to input their note content, which is then saved to the database.***

## templates/edit_note.html
***helps users edit their notes.***

## notepad.db
***The SQLite database file that stores user information (like usernames and passwords) and their notes. The app interacts with this file to save and retrieve data.***

## init_db.py
***helps initialize the database environment.***
