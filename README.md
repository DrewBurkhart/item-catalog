# Item Catalog

> Item Catalog written in Python using Flask Framework,
> SQLAlchemy and Jinja templating.

### Instructions:

    1. Open Terminal
    1. cd into Vagrant directory
    1. Run 'vagrant up' command
    1. Run 'vagrant ssh' command
    1. cd into project directory /vagrant/catalog
    1. Run 'python database_setup.py' command to create database
    1. Run 'python lotsofcatalogs.py' command to populate database
    1. Run 'python project.py' command to run the app
    1. Go to http://localhost:5000 in your browser


### Contents:

**/static**
> CSS and JS files to style the site

**/templates**
> HTML files to create page templates

**database_setup.py**
> Python file to scaffold our database

**lotsofcatalogs.py**
> Python file to populate the database
> with some stock entities

**client_secrets.json & fb_client_secrets.json**
> JSON files used for Google and Facebook
> authentication with OAuth2

**project.py**
> The main Python file that describes
> all functionality for the site
