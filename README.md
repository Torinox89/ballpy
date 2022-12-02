# ballpy
This API defines the boundary between the front-end and back-end.
It will allow to complement Front-end Views.
The database is ready to be filled.
For this API, it is the minimum essential for interconnectivity with the database.

Overall, the process for creating an API with Flask:

Create a virtual environment.
Install and import Flask.
Create an application factory.
Import and invoke the application factory on a root app.py file.
Create the database in Postgres and configure it within the app using Flask-SQLAlchemy.
Create the database instance and all necessary models.
Create blueprints and all necessary routes.
Import the database models into the application factory.
Import and register all blueprints onto the application factory.
Import and install Flask-Migrate to migrate the database changes.
