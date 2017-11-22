# Flask application

[![Build Status](https://travis-ci.org/sasakad/shoppinglist-andela.svg?branch=master)](https://travis-ci.org/sasakad/shoppinglist-andela)


This is repo contains an application created with python language and flask framework.
Install
The software needed for this project

Create and clone this repo 

$ git clone https://github.com/sasakad/shoppinglist-andela.git
$ cd flask-app-template
Create templates using html and css the templates to be used later in creating the flask application.The templates will enable the user to
    Log in
    Register
    Delete,Add and edit shoppinglists
    
## Installation
Set up flask:Download flask
   $ pip install flask
    
Create a virtualenv, and activate this:
$ virtualenv env 
$ source env/bin/activate

Write your flask app with the main file being the 
  $MAIN.PY

To see your application, run the file and access this url in your browser: 

	http://localhost:5000

##To deploy to heroku one needs to: 
##Open a heroku account

 
After, install all dependecies necessary to run:

    $ pip install -r requirements.txt
 Dependecies of flask:
 **Flask-Login** - Flask-Login provides user session management for Flask.
* **Flask-Bootstrap** - Ready-to-use Twitter-bootstrap for use in Flask.

* **Flask-Admin** - Flask extension module that provides an admin interface

* **Flask-Mail** - Makes sending mails from Flask applications very easy and has also support for unittesting.

* **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask. Quick and easy.

* **Flask-WTF** - Flask-Themes makes it easy for your application to support a wide range of appearances.
 Intergrating coveralls and continuous intergration
 Open the travis ci and login with git hub
 OPen coveralls and also login with github
     Add repo to activate repo to intergrate with travis ci
     Start building repo to intergrate travis ci and ensure tests
     If any errors are encountered traceback errors and restart build
    

