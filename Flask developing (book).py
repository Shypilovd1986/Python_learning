#                                    CHAPTER 1
# Flask has three main dependencies. The routing, debugging, and Web Server Gateway Interface (WSGI) subsystems come
# from Werkzeug; the template support is provided by Jinja2; and the command-line integration comes from Click. These
# dependencies are all authored by Armin Ronacher, the author of Flask.

# If you are using the stock Python 3 interpreter on an Ubuntu Linux system, the standard venv package is not installed
# by default. To add it to your system, install the python3-venv package as follows:
# $ sudo apt-get install python3-venv

# The command that creates a virtual environment has the following structure:
# $ python3 -m venv virtual-environment-name

# The -m venv option runs the venv package from the standard library as a standalone script, passing the desired name as
# an argument.
# pip install flask
# pip freeze > requirements.txt

#                                   CHAPTER 2 Basic Application Structure
# ____________________________________________________________________________________________________________________
#                                               Initialization
# ____________________________________________________________________________________________________________________
# All Flask applications must create an application instance. The web server passes all requests it receives from
# clients to this object for handling, using a protocol called Web Server Gateway Interface
# (WSGI, pronounced “wiz-ghee”). The application instance is an object of class Flask, usually created as follows:

# from flask import Flask
# app = Flask(__name__)

# The only required argument to the Flask class constructor is the name of the main module or package of the application
# For most applications, Python’s __name__ variable is the correct value for this argument.

# ____________________________________________________________________________________________________________________
#                                           Routes and View Functions
# ____________________________________________________________________________________________________________________
# Clients such as web browsers send requests to the web server, which in turn sends them to the Flask application
# instance. The Flask application instance needs to know what code it needs to run for each URL requested, so it keeps
# a mapping of URLs to Python functions. The association between a URL and the function that handles it is called
# a route.

# The previous example registers function index() as the handler for the application’s root URL. While the app.route
# decorator is the preferred method to register view functions, Flask also offers a more traditional way to set up the
# application routes with the app.add_url_rule() method, which in its most basic form takes three arguments: the URL,
# the endpoint name, and the view function. The following example uses app.add_url_rule() to register an index()
# function that is equivalent to the one shown previously:
# def index():
#   return '<h1>Hello World!</h1>'
# app.add_url_rule('/', 'index', index)

# If you pay attention to how some URLs for services that you use every day are formed, you will notice that many have
# variable sections. For example, the URL for your Facebook profile page has the format
# https://www.facebook.com/<your-name>, which includes your username, making it different for each user. Flask supports
# these types of URLs using a special syntax in the app.route decorator. The following example defines a route that
# has a dynamic component:

# @app.route('/user/<name>')
# def user(name):
#   return '<h1>Hello, {}!</h1>'.format(name)

# The portion of the route URL enclosed in angle brackets is the dynamic part. Any URLs that match the static portions
# will be mapped to this route, and when the view function is invoked, the dynamic component will be passed as an
# argument. In the preceding example, the name argument is used to generate a response that includes a personalized
# greeting.

# The dynamic components in routes are strings by default but can also be of different types. For example, the route
# /user/<int:id> would match only URLs that have an integer in the id dynamic segment, such as /user/123. Flask supports
# the types string, int, float, and path for routes. The path type is a special string type that can include forward
# slashes, unlike the string type.

# ____________________________________________________________________________________________________________________
#                           Development Web Server
# ____________________________________________________________________________________________________________________

# Flask applications include a development web server that can be started with the flask run command. This command looks
# for the name of the Python script that contains the application instance in the FLASK_APP environment variable.
# To start the hello.py application from the previous section, first make sure the virtual environment you created
# earlier is activated and has Flask installed in it. For Linux and macOS users, start the web server as follows:
# (venv) $ export FLASK_APP=hello.py
# (venv) $ flask run
#      * Serving Flask app "hello"
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# For Microsoft Windows users, the only difference is in how the FLASK_APP environment variable is set:
# (venv) $ set FLASK_APP=hello.py
# (venv) $ flask run

# The web server provided by Flask is intended to be used only for development and testing.

# The Flask development web server can also be started programmatically by invoking the app.run() method. Older
# versions of Flask that did not have the flask command required the server to be started by running the application’s
# main script, which had to include the following snippet at the end:

# if __name__ == '__main__':
#   app.run()

# While the flask run command makes this practice unnecessary, the app.run() method can still be useful on certain
# occasions

# ____________________________________________________________________________________________________________________
#                                           Debug Mode
# ____________________________________________________________________________________________________________________

# Flask applications can optionally be executed in debug mode. In this mode, two very convenient modules of the
# development server called the reloader and the debugger are enabled by default.

# By default, debug mode is disabled. To enable it, set a FLASK_DEBUG=1 environment variable before invoking flask run:
# (venv) $ export FLASK_APP=hello.py
# (venv) $ export FLASK_DEBUG=1
# (venv) $ flask run
#      * Serving Flask app "hello"
#      * Forcing debug mode on
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#      * Restarting with stat
#      * Debugger is active!
#      * Debugger PIN: 273-181-528
# If you are using Microsoft Windows, use set instead of export to set the environment variables.

# ____________________________________________________________________________________________________________________
#                                   Command-Line Options
# ____________________________________________________________________________________________________________________
# The flask command supports a number of options. To see what’s available, you can run flask --help or just flask
# without any arguments:

# (venv) $ flask --help

# Usage: flask [OPTIONS] COMMAND [ARGS]...
# This shell command acts as general utility script for Flask applications. It loads the application configured
# (through the FLASK_APP environment variable) and then provides commands either provided by the application or Flask
# itself.

# The most useful commands are the "run" and "shell" command.

# The flask shell command is used to start a Python shell session in the context of the application. You can use this
# session to run maintenance tasks or tests, or to debug issues.

# The --host argument is particularly useful because it tells the web server what network interface to listen to for
# connections from clients. By default, Flask’s development web server listens for connections on localhost, so only
# connections originating from the computer running the server are accepted. The following command makes the web server
# listen for connections on the public network interface, enabling other computers in the same network to connect as
# well:
# (venv) $ flask run --host 0.0.0.0
# * Serving Flask app "hello"
# * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

# ____________________________________________________________________________________________________________________
#                       Application and Request Contexts
# ____________________________________________________________________________________________________________________
# When Flask receives a request from a client, it needs to make a few objects available to the view function that will
# handle it. A good example is the request object, which encapsulates the HTTP request sent by the client.
#
# Variable name            Context                Description
# current_app      Application context    The application instance for the active application.
# g                Application context    An object that the application can use for temporary storage during the
#                                         handling of a request. This variable is reset with each request.
# request,         Request context        The request object, which encapsulates the contents of an HTTP request sent by
#                                         the client.
# session          Request context        The user session, a dictionary that the application can use to store values
#                                         that are “remembered” between requests.

# from flask import request
# @app.route('/')
# def index():
#   user_agent = request.headers.get('User-Agent')
#   return '<p>Your browser is {}</p>'.format(user_agent)

# Note how in this view function, request is used as if it were a global variable. In reality, request cannot be a
# global variable; in a multithreaded server several threads can be working on different requests from different clients
# all at the same time, so each thread needs to see a different object in request. Contexts enable Flask to make
# certain variables globally accessible to a thread without interfering with the other threads.

# A thread is the smallest sequence of instructions that can be managed independently. It is common for a process to
# have multiple active threads, sometimes sharing resources such as memory or file handles. Multithreaded web servers
# start a pool of threads and select a thread from the pool to handle each incoming request.

# There are two contexts in Flask: the application context and the request context.

# ____________________________________________________________________________________________________________________
#                                            The Request Object
# ____________________________________________________________________________________________________________________
# You have seen that Flask exposes a request object as a context variable named request. This is an extremely useful
# object that contains all the information that the client included in the HTTP request. Table 2-2 enumerates the most
# commonly used attributes and methods of the Flask request object.
#                       Table 2-2. Flask request object
#                             Attribute or Method
# form           A dictionary with all the form fields submitted with the request.
# args           A dictionary with all the arguments passed in the query string of the URL.
# values         A dictionary that combines the values inform and args.
# cookies        A dictionary with all the cookies included in the request.
# headers        A dictionary with all the HTTP headers included in the request.
# files          A dictionary with all the file uploads included with the request.
# get_data()     Returns the buffered data from the request body.
# get_json()     Returns a Python dictionary with the parsed JSON included in the body of the request.
# blueprint      The name of the Flask blueprint that is handling the request.
# endpoint       The name of the Flask endpoint that is handling the request. Flask uses the name of the view function
#                as the endpoint name for a route.
# method         The HTTP request method, such as GET or POST.
# scheme         The URL scheme (http or https).
# is_secure()    Returns True if the request came through a secure (HTTPS) connection.
# host           The host defined in the request, including the port number if given by the client.
# path           The path portion of the URL.
# query_string   The query string portion of the URL, as a raw binary value.
# full_path      The path and query string portions of the URL.
# url            The complete URL requested by the client.
# base_url       Same as url, but without the query string component.
# remote_addr    The IP address of the client.
# environ        The raw WSGI environment dictionary for the request.

# ____________________________________________________________________________________________________________________
#                                           Request Hooks
# ____________________________________________________________________________________________________________________
# Sometimes it is useful to execute code before or after each request is processed. For example, at the start of each
# request it may be necessary to create a database connection or authenticate the user making the request. Instead of
# duplicating the code that performs these actions in every view function, Flask gives you the option to register common
# functions to be invoked before or after a request is dispatched.

# Request hooks are implemented as decorators. These are the four hooks supported by Flask:
# before_request
# Registers a function to run before each request.

# before_first_request
# Registers a function to run only before the first request is handled. This can be a convenient way to add server
# initialization tasks.

# after_request
# Registers a function to run after each request, but only if no unhandled exceptions occurred.

# teardown_request
# Registers a function to run after each request, even if unhandled exceptions occurred.

# A common pattern to share data between request hook functions and view functions is to use the g context global as
# storage. For example, a before_request handler can load the logged-in user from the database and store it in g.user.
# Later, when the view function is invoked, it can retrieve the user from there.

# ____________________________________________________________________________________________________________________
#                                                   Responses
# ____________________________________________________________________________________________________________________
# When Flask invokes a view function, it expects its return value to be the response to the request. In most cases the
# response is a simple string that is sent back to the client as an HTML page.
# But the HTTP protocol requires more than a string as a response to a request. A very important part of the HTTP
# response is the status code, which Flask by default sets to 200, the code that indicates that the request was carried
# out successfully.
# When a view function needs to respond with a different status code, it can add the numeric code as a second return
# value after the response text. For example, the following view function returns a 400 status code, the code for a
# bad request error:

# @app.route('/')
# def index():
#    return '<h1>Bad Request</h1>', 400

# Responses returned by view functions can also take a third argument, a dictionary of headers that are added to the
# HTTP response.

# Instead of returning one, two, or three values as a tuple, Flask view functions have the option of returning a
# response object. The make_response() function takes one, two, or three arguments, the same values that can be returned
# from a view function, and returns an equivalent response object. Sometimes it is useful to generate the response
# object inside the view function, and then use its methods to further configure the response. The following example
# creates a response object and then sets a cookie in it:

# from flask import make_response
# @app.route('/')
# def index():
#   response = make_response('<h1>This document carries a cookie!</h1>')
#   response.set_cookie('answer', '42')
#   return response

# Table 2-3 shows the most commonly used attributes and methods available in response objects.

# Attribute or Method                Description
# status_code           The numeric HTTP status code
# headers               A dictionary-like object with all the headers that will be sent with the response
# set_cookie()          Adds a cookie to the response
# delete_cookie()       Removes a cookie
# content_length        The length of the response body
# content_type          The media type of the response body
# set_data()            Sets the response body as a string or bytes value
# get_data()            Gets the response body

# There is a special type of response called a redirect. This response does not include a page document; it just gives
# the browser a new URL to navigate to. A very common use of redirects is when working with web forms

# A redirect is typically indicated with a 302 response status code and the URL to go to given in a Location header.
# A redirect response can be generated manually with a three-value return or with a response object, but given its
# frequent use, Flask provides a redirect() helper function that creates this type of response:

# from flask import redirect
# @app.route('/')
# def index():
#   return redirect('http://www.example.com')

# Another special response is issued with the abort() function, which is used for error handling. The following example
# returns status code 404 if the id dynamic argument given in the URL does not represent a valid user:

# from flask import abort
# @app.route('/user/<id>')
# def get_user(id):
#   user = load_user(id) if not user:
#   abort(404)
#   return '<h1>Hello, {}</h1>'.format(user.name)

# Note that abort() does not return control back to the function because it raises an exception.
# ____________________________________________________________________________________________________________________
 #                                          Templates
# ____________________________________________________________________________________________________________________

# Variables can be modified with filters, which are added after the variable name with a pipe character as separator.
# For example, the following template shows the name variable capitalized:
    # Hello, {{ name|capitalize }}

# Table 3-1. Jinja2 variable filters
# Filter name    description

# safe           Renders the value without applying escaping
# capitalize     Converts the first character of the value to uppercase and the rest to lowercase
# lower          Converts the value to lowercase characters
# upper          Converts the value to uppercase characters
# title          Capitalizes each word in the value
# trim           Removes leading and trailing whitespace from the value
# striptags      Removes any HTML tags from the value before rendering

# ____________________________________________________________________________________________________________________
#                                       Control Structures
# ____________________________________________________________________________________________________________________
# Jinja2 offers several control structures that can be used to alter the flow of the template. This section introduces
# some of the most useful ones with simple examples.
# The following example shows how conditional statements can be entered in a template:
#     {% if user %}
#         Hello, {{ user }}!
#     {% else %}
#         Hello, Stranger!
# {% endif %}
# Another common need in templates is to render a list of elements. This example shows how this can be done with
# a for loop:
# <ul>
#    {% for comment in comments %}
# <li>{{ comment }}</li>
# {% endfor %}
# </ul>
# Jinja2 also supports macros, which are similar to functions in Python code. For example:
# {% macro render_comment(comment) %} <li>{{ comment }}</li>
#     {% endmacro %}
# <ul>
#         {% for comment in comments %}
#             {{ render_comment(comment) }}
# {% endfor %}
# </ul>
# To make macros more reusable, they can be stored in standalone files that are then imported from all the templates
# that need them:
#     {% import 'macros.html' as macros %}
# <ul>
#         {% for comment in comments %}
#             {{ macros.render_comment(comment) }}
# {% endfor %}
# </ul>
# Portions of template code that need to be repeated in several places can be stored in a separate file and included
# from all the templates to avoid repetition:
#     {% include 'common.html' %}
# Yet another powerful way to reuse is through template inheritance, which is similar to class inheritance in Python
# code. First, a base template is created with the name base.html:
#     <html>
#     <head>
# {% block head %}
# <title>{% block title %}{% endblock %} - My Application</title>
# {% endblock %}
#     </head>
#     <body>
#         {% block body %}
#         {% endblock %}
#     </body>
#     </html>
# Base templates define blocks that can be overridden by derived templates. The Jinja2 block and endblock directives
# define blocks of content that are added to the base template. In this example, there are blocks called head, title,
# and body; note that title is contained by head. The following example is a derived template of the base template:

# ____________________________________________________________________________________________________________________
#                                 flask_moment
# ____________________________________________________________________________________________________________________
# Localization of Dates and Times with Flask-Moment
# pip install flask-moment
#
# from flask_moment import Moment
# moment = Moment(app)
#
# @app.route('/')
# def index():
#   return render_template('index.html', current_time=datetime.utcnow())

# {{ moment.include_moment() }}
# <p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
# <p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>

# The format('LLL') function renders the date and time according to the time zone and locale settings in the client
# computer. The argument determines the rendering style, from 'L' to 'LLLL' for four different levels of verbosity. The
# format() function can also accept a long list of custom format specifiers.
# The fromNow() render style shown in the second line renders a relative timestamp and automatically refreshes it as
# time passes. Initially this timestamp will be shown as “a few seconds ago,” but the refresh=True option will keep it
# updated as time passes, so if you leave the page open for a few minutes you will see the text changing to “a minute
# ago,” then “2 minutes ago,” and so on.

# Flask-Moment implements the format(), fromNow(), fromTime(), calendar(), valueOf(), and unix() methods from Moment.js.
# Consult the Moment.js documentation to learn about all the formatting options offered by this library.

# The timestamps rendered by Flask-Moment can be localized to many languages. A language can be selected in the template
# by passing the two-letter language code to function locale(), right after the Moment.js library is included.
# For example, here is how to configure Moment.js to use Spanish:
#     {% block scripts %}
#     {{ super() }}
#     {{ moment.include_moment() }}
#     {{ moment.locale('es') }}
#     {% endblock %}

# ____________________________________________________________________________________________________________________
#                            Static Files
# ____________________________________________________________________________________________________________________

# You may recall that when the hello.py application’s URL map was inspected in Chapter 2, a static entry appeared in
# it. Flask automatically supports static files by adding a special route to the application defined as
# /static/<filename>. For example, a call to url_for('static', filename='css/styles.css', _external=True) would return
# http://localhost:5000/static/css/styles.css.
# In its default configuration, Flask looks for static files in a subdirectory called static located in the
# application’s root folder.

#
# {% block head %}
# {{ super() }}
# <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
# <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
# {% endblock %}

# The icon declaration is inserted at the end of the head block.

# Note how super() is used to preserve the original contents of the block defined in the base templates.   !!!!!!!

# ____________________________________________________________________________________________________________________
#                                 Web Forms
#                                 flask-WTF
# ____________________________________________________________________________________________________________________
#                             Configuration
# The Flask-WTF extension makes working with web forms a much more pleasant experience. This extension is a Flask
# integration wrapper around the framework-agnostic WTForms package.
# Flask-WTF and its dependencies can be installed with pip:
# (venv) $ pip install flask-wtf

# Unlike most other extensions, Flask-WTF does not need to be initialized at the application level, but it expects
# the application to have a secret key configured. A secret key is a string with any random and unique content that is
# used as an encryption or signing key to improve the security of the application in several ways. Flask uses this key
# to protect the contents of the user session against tampering. You should pick a different secret key in each
# application that you build and make sure that this string is not known by anyone.

# The app.config dictionary is a general-purpose place to store configuration variables used by Flask, extensions, or
# the application itself. Configuration values can be added to the app.config object using standard dictionary syntax.
# The configuration object also has methods to import configuration values from files or the environment.

# flask-WTF requires a secret key to be configured in the application because this key is part of the mechanism the
# extension uses to protect all forms against cross-site request forgery (CSRF) attacks. A CSRF attack occurs when a
# malicious website sends requests to the application server on which the user is currently logged in. Flask-WTF
# generates security tokens for all forms and stores them in the user session, which is protected with a cryptographic
# signature generated from the secret key.

# ____________________________________________________________________________________________________________________
#                               Form Classes
# ____________________________________________________________________________________________________________________
# When using Flask-WTF, each web form is represented in the server by a class that inherits from the class FlaskForm.
# The class defines the list of fields in the form, each represented by an object. Each field object can have one or
# more validators attached. A validator is a function that checks whether the data submitted by the user is valid.

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# class NameForm(FlaskForm):
#    name = StringField('What is your name?',validators=[DataRequired()])
#    submit = SubmitField('Submit')

# The fields in the form are defined as class variables, and each class variable is assigned an object associated with
# the field type.

# The optional validators argument included in the StringField constructor defines a list of checkers that will be
# applied to the data submitted by the user before it is accepted. The DataRequired() validator ensures that the field
# is not submitted empty.

# The FlaskForm base class is defined by the Flask-WTF extension, so it is imported from flask_wtf. The fields and
# validators, however, are imported directly from the WTForms package.

#                           The list of standard HTML fields supported by WTForms

# Field type                Description

# BooleanField              Checkbox with True and False values
# DateField                 Text field that accepts a datetime. date value in a given format
# DateTimeField             Text field that accepts a datetime. datetime value in a given format
# DecimalField              Text field that accepts a decimal. Decimal value
# FileField                 File upload field
# HiddenField               Hidden text field
# MultipleFileField         Multiple file upload field
# FieldList                 List of fields of a given type
# FloatField                Text field that accepts a floating-point value
# FormField                 Form embedded as a field in a container form
# IntegerField              Text field that accepts an integer value
# PasswordField             Password text field
# RadioField                List of radio buttons
# SelectField               Drop-down list of choices
# SelectMultipleField       Drop-down list of choices with multiple selection
# SubmitField               Form submission button
# StringField               Text field
# TextAreaField             Multiple-line text field

#               The list of WTForms built-in validators is shown in

#   Validator                   Description

# DataRequired          Validates that the field contains data after type conversion
# Email                 Validates an email address
# EqualTo               Compares the values of two fields; useful when requesting a password to be entered twice for
#                       confirmation
# InputRequired         Validates that the field contains data before type conversion
# IPAddress             Validates an IPv4 network address
# Length                Validates the length of the string entered
# MacAddress            Validates a MAC address
# NumberRange           Validates that the value entered is within a numeric range
# Optional              Allows empty input in the field, skipping additional validators
# Regexp                Validates the input against a regular expression
# URL                   Validates a URL
# UUID                  Validates a UUID
# AnyOf                 Validates that the input is one of a list of possible values
# NoneOf                Validates that the input is none of a list of possible values

# we need install extension : pip install email-validator   for working with Email validator !!!!!!!!!!!!!!!!!!!!!!!!!!
#
#                       HTML Rendering of Forms

# <form method="POST">
# {{ form.hidden_tag() }}
# {{ form.name.label }} {{ form.name() }} {{ form.submit() }}
# </form>

# Note that in addition to the name and submit fields, the form has a form.hidden_tag() element. This element defines an
# extra form field that is hidden, used by Flask-WTF to implement CSRF protection.

#                       Form Handling in View Functions

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   name = None
#   form = NameForm()
#   if form.validate_on_submit():
#         name = form.name.data
#   form.name.data = ''
#   return render_template('index.html', form=form, name=name)

# The validate_on_submit() method of the form returns True when the form was submitted and the data was accepted by all
# the field validators. In all other cases, validate_on_submit() returns False. The return value of this method
# effectively serves to determine whether the form needs to be rendered or processed.

# ____________________________________________________________________________________________________________________
#                           Redirects and User Sessions
# ____________________________________________________________________________________________________________________
# it is considered good practice for web applications to never leave a POST request as the last request sent by the
# browser.
# This is achieved by responding to POST requests with a redirect instead of a normal response. A redirect is a special
# type of response that contains a URL instead of a string with HTML code. it issues a GET request for the redirect URL,
# and that is the page that it displays.
#
# Applications can “remember” things from one request to the next by storing them in the user session, a private storage
# that is available to each connected client.

# from flask import Flask, render_template, session, redirect, url_for
# @app.route('/', methods=['GET', 'POST'])
# def index():
#   form = NameForm()
#   if form.validate_on_submit():
#      session['name'] = form.name.data
#      return redirect(url_for('index'))
#   return render_template('index.html', form=form, name=session.get('name'))

# The redirect() function takes the URL to redirect to as an argument.
# The first and only required argument to url_for() is the endpoint name, the internal name each route has.
# ____________________________________________________________________________________________________________________
#                               Message Flashing
# ____________________________________________________________________________________________________________________
# old_name = session.get('name')
# if old_name is not None and old_name != form.name.data:
#   flash('Looks like you have changed your name!')

# {% for message in get_flashed_messages() %}
# <div class="alert alert-warning">
#   <button type="button" class="close" data-dismiss="alert">&times;</button>
#   {{ message }}
# </div>
# {% endfor %}

# form.<name_field>.errors   handle collection of errors  !!
# ____________________________________________________________________________________________________________________
#                                                   Databases
# ____________________________________________________________________________________________________________________
# called SQL databases in reference to the Structured Query Language they use. But in recent years document-oriented and
# key-value databases, informally known together as NoSQL databases

# Relational databases store data in tables,
# A table has a fixed number of columns and a variable number of rows.
# This graphical style of representing the structure of a database is called an entity relationship diagram.

# Databases that do not follow the relational model described in the previous section are collectively referred to as
# NoSQL databases. One common organization for NoSQL databases uses collections instead of tables and documents instead
# of records. NoSQL databases are designed in a way that makes joins difficult, so most of them do not support this
# operation at all. A more appropriate design for a NoSQL database is shown in Figure 5-2. This is the result of
# applying an operation called denormalization, which reduces the number of tables at the expense of data duplication.

# ACID, which stands for Atomicity, Consistency, Isolation, and Durability. NoSQL databases relax some of ACID
# requirements and as a result can sometimes get a performance edge.

# there are also a number of database abstraction layer packages, such as SQLAlchemy or MongoEngine, that allow you to
# work at a higher level with regular Python objects instead of database entities such as tables, documents, or query
# languages.

# When comparing straight database engines to database abstraction layers, the second group clearly wins. Abstraction
# layers, also called object-relational mappers (ORMs) or object-document mappers (ODMs), provide transparent
# conversion of high-level object-oriented operations into low-level database instructions.

# Flask-SQLAlchemy is a Flask extension that simplifies the use of SQLAlchemy inside Flask applications. SQLAlchemy is
# a powerful relational database framework that supports several database backends. It offers a high-level ORM and
# low-level access to the database’s native SQL functionality.

# Like most other extensions, Flask-SQLAlchemy is installed with pip:
# (venv) $ pip install flask-sqlalchemy
# In Flask-SQLAlchemy, a database is specified as a URL. Table 5-1 lists the format of the URLs for the three most
# popular database engines.

# Table 5-1. Flask-SQLAlchemy database URLs

# Database                  engine
# MySQL             mysql://username:password@hostname/database
# Postgres          postgresql://username:password@hostname/database
# SQLite (Linux, macOS)       sqlite:////absolute/path/to/database
# SQLite (Windows)            sqlite:///c:/absolute/path/to/database

# In these URLs, hostname refers to the server that hosts the database service, which could be localhost or a remote
# server.

# The URL of the application database must be configured as the key SQLALCHEMY_DATABASE_URI in the Flask configuration
# object. The Flask-SQLAlchemy documentation also suggests setting key SQLALCHEMY_TRACK_MODIFICATIONS to False for using
# less memory unless signals for object changes are needed.

# import os
# from flask_sqlalchemy import SQLAlchemy
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# The term model is used when referring to the persistent entities used by the application. In the context of an ORM,
# a model is typically a Python class with attributes that match the columns of a corresponding database table.

# The __tablename__ class variable defines the name of the table in the database.

# class User(db.Model):
#   __tablename__ = 'users'
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(64), unique=True, index=True)

#   def __repr__(self):
#       return '<User %r>' % self.username

#           Most common SQLAlchemy column options
# primary_key       If set to True, the column is the table’s primary key.
# unique            If set to True, do not allow duplicate values for this column.
# index             If set to True, create an index for this column, so that queries are more efficient.
# nullable   If set to True, allow empty values for this column. If set to False, the column will not allow null values.
# default           Define a default value for the column.

# __repr__() method to give them a readable string representation that can be used for debugging and testing purposes.

# Relational databases establish connections between rows in different tables through the use of relationships.
# This is a one-to-many relationship from roles to users, because one role can belong to many users, but each user can
# have only one role.

# class Role(db.Model): # ...
#     users = db.relationship('User', backref='role')
# class User(db.Model): # ...
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

# The 'roles.id' argument to db.ForeignKey() specifies that the column should be interpreted as having id values from
# rows in the roles table.

# The users attribute added to the model Role represents the object-oriented view of the relationship, as seen from the
# “one” side. Given an instance of class Role, the users attribute will return the list of users associated with that
# role

# The backref argument to db.relationship() defines the reverse direction of the relationship, by adding a role
# attribute to the User model. This attribute can be used on any instance of User instead of the role_id foreign key
# to access the Role model as an object.

# The very first thing to do is to instruct Flask-SQLAlchemy to create a database based on the model classes.
# The db.create_all() function locates all the subclasses of db.Model and creates corresponding tables in the database
# for them:
# (venv) $ flask shell
# >>> from hello import db
# >>> db.create_all()
#
# !!!!!!  Will remove old tables
# db.drop_all()

# Inserting Rows
# The following example creates a few roles and users:

# >>> from hello import Role, User
# >>> admin_role = Role(name='Admin')
# >>> mod_role = Role(name='Moderator')
# >>> user_role = Role(name='User')
# >>> user_john = User(username='john', role=admin_role)
# >>> user_susan = User(username='susan', role=user_role)
# >>> user_david = User(username='david', role=user_role)

# The constructors for models accept initial values for the model attributes as keyword arguments. Note that the role
# attribute can be used, even though it is not a real database column but a high-level representation of the
# one-to-many relationship. The id attribute of these new objects is not set explicitly: the primary keys in many
# databases are managed by the database itself. The objects exist only on the Python side so far; they have not been
# written to the database yet. Because of that, their id values have not yet been assigned:
# >>> print(admin_role.id) None

# Changes to the database are managed through a database session, which Flask- SQLAlchemy provides as db.session.
# To prepare objects to be written to the database, they must be added to the session:
# >>> db.session.add(admin_role)

# Or, more concisely:
# >>> db.session.add_all([admin_role, mod_role, user_role, ... user_john, user_susan, user_david])

# To write the objects to the database, the session needs to be committed by calling its commit() method:
# >>> db.session.commit()

# The db.session database session is not related to the Flask session object discussed in Chapter 4. Database sessions
# are also called transactions.

# Database sessions are extremely useful in keeping the database consistent. The commit operation writes all the
# objects that were added to the session atomically. if an error occurs while the session is being written, the whole
# session is discarded.

# A database session can also be rolled back. If db.session.rollback() is called, any objects that were added to the

#                    Modifying Rows
# The add() method of the database session can also be used to update models. Continuing in the same shell session,
# the following example renames the "Admin" role to "Administrator":
# >>> admin_role.name = 'Administrator'
# >>> db.session.add(admin_role)
# >>> db.session.commit()
#                   Deleting Rows
# The database session also had delete() method. The following example deletes the "Moderator" role from the database:
# >>> db.session.delete(mod_role)
# >>> db.session.commit()
# Note that deletions, like insertions and updates, are executed only when the database session is committed. !!!!!!

#               Querying Rows

# Flask-SQLAlchemy makes a query object available in each model class. The most basic query for a model is triggered
# with the all() method, which returns the entire contents of the corresponding table:
# >>> Role.query.all()
# [<Role 'Administrator'>, <Role 'User'>]

# The following example finds all the users that were assigned the "User" role:
# >>> User.query.filter_by(role=user_role).all() [<User 'susan'>, <User 'david'>]

# >>> user_role = Role.query.filter_by(name='User').first()
# Note how in this case, the query was issued with the first() method instead of all().

#                           Table 5-5. Common SQLAlchemy query filters.
# filter()          Returns a new query that has an additional filter to the original query
# filter_by()       Returns a new query that has an additional equality filter to the original query
# limit()           Returns a new query that limits the number of results of the original query to the given number
# offset()          Returns a new query that applies an offset into the list of results of the original query
# order_by()        Returns a new query that sorts the results of the original query according to the given criteria
# group_by()        Returns a new query that groups the results of the original query according to the given criteria

#                           Table 5-6. Most common SQLAlchemy query executors

# all()                 Returns all the results of a query as a list
# first()               Returns the first result of a query, or None if there are no results
# first_or_404()        Returns the first result of a query, or aborts the request and sends a 404 error as the response
#                       if there are no results
# get()                 Returns the row that matches the given primary key, or None if no matching row is found
# get_or_404()          Returns the row that matches the given primary key or, if the key is not found, aborts the
#                       request and sends a 404 error as the response
# count()               Returns the result count of the query
# paginate()            Returns a Pagination object that contains the specified range of results
# ____________________________________________________________________________________________________________________
#                              Integration with the Python Shell
# ____________________________________________________________________________________________________________________
# To add objects to the import list, a shell context processor must be created and registered with the
# app.shell_context_processor decorator.

# @app.shell_context_processor
# def make_shell_context():
#   return dict(db=db, User=User, Role=Role)

# The shell context processor function returns a dictionary that includes the database instance and the models. The
# flask shell command will import these items automatically into the shell, in addition to app, which is imported by
# default:
# $ flask shell
# >>> app
# <Flask 'hello'>
# >>> db
# <SQLAlchemy engine='sqlite:////home/flask/flasky/data.sqlite'>
# ____________________________________________________________________________________________________________________
#                   Database Migrations with Flask-Migrate
# ____________________________________________________________________________________________________________________
# only way to make it update tables is by destroying the old tables
# A better solution is to use a database migration framework.
# Flask applications can use the Flask-Migrate extension
# pip install flask-migrate

# from flask_migrate import Migrate # ...
# migrate = Migrate(app, db)
# To expose the database migration commands, Flask-Migrate adds a flask db command with several subcommands. When you
# work on a new project, you can add support for database migrations with the init subcommand:

# Alembic migrations can be created manually or automatically using the revision and migrate commands, respectively.
# A manual migration creates a migration skeleton script with empty upgrade() and downgrade() functions that need to be
# implemented by the developer using directives exposed by Alembic’s Operations object. An automatic migration attempts
# to generate the code for the upgrade() and downgrade() functions by looking for differences between the model
# definitions and the current state of the database.

# about db migration
# https://flask-migrate.readthedocs.io/en/latest/

# With the above application you can create a migration repository with the following command:
# $ flask db init

# You can then generate an initial migration:
# $ flask db migrate -m "Initial migration."

# Then you can apply the changes described by the migration script to your database:
# $ flask db upgrade

# To see all the commands that are available run this command:
# $ flask db --help

# ____________________________________________________________________________________________________________________
#                       Email Support with Flask-Mail
# ____________________________________________________________________________________________________________________

# pip install flask-mail
# The extension connects to a Simple Mail Transfer Protocol (SMTP) server and passes emails to it for delivery. If no
# configuration is given, Flask-Mail connects to localhost at port 25 and sends email without authentication.

# Flask-Mail SMTP server configuration keys
# Key                Default         Description
#
# MAIL_SERVER       localhost       Hostname or IP address of the email server
# MAIL_PORT         25              Port of the email server
# MAIL_USE_TLS      False           Enable Transport Layer Security (TLS) security
# MAIL_USE_SSL      False           Enable Secure Sockets Layer (SSL) security
# MAIL_USERNAME     None            Mail account username
# MAIL_PASSWORD     None            Mail account password
#                       from official site !
# MAIL_SERVER : default ‘localhost’
# MAIL_PORT : default 25
# MAIL_USE_TLS : default False
# MAIL_USE_SSL : default False
# MAIL_DEBUG : default app.debug
# MAIL_USERNAME : default None
# MAIL_PASSWORD : default None
# MAIL_DEFAULT_SENDER : default None
# MAIL_MAX_EMAILS : default None
# MAIL_SUPPRESS_SEND : default app.testing
# MAIL_ASCII_ATTACHMENTS : default False
# In addition the standard Flask TESTING configuration option is used by Flask-Mail in unit tests (see below).
# Emails are managed through a Mail instance:
#
# from flask import Flask
# from flask_mail import Mail
#
# app = Flask(__name__)
# mail = Mail(app)
# In this case all emails are sent using the configuration values of the application that was passed to the Mail class
# constructor.
# Alternatively you can set up your Mail instance later at configuration time, using the init_app method:
#
# mail = Mail()
# app = Flask(__name__)
# mail.init_app(app)
# In this case emails will be sent using the configuration values from Flask’s current_app context global. This is
# useful if you have multiple applications running in the same process but with different configuration options.

# During development it may be more convenient to connect to an external SMTP server.
# import os
# # ...
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# from flask_mail import Mail
# mail = Mail(app)

# The two environment variables that hold the email server username and password need to be defined in the environment.
# If you are on Linux or macOS, you can set these variables as follows:
# (venv) $ export MAIL_USERNAME=<Gmail username>
# (venv) $ export MAIL_PASSWORD=<Gmail password>

# For Microsoft Windows users, the environment variables are set as follows:
# (venv) $ set MAIL_USERNAME=<Gmail username>
# (venv) $ set MAIL_PASSWORD=<Gmail password>

# Sending Email from the Python Shell
# To test the configuration, you can start a shell session and send a test email (replace you@example.com with your own email address):
# (venv) $ flask shell
# >>> from flask_mail import Message
# >>> from hello import mail
# >>> msg = Message('test email', sender='you@example.com', ... recipients=['you@example.com'])
# >>> msg.body = 'This is the plain text body'
# >>> msg.html = 'This is the <b>HTML</b> body'
# >>> with app.app_context():
# ... mail.send(msg)
# ...
# Note that Flask-Mail’s send() function uses current_app, so it needs to be executed with an activated application
# context.

# Integrating Emails with the Application
# To avoid having to create email messages manually every time, it is a good idea to abstract the common parts of the
# application’s email sending functionality into a function. As an added benefit, this function can render email bodies
# from Jinja2 templates to have the most flexibility. The implementation is shown in Example 6-3.
# Example 6-3. hello.py: email support

# from flask_mail import Message
# app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
# def send_email(to, subject, template, **kwargs):
#   msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     mail.send(msg)


# The index() view function can easily be expanded to send an email at the administrator whenever a new name is
# received with the form. Example 6-4 shows this change.
# Example 6-4. hello.py: email example
# # ...
# app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN') # ...
# @app.route('/', methods=['GET', 'POST'])
# def index():
# form = NameForm()
# if form.validate_on_submit():
# user = User.query.filter_by(username=form.name.data).first() if user is None:
# user = User(username=form.name.data) db.session.add(user) session['known'] = False
# if app.config['FLASKY_ADMIN']:
#                 send_email(app.config['FLASKY_ADMIN'], 'New User',
#                            'mail/new_user', user=user)
# else:
# session['known'] = True
# session['name'] = form.name.data form.name.data = ''
# return redirect(url_for('index'))
# return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

# In addition to the MAIL_USERNAME and MAIL_PASSWORD environment variables described earlier, this version of the
# application needs the FLASKY_ADMIN environment variable. For Linux and macOS users, the command to set this
# variable is:
# (venv) $ export FLASKY_ADMIN=<your-email-address>
# For Microsoft Windows users, this is the equivalent command:
# (venv) $ set FLASKY_ADMIN=<your-email-address>
# With these environment variables set, you can test the application and receive an
# email every time you enter a new name in the form.

# Sending Asynchronous Email
# If you sent a few test emails, you likely noticed that the mail.send() function blocks for a few seconds while the
# email is sent, making the browser look unresponsive dur‐ ing that time. To avoid unnecessary delays during request
# handling, the email send function can be moved to a background thread. Example 6-5 shows this change.
# Example 6-5. hello.py: asynchronous email support
# from threading import Thread
# def send_async_email(app, msg): with app.app_context():
#         mail.send(msg)
# def send_email(to, subject, template, **kwargs):
#   msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#   msg.body = render_template(template + '.txt', **kwargs)
#   msg.html = render_template(template + '.html', **kwargs)
#   thr = Thread(target=send_async_email, args=[app, msg])
#   thr.start()
#   return thr

# This implementation highlights an interesting problem. Many Flask extensions oper‐ ate under the assumption that there
# are active application and/or request contexts. As mentioned previously, Flask-Mail’s send() function uses
# current_app, so it requires the application context to be active. But since contexts are associated with a thread,
# when the mail.send() function executes in a different thread it needs the application context to be created
# artificially using app.app_context(). The app instance is passed to the thread as an argument so that a context can be
# created.

# ____________________________________________________________________________________________________________________
#                           Large Application Structure
# ____________________________________________________________________________________________________________________
#
# |-flasky
#   |-app/
#       |-templates/
#       |-static/
#       |-main/
#           |-__init__.py
#           |-errors.py
#           |-forms.py
#           |-views.py
#       |-__init__.py
#       |-email.py
#       |-models.py
#   |-migrations/
#   |-tests/
#       |-__init__.py
#       |-test*.py
#   |-venv/
#   |-requirements.txt
#   |-config.py
#   |-flasky.py
#
# ____________________________________________________________________________________________________________________
#                                   Configuration Options
# ____________________________________________________________________________________________________________________

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# class Config:
# SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
# MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.googlemail.com')
# MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
# MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
#         ['true', 'on', '1']
#     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#     FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
#     FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
#     FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     @staticmethod
# def init_app(app): pass
# class DevelopmentConfig(Config): DEBUG = True
# SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \ 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')
# class TestingConfig(Config): TESTING = True
# SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \ 'sqlite://'
# class ProductionConfig(Config):
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
#     'default': DevelopmentConfig

# The Config base class contains settings that are common to all configurations; the different subclasses define
# settings that are specific to a configuration. Additional configurations can be added as needed.

# ____________________________________________________________________________________________________________________
#                       Application Package
# ____________________________________________________________________________________________________________________
# The application package is where all the application code, templates, and static files live. It is called simply app
# here, though it can be given an application-specific name if desired. The templates and static directories are now
# part of the application package, so they are moved inside app. The database models and the email support functions are
# also moved inside this package, each in its own module, as app/models.py and app/email.py.

# ____________________________________________________________________________________________________________________
#                   Using an Application Factory
# ____________________________________________________________________________________________________________________

# The solution to this problem is to delay the creation of the application by moving it into a factory function that can
# be explicitly invoked from the script.

# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy from config import config
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()
# def create_app(config_name):
# app = Flask(__name__) app.config.from_object(config[config_name]) config[config_name].init_app(app)
#     bootstrap.init_app(app)
#     mail.init_app(app)
#     moment.init_app(app)
#     db.init_app(app)
#     # attach routes and custom error pages here
# return app

# This constructor imports most of the Flask extensions currently in use, but because there is no application instance
# to initialize them with, it creates them uninitialized by passing no arguments into their constructors.
# The create_app() function is the application factory, which takes as an argument the name of a configuration to use
# for the application.
# ____________________________________________________________________________________________________________________
#                       Implementing Application Functionality in a Blueprint
# ____________________________________________________________________________________________________________________

#           app/main/__init__.py: main blueprint creation
# from flask import Blueprint
# main = Blueprint('main', __name__)
# from . import views, errors

# Blueprints are created by instantiating an object of class Blueprint. The constructor for this class takes two
# required arguments: the blueprint name and the module or package where the blueprint is located. As with applications,
# Python’s __name__ vari‐ able is in most cases the correct value for the second argument.
# The routes of the application are stored in an app/main/views.py module inside the package, and the error handlers are
# in app/main/errors.py.

#              app/__init__.py: main blueprint registration
# def create_app(config_name): # ...
# from .main import main as main_blueprint
# app.register_blueprint(main_blueprint)
# return app

# Example 7-6 shows the error handlers.
# Example 7-6. app/main/errors.py: error handlers in main blueprint
# from flask import render_template from . import main
# @main.app_errorhandler(404) def page_not_found(e):
# return render_template('404.html'), 404
# @main.app_errorhandler(500) def internal_server_error(e):
# return render_template('500.html'), 500
# A difference when writing error handlers inside a blueprint is that if the errorhandler decorator is used, the handler
# will be invoked only for errors that originate in the routes defined by the blueprint. To install application-wide
# error handlers, the app_errorhandler decorator must be used instead.

# The flasky.py module in the top-level directory is where the application instance is defined. This script is shown in
# Example 7-8. flasky.py: main script
# import os
# from app import create_app, db from app.models import User, Role from flask_migrate import Migrate
# app = create_app(os.getenv('FLASK_CONFIG') or 'default') migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
# return dict(db=db, User=User, Role=Role)
# The script begins by creating an application. The configuration is taken from the environment variable FLASK_CONFIG
# if it’s defined, or else the default configuration is used. Flask-Migrate and the custom context for the Python shell
# are then initialized.

# ____________________________________________________________________________________________________________________
#                   Hashing Passwords with Werkzeug
# ____________________________________________________________________________________________________________________

# Werkzeug’s security module conveniently implements secure password hashing. This functionality is exposed with just
# two functions, used in the registration and verification phases, respectively:

# generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

# This function takes a plain-text password and returns the password hash as a string that can be stored in the user
# database. The default values for method and salt_length are sufficient for most use cases.

# check_password_hash(hash, password)

# This function takes a password hash previously stored in the database and the password entered by the user. A return
# value of True indicates that the user pass‐ word is correct.

# ____________________________________________________________________________________________________________________
#                                   User Authentication with Flask-Login
# ____________________________________________________________________________________________________________________

# When users log in to the application, their authenticated state has to be recorded in the user session, so that it is
# remembered as they navigate through different pages. Flask-Login is a small but extremely useful extension that
# specializes in managing this particular aspect of a user authentication system, without being tied to a specific
# authentication mechanism.

# To begin, the extension needs to be installed in the virtual environment:
# (venv) $ pip install flask-login

# ____________________________________________________________________________________________________________________
#                                       Preparing the User Model for Logins
# ____________________________________________________________________________________________________________________

# Flask-Login works closely with the application’s own User objects. To be able to work with the application’s User
# model, the Flask-Login extension requires it to implement a few common properties and methods. The required items are
# shown in Table 8-1.
# Table 8-1. Flask-Login required items
# Property/method         Description
# is_authenticated     Must be True if the user has valid login credentials or False otherwise.
# is_active            Must be True if the user is allowed to log in or False otherwise. A False value can be used for
#                      disabled accounts.
# is_anonymous         Must always be False for regular users and True for a special user object that represents
#                      anonymous users.
# get_id()             Must return a unique identifier for the user, encoded as a Unicode string.
#
# These properties and methods can be implemented directly in the model class, but as an easier alternative Flask-Login
# provides a UserMixin class that has default implementations that are appropriate for most cases. The updated User
# model is shown in Example 8-6.

# from flask_login import UserMixin
# class User(UserMixin, db.Model):
#   __tablename__ = 'users'
#   id = db.Column(db.Integer, primary_key = True)
#    email = db.Column(db.String(64), unique=True, index=True)
#    username = db.Column(db.String(64), unique=True, index=True)
#    password_hash = db.Column(db.String(128))
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

# Example 8-7. app/__init__.py: Flask-Login initialization
# from flask_login import LoginManager login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# def create_app(config_name): # ...
# login_manager.init_app(app, True) # ...

# The login_view attribute of the LoginManager object sets the endpoint for the login page. Flask-Login will redirect to
# the login page when an anonymous user tries to access a protected page. Because the login route is inside a blueprint,
# it needs to be prefixed with the blueprint name.
# Finally, Flask-Login requires the application to designate a function to be invoked when the extension needs to load a
# user from the database given its identifier. This function is shown in Example 8-8.

# Example 8-8. app/models.py: user loader function

# from . import login_manager

# @login_manager.user_loader
# def load_user(user_id):
#   return User.query.get(int(user_id))

# The login_manager.user_loader decorator is used to register the function with Flask-Login, which will call it when it
# needs to retrieve information about the logged-in user. The user identifier will be passed as a string, so the
# function converts it to an integer before it passes it to the Flask-SQLAlchemy query that loads the user.

# ____________________________________________________________________________________________________________________
#                                           Protecting Routes
# ____________________________________________________________________________________________________________________

# To protect a route so that it can only be accessed by authenticated users, Flask-Login provides a login_required
# decorator. An example of its usage follows:

# from flask_login import login_required
# @app.route('/secret')
# @login_required
# def secret():
#   return 'Only authenticated users are allowed!'

#  In this example, the secret() function will be protected against unauthorized users with login_required, and then the
#  resulting function will be registered with Flask as a route.

# Thanks to the login_required decorator, if this route is accessed by a user who is not authenticated, Flask-Login will
# intercept the request and send the user to the login page instead.

# The navigation bar in the base.html template uses a Jinja2 conditional to display “Log In” or “Log Out” links
# depending on the logged-in state of the current user. The conditional is shown in

# Example 8-10. app/templates/base.html: Log In and Log Out navigation bar links

# <ul class="nav navbar-nav navbar-right">
# {% if current_user.is_authenticated %}
# <li><a href="{{ url_for('auth.logout') }}">Log Out</a></li> {% else %}
# <li><a href="{{ url_for('auth.login') }}">Log In</a></li> {% endif %}
# </ul>

# The current_user variable used in the conditional is defined by Flask-Login and is automatically available to view
# functions and templates. This variable contains the currently logged-in user, or a proxy anonymous user object if the
# user is not logged in. Anonymous user objects have the is_authenticated property set to False

#                               Signing Users In
# To log a user in, the function begins by loading the user from the database using the email provided with the form. If
# a user with the given email address exists, then its verify_password() method is called with the password that also
# came with the form. If the password is valid, Flask-Login’s login_user() function is invoked to record the user as
# logged in for the user session. The login_user() function takes the user to log in and an optional “remember me”
# Boolean, which was also submitted with the form. A value of False for this argument causes the user session to expire
# when the browser window is closed, so the user will have to log in again next time. A value of True causes a long-term
# cookie to be set in the user’s browser, which Flask-Login uses to restore the user session. The optional
# REMEMBER_COOKIE_DURATION configuration option can be used to change the default one-year duration for the remember
# cookie.

# #
# from flask import render_template, redirect, request, url_for, flash
# from flask_login import login_user
# from . import auth
# from ..models import User
# from .forms import LoginForm

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#   form = LoginForm()
#   if form.validate_on_submit():
#       user = User.query.filter_by(email=form.email.data).first()
#       if user is not None and user.verify_password(form.password.data):
#           login_user(user, form.remember_me.data)
#           next = request.args.get('next')
#           if next is None or not next.startswith('/'):
#               next = url_for('main.index') return redirect(next)
#               flash('Invalid username or password.')
#    return render_template('auth/login.html', form=form)
#
# The login_user() function writes the ID of the user to the user session as a string.
# ____________________________________________________________________________________________________________________
#                         Signing Users Out
# ____________________________________________________________________________________________________________________

# from flask_login import logout_user, login_required
#
# @auth.route('/logout')
# @login_required
# def logout():
#   logout_user()
#   flash('You have been logged out.')
#   return redirect(url_for('main.index'))
#
# To log a user out, Flask-Login’s logout_user() function is called to remove and reset the user session. The logout is
# completed with a flash message that confirms the action and a redirect to the home page.

# b. During the rendering of the Jinja2 template, a reference to Flask-Login’s current_user appears for the first time.
# c. The current_user context variable does not have a value assigned for this request yet, so it invokes Flask-Login’s
# internal function _get_user() to find out who the user is.
#
#  username = StringField('Username', validators=[
#         DataRequired(), Length(1, 64),
#         Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#                'Usernames must have only letters, numbers, dots or '
#                'underscores')])

# <p>
# New user?
# <a href="{{ url_for('auth.register') }}"> Click here to register
# </a> </p>

# ____________________________________________________________________________________________________________________
#                           Account Confirmation
# ____________________________________________________________________________________________________________________

# To validate the email address, applications send a confirmation email to users immediately after they register. The
# new account is initially marked as unconfirmed until the instructions in the email are followed, which proves that the
# user has received the email. The account confirmation procedure usually involves clicking a specially crafted URL link
# that includes a confirmation token.

# The simplest account confirmation link would be a URL with the format http:// www.example.com/auth/confirm/<id>
# included in the confirmation email. The idea is to replace the <id> in the URL with a token that contains the same
# information, but in such a way that only the server can generate valid confirmation URLs.

# The user session cookies contain a cryptographic signature generated by a package called itsdangerous. If the
# contents of the user session is altered, the signature will not match the content anymore, so Flask discards the
# session and starts a new one. The same concept can be applied to confirmation tokens.

# The following is a short shell session that shows how itsdangerous can generate a signed token that contains a user
# id inside:
# (venv) $ flask shell
# >>> from itsdangerous import  URLSafeTimedSerializer as Serializer
# >>> s = Serializer(app.config['SECRET_KEY'], expires_in=3600)
# >>> token = s.dumps({ 'confirm': 23 })
# >>> token 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4MTcxODU1OCwiaWF0IjoxMzgxNzE0OTU4fQ.ey ...'
# >>> data = s.loads(token)
# >>> data
# {'confirm': 23}

# The itsdangerous package provides several types of token generators. Among them, the class URLSafeTimedSerializer
# generates JSON Web Signatures (JWSs) with a time expiration. The constructor of this class takes an encryption key as
# an argument, which in a Flask application can be the configured SECRET_KEY.

# The dumps() method generates a cryptographic signature for the data given as an argument and then serializes the data
# plus the signature as a convenient token string.
# To decode the token, the serializer object provides a loads() method that takes the token as its only argument.
# The function verifies the signature and the expiration time and, if both are valid, it returns the original data.
# When the loads() method is given an invalid token or a valid token that is expired, an exception is raised.

# Token generation and verification using this functionality can be added to the User model.

# from itsdangerous import URLSafeTimedSerializer as Serializer
# from flask import current_app
# from . import db
# class User(UserMixin, db.Model):
#      ...
#     confirmed = db.Column(db.Boolean, default=False)
#     def generate_confirmation_token(self):
#        s = Serializer(current_app.config['SECRET_KEY'])
#        return s.dumps({'confirm': self.id}).decode('utf-8')
#     def confirm(self, token):
#         s = Serializer(current_app.config['SECRET_KEY'])
#         try:
#               data = s.loads(token.encode('utf-8'))
#         except:
#             return False
#         if data.get('confirm') != self.id:
#             return False
#         self.confirmed = True
#          db.session.add(self)
#         return True

# The generate_confirmation_token() method generates a token with a default validity time of one hour. The confirm()
# method verifies the token and, if valid, sets the new confirmed attribute in the user model to True.
# In addition to verifying the token, the confirm() function checks that the id from the token matches the logged-in
# user, which is stored in current_user. This ensures that a confirmation token for a given user cannot be used to
# confirm a different user.
#
#                        Sending Confirmation Emails

# from ..email import send_email
# @auth.route('/register', methods=['GET', 'POST'])
# def register():
# form = RegistrationForm()
# if form.validate_on_submit():
# ...
#  db.session.add(user)
#  db.session.commit()
#  token = user.generate_confirmation_token()
#  send_email(user.email, 'Confirm Your Account','auth/email/confirm', user=user, token=token)
#  flash('A confirmation email has been sent to you by email.')
#       return redirect(url_for('main.index'))
# return render_template('auth/register.html', form=form)
# Note that a db.session.commit() call had to be added before the confirmation email is sent out. The problem is that
# new users get assigned an id when they are commit‐ ted to the database, and this id is needed to generate the
# confirmation token.
# The email templates used by the authentication blueprint will be added in the tem‐ plates/auth/email directory to keep
# them separate from the HTML templates. As dis‐ cussed in Chapter 6, for each email two templates are needed for the
# plain-text and HTML versions of the body.

# Dear {{ user.username }},
# Welcome to Flasky!
# To confirm your account please click on the following link:
# {{ url_for('auth.confirm', token=token, _external=True) }}
# Sincerely,
# The Flasky Team
# Note: replies to this email address are not monitored.

# By default, url_for() generates relative URLs; so, for example, url_for('auth.confirm', token='abc') returns the
# string '/auth/confirm/abc'. This, of course, is not a valid URL that can be sent in an email, since it is only the
# path portion of the URL. Relative URLs work fine when they are used within the con‐ text of a web page because the
# browser converts them to absolute URLs by adding the hostname and port number from the current page, but when sending
# a URL over email there is no such context. The _external=True argument is added to the url_for() call to request a
# fully qualified URL that includes the scheme (http:// or https://), hostname, and port.

# from flask_login import current_user
# @auth.route('/confirm/<token>') @login_required
# def confirm(token):
# if current_user.confirmed:
# return redirect(url_for('main.index'))
# if current_user.confirm(token):
# db.session.commit()
# flash('You have confirmed your account. Thanks!')
# else:
# flash('The confirmation link is invalid or has expired.')
# return redirect(url_for('main.index'))
# This route is protected with the login_required decorator from Flask-Login, so that when the users click on the link
# from the confirmation email they are asked to log in before they reach this view function.
# The function first checks if the logged-in user is already confirmed, and in that case it redirects to the home page,
# as obviously there is nothing to do. This can prevent unnecessary work if a user clicks the confirmation token
# multiple times by mistake.
# Because the actual token confirmation is done entirely in the User model, all the view function needs to do is call
# the confirm() method and then flash a message accord‐ ing to the result. When the confirmation succeeds, the User
# model’s confirmed attribute is changed and added to the session and then the database session is committed.
# Each application can decide what unconfirmed users are allowed to do before they confirm their accounts.
# One possibility is to allow unconfirmed users to log in, but only show them a page that asks them to confirm their
# accounts before they can gain further access.

# @auth.before_app_request
# def before_request():
#   if current_user.is_authenticated \
#   and not current_user.confirmed \ and request.blueprint != 'auth' \ and request.endpoint != 'static':
#   return redirect(url_for('auth.unconfirmed'))

# @auth.route('/unconfirmed') def unconfirmed():
#   if current_user.is_anonymous or current_user.confirmed: return redirect(url_for('main.index'))
#   return render_template('auth/unconfirmed.html')
#   The before_app_request handler will intercept a request when three conditions are true:
# 1. A user is logged in (current_user.is_authenticated is True).
# 2. The account for the user is not confirmed.
# 3. The requested URL is outside of the authentication blueprint and is not for a static file. Access to the
# authentication routes needs to be granted, as those are the routes that will enable the user to confirm the account or
# perform other account management functions.
# If these three conditions are met, then a redirect is issued to a new /auth/unconfirmed route that shows a page with
# information about account confirmation.

# The page that is presented to unconfirmed users (shown in Figure 8-4) just renders a template that gives users
# instructions for how to confirm their accounts and offers a link to request a new confirmation email, in case the
# original email was lost. The route that resends the confirmation email is shown in Example 8-23.



# Example 8-23. app/auth/views.py: resending the account confirmation email
# @auth.route('/confirm') @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email(current_user.email, 'Confirm Your Account',
#     'auth/email/confirm', user=current_user, token=token)
#     flash('A new confirmation email has been sent to you by email.')
#     return redirect(url_for('main.index'))
# This route repeats what was done in the registration route using current_user, the user who is logged in, as the
# target user. This route is also protected with login_required to ensure that when it is accessed, the user that is
# making the request is authenticated.

# ____________________________________________________________________________________________________________________
#                           make_response
# ____________________________________________________________________________________________________________________

# from flask import make_response
# @app.route('/')
# def index():
#     some =  render_template('index.html', index=True, current_time=datetime.utcnow())
#     # return render_template('index.html', index=True, current_time=datetime.utcnow())
#     res= make_response(some)
#     res.headers['Content-Type'] = 'text/plain'
#     return res

# @app.route('/')
# def index():
#     res = make_response('<h1>Server error</h1>', 500)

# @app.route('/')
# def index()
#     return <h1>Server error</h1> , 500 , {'Content-Type':'text/plain'}

# @app.before_first_request
# @app.before_request
# @app.after_request
# @app.teardown_request
#
# <script>
#     document.cookie="ex=1;";
#     if (!document.cookie)
#         {
#             alert("You need to turn on cookie")
#         }
# </script>

# set_cookie(key, value="", max_age=None)
# res.set_cookie("logged", 'yes')
#
#app.permanent_session_lifetime=datetime.timedelta(days=10)   point how many days keeps  session in browser
# session_permanent = True    session will keep in browser for 31 days, if not it will clean after close browser
# session.modified= True    we explicitly point that session changed

#