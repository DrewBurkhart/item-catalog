<h1>Item Catalog</h1>

> Item Catalog written in Python using Flask Framework,
> SQLAlchemy and Jinja templating.

<h2>Instructions:</h2>
<ol>
    <li>Open Terminal</li>
    <li>cd into Vagrant directory</li>
    <li>Run 'vagrant up' command</li>
    <li>Run 'vagrant ssh' command</li>
    <li>cd into project directory /vagrant/catalog</li>
    <li>Run 'python database_setup.py' command to create database</li>
    <li>Run 'python lotsofcatalogs.py' command to populate database</li>
    <li>Run 'python project.py' command to run the app</li>
    <li>Go to http://localhost:5000 in your browser</li>
</ol>

<h3>Contents:</h3>

<strong>/static</strong>
> CSS and JS files to style the site

<strong>/templates</strong>
> HTML files to create page templates

<strong>database_setup.py</strong>
> Python file to scaffold our database

<strong>lotsofcatalogs.py</strong>
> Python file to populate the database
> with some stock entities

<strong>client_secrets.json & fb_client_secrets.json</strong>
> JSON files used for Google and Facebook
> authentication with OAuth2

<strong>project.py</strong>
> The main Python file that describes
> all functionality for the site
