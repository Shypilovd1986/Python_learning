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

#                                               Initialization
# All Flask applications must create an application instance. The web server passes all requests it receives from
# clients to this object for handling, using a protocol called Web Server Gateway Interface
# (WSGI, pronounced “wiz-ghee”). The application instance is an object of class Flask, usually created as follows:

# from flask import Flask
# app = Flask(__name__)

# The only required argument to the Flask class constructor is the name of the main module or package of the application
# For most applications, Python’s __name__ vari‐ able is the correct value for this argument.

#                                           Routes and View Functions
# Clients such as web browsers send requests to the web server, which in turn sends them to the Flask application
# instance. The Flask application instance needs to know what code it needs to run for each URL requested, so it keeps
# a mapping of URLs to Python functions. The association between a URL and the function that handles it is called
# a route.

# The previous example registers function index() as the handler for the application’s root URL. While the app.route
# decorator is the preferred method to register view functions, Flask also offers a more traditional way to set up the
# application routes with the app.add_url_rule() method, which in its most basic form takes three argu‐ ments: the URL,
# the endpoint name, and the view function. The following example uses app.add_url_rule() to register an index()
# function that is equivalent to the one shown previously:
# def index():
#   return '<h1>Hello World!</h1>'
# app.add_url_rule('/', 'index', index)

# If you pay attention to how some URLs for services that you use every day are formed, you will notice that many have
# variable sections. For example, the URL for your Facebook profile page has the format
# https://www.facebook.com/<your-name>, which includes your username, making it different for each user. Flask supports
# these types of URLs using a special syntax in the app.route decorator. The following exam‐ ple defines a route that
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

#                           Development Web Server
# Flask applications include a development web server that can be started with the flask run command. This command looks
# for the name of the Python script that contains the application instance in the FLASK_APP environment variable.
# To start the hello.py application from the previous section, first make sure the virtual environment you created
# earlier is activated and has Flask installed in it. For Linux and macOS users, start the web server as follows:
# (venv) $ export FLASK_APP=hello.py
# (venv) $ flask run
#      * Serving Flask app "hello"
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# For Microsoft Windows users, the only difference is in how the FLASK_APP environ‐ ment variable is set:
# (venv) $ set FLASK_APP=hello.py
# (venv) $ flask run

# The web server provided by Flask is intended to be used only for development and testing.

# The Flask development web server can also be started program‐ matically by invoking the app.run() method. Older
# versions of Flask that did not have the flask command required the server to be started by running the application’s
# main script, which had to include the following snippet at the end:

# if __name__ == '__main__':
#   app.run()

# While the flask run command makes this practice unnecessary, the app.run() method can still be useful on certain
# occasions

#                                           Debug Mode
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
# If you are using Microsoft Windows, use set instead of export to set the environ‐ ment variables.

#                                   Command-Line Options
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

# The --host argument is particularly useful because it tells the web server what net‐ work interface to listen to for
# connections from clients. By default, Flask’s develop‐ ment web server listens for connections on localhost, so only
# connections originating from the computer running the server are accepted. The following command makes the web server
# listen for connections on the public network interface, enabling other computers in the same network to connect as
# well:
# (venv) $ flask run --host 0.0.0.0
# * Serving Flask app "hello"
# * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

#                       Application and Request Contexts
# When Flask receives a request from a client, it needs to make a few objects available to the view function that will
# handle it. A good example is the request object, which encapsulates the HTTP request sent by the client.
#
# Variable name            Context                Description
# current_app      Application context    The application instance for the active application.
# g                Application context    An object that the application can use for temporary storage during the
#                                         handling of a request. This variable is reset with each request.
# request          Request context        The request object, which encapsulates the contents of an HTTP request sent by
#                                         the client.
# session          Request context        The user session, a dictionary that the application can use to store values
#                                         that are “remembered” between requests.

# from flask import request
# @app.route('/')
# def index():
#   user_agent = request.headers.get('User-Agent')
#   return '<p>Your browser is {}</p>'.format(user_agent)

# Note how in this view function, request is used as if it were a global variable. In real‐ ity, request cannot be a
# global variable; in a multithreaded server several threads can be working on different requests from different clients
# all at the same time, so each thread needs to see a different object in request. Contexts enable Flask to make
# cer‐ tain variables globally accessible to a thread without interfering with the other threads.

# A thread is the smallest sequence of instructions that can be man‐ aged independently. It is common for a process to
# have multiple active threads, sometimes sharing resources such as memory or file handles. Multithreaded web servers
# start a pool of threads and select a thread from the pool to handle each incoming request.

# There are two contexts in Flask: the application context and the request context.

#                                            The Request Object
# You have seen that Flask exposes a request object as a context variable named request. This is an extremely useful
# object that contains all the information that the client included in the HTTP request. Table 2-2 enumerates the most
# commonly used attributes and methods of the Flask request object.
#                       Table 2-2. Flask request object
#                             Attribute or Method
# form           A dictionary with all the form fields submitted with the request.
# args           A dictionary with all the arguments passed in the query string of the URL.
# values         A dictionary that combines the values informandargs.
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

#                                           Request Hooks
# Sometimes it is useful to execute code before or after each request is processed. For example, at the start of each
# request it may be necessary to create a database connec‐ tion or authenticate the user making the request. Instead of
# duplicating the code that performs these actions in every view function, Flask gives you the option to register common
# functions to be invoked before or after a request is dispatched.

# Request hooks are implemented as decorators. These are the four hooks supported by Flask:
# before_request
# Registers a function to run before each request.

# before_first_request
# Registers a function to run only before the first request is handled. This can be a convenient way to add server
# initialization tasks.

# after_request
# Registers a function to run after each request, but only if no unhandled excep‐ tions occurred.

# teardown_request
# Registers a function to run after each request, even if unhandled exceptions occurred.

# A common pattern to share data between request hook functions and view functions is to use the g context global as
# storage. For example, a before_request handler can load the logged-in user from the database and store it in g.user.
# Later, when the view function is invoked, it can retrieve the user from there.

#                                                   Responses
# When Flask invokes a view function, it expects its return value to be the response to the request. In most cases the
# response is a simple string that is sent back to the client as an HTML page.
# But the HTTP protocol requires more than a string as a response to a request. A very important part of the HTTP
# response is the status code, which Flask by default sets to 200, the code that indicates that the request was carried
# out successfully.
# When a view function needs to respond with a different status code, it can add the numeric code as a second return
# value after the response text. For example, the fol‐ lowing view function returns a 400 status code, the code for a
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

# xxxxxxxxxxxx  Templates   xxxxxxxxxx

# Variables can be modified with filters, which are added after the variable name with a pipe character as separator.
# For example, the following template shows the name vari‐ able capitalized:
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

#                                       Control Structures
# Jinja2 offers several control structures that can be used to alter the flow of the tem‐ plate. This section introduces
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
#         {% for comment in comments %}
# <li>{{ comment }}</li> {% endfor %}
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
# <title>{% block title %}{% endblock %} - My Application</title> {% endblock %}
#     </head>
#     <body>
#         {% block body %}
#         {% endblock %}
#     </body>
#     </html>
# Base templates define blocks that can be overridden by derived templates. The Jinja2 block and endblock directives
# define blocks of content that are added to the base template. In this example, there are blocks called head, title,
# and body; note that title is contained by head. The following example is a derived template of the base template:

#
#   xxxxxxxxxxxx                flask_moment          xxxxxxxxxx
#
# Localization of Dates and Times with Flask-Moment
# pip install flask-moment
#
# from flask_moment import Moment moment = Moment(app)

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
# Consult the Moment.js documen‐ tation to learn about all the formatting options offered by this library.

# The timestamps rendered by Flask-Moment can be localized to many languages. A language can be selected in the template
# by passing the two-letter language code to function locale(), right after the Moment.js library is included.
# For example, here is how to configure Moment.js to use Spanish:
#     {% block scripts %}
#     {{ super() }}
#     {{ moment.include_moment() }}
#     {{ moment.locale('es') }}
#     {% endblock %}

#
# xxxxxxxxxx      Static Files       xxxxxxxxxx

# You may recall that when the hello.py application’s URL map was inspected in Chap‐ ter 2, a static entry appeared in
# it. Flask automatically supports static files by adding a special route to the application defined a
# s /static/<filename>. For example, a call to url_for('static', filename='css/styles.css', _external=True) would return
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


#                               Web Forms
#                   xxxxxxxxx      flask-WTF     xxxxxxxxxx
#                             Configuration
# The Flask-WTF extension makes working with web forms a much more pleasant experience. This extension is a Flask
# integration wrapper around the framework- agnostic WTForms package.
# Flask-WTF and its dependencies can be installed with pip:
# (venv) $ pip install flask-wtf

# Unlike most other extensions, Flask-WTF does not need to be initialized at the appli‐ cation level, but it expects
# the application to have a secret key configured. A secret key is a string with any random and unique content that is
# used as an encryption or sign‐ ing key to improve the security of the application in several ways. Flask uses this key
# to protect the contents of the user session against tampering. You should pick a dif‐ ferent secret key in each
# application that you build and make sure that this string is not known by anyone.

# The app.config dictionary is a general-purpose place to store configuration variables used by Flask, extensions, or
# the application itself. Configuration values can be added to the app.config object using standard dictionary syntax.
# The configuration object also has methods to import configuration values from files or the environment.

# lask-WTF requires a secret key to be configured in the application because this key is part of the mechanism the
# extension uses to protect all forms against cross-site request forgery (CSRF) attacks. A CSRF attack occurs when a
# malicious website sends requests to the application server on which the user is currently logged in. Flask-WTF
# generates security tokens for all forms and stores them in the user session, which is protected with a cryptographic
# signature generated from the secret key.

#                               Form Classes
# When using Flask-WTF, each web form is represented in the server by a class that inherits from the class FlaskForm.
# The class defines the list of fields in the form, each represented by an object. Each field object can have one or
# more validators attached. A validator is a function that checks whether the data submitted by the user is valid.

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField from wtforms.validators import DataRequired
# class NameForm(FlaskForm):
# name = StringField('What is your name?',
# validators=[DataRequired()]) submit = SubmitField('Submit')

# The fields in the form are defined as class variables, and each class variable is assigned an object associated with
# the field type.

# The optional validators argument included in the StringField constructor defines a list of checkers that will be
# applied to the data submitted by the user before it is accepted. The DataRequired() validator ensures that the field
# is not submitted empty.

# The FlaskForm base class is defined by the Flask-WTF extension, so it is imported from flask_wtf. The fields and
# validators, how‐ ever, are imported directly from the WTForms package.

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

# we need install extension : pip install email-validator   for working with Email validator
#
#                       HTML Rendering of Forms

# <form method="POST">
# {{ form.hidden_tag() }}
# {{ form.name.label }} {{ form.name() }} {{ form.submit() }}
# </form>

# Note that in addition to the name and submit fields, the form has a form.hidden_tag() element. This element defines an
# extra form field that is hidden, used by Flask-WTF to implement CSRF protection.

#                   Form Handling in View Functions

# @app.route('/', methods=['GET', 'POST']) def index():
# name = None
# form = NameForm()
# if form.validate_on_submit():
#         name = form.name.data
# form.name.data = ''
# return render_template('index.html', form=form, name=name)

# The validate_on_submit() method of the form returns True when the form was submitted and the data was accepted by all
# the field validators. In all other cases, validate_on_submit() returns False. The return value of this method
# effectively serves to determine whether the form needs to be rendered or processed.

#                           Redirects and User Sessions

# it is considered good practice for web applications to never leave a POST request as the last request sent by the
# browser.
# This is achieved by responding to POST requests with a redirect instead of a normal response. A redirect is a special
# type of response that contains a URL instead of a string with HTML code. it issues a GET request for the redirect URL,
# and that is the page that it displays.
#
# Applications can “remember” things from one request to the next by storing them in the user session, a private storage
# that is available to each connected client.

# from flask import Flask, render_template, session, redirect, url_for
# @app.route('/', methods=['GET', 'POST']) def index():
# form = NameForm()
# if form.validate_on_submit():
#         session['name'] = form.name.data
# return redirect(url_for('index'))
# return render_template('index.html', form=form, name=session.get('name'))

# The redirect() function takes the URL to redirect to as an argument.
# The first and only required argument to url_for() is the endpoint name, the internal name each route has.

#                               Message Flashing

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

#                   Databases

# called SQL databases in reference to the Structured Query Language they use. But in recent years document-oriented and
# key-value databases, informally known together as NoSQL databases

# Relational databases store data in tables,
# A table has a fixed number of columns and a variable number of rows.
# This graphical style of representing the structure of a database is called an entity- relationship diagram.

# Databases that do not follow the relational model described in the previous section are collectively referred to as
# NoSQL databases. One common organization for NoSQL databases uses collections instead of tables and documents instead
# of records. NoSQL databases are designed in a way that makes joins difficult, so most of them do not support this
# operation at all. A more appropriate design for a NoSQL database is shown in Figure 5-2. This is the result of
# applying an operation called denormalization, which reduces the number of tables at the expense of data duplication.

# ACID, which stands for Atomicity, Consis‐ tency, Isolation, and Durability. NoSQL databases relax some of the ACID
# require‐ ments and as a result can sometimes get a performance edge.

# there are also a number of database abstraction layer packages, such as SQLAlchemy or MongoEngine, that allow you to
# work at a higher level with regular Python objects instead of database entities such as tables, documents, or query
# languages.

# When comparing straight database engines to database abstraction layers, the second group clearly wins. Abstraction
# layers, also called object-relational map‐ pers (ORMs) or object-document mappers (ODMs), provide transparent
# conver‐ sion of high-level object-oriented operations into low-level database instructions.

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
# object. The Flask-SQLAlchemy documentation also suggests setting key SQLALCHEMY_TRACK_MODIFICATIONS to False to use
# less memory unless signals for object changes are needed.

# import os
# from flask_sqlalchemy import SQLAlchemy
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__) app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# The term model is used when referring to the persistent entities used by the applica‐ tion. In the context of an ORM,
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
# attribute can be used, even though it is not a real data‐ base column but a high-level representation of the
# one-to-many relationship. The id attribute of these new objects is not set explicitly: the primary keys in many
# databases are managed by the database itself. The objects exist only on the Python side so far; they have not been
# written to the database yet. Because of that, their id values have not yet been assigned:
# >>> print(admin_role.id) None

# Changes to the database are managed through a database session, which Flask- SQLAlchemy provides as db.session.
# To prepare objects to be written to the data‐ base, they must be added to the session:
# >>> db.session.add(admin_role)

# Or, more concisely:
# >>> db.session.add_all([admin_role, mod_role, user_role, ... user_john, user_susan, user_david])

# To write the objects to the database, the session needs to be committed by calling its commit() method:
# >>> db.session.commit()

# The db.session database session is not related to the Flask session object discussed in Chapter 4. Database sessions
# are also called transactions.

# Database sessions are extremely useful in keeping the database consistent. The com‐ mit operation writes all the
# objects that were added to the session atomically. if an error occurs while the session is being written, the whole
# session is discarded.

# A database session can also be rolled back. If db.session.rollback() is called, any objects that were added to the
# database session are restored to the state they have in the data‐ base.

#                    Modifying Rows
# The add() method of the database session can also be used to update models. Con‐ tinuing in the same shell session,
# the following example renames the "Admin" role to "Administrator":
# >>> admin_role.name = 'Administrator' >>> db.session.add(admin_role)
# >>> db.session.commit()
#                   Deleting Rows
# The database session also has a delete() method. The following example deletes the "Moderator" role from the database:
# >>> db.session.delete(mod_role) >>> db.session.commit()
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

#                           Table 5-5. Common SQLAlchemy query filters
# filter()          Returns a new query that adds an additional filter to the original query
# filter_by()       Returns a new query that adds an additional equality filter to the original query
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

#                   Integration with the Python Shell

# To add objects to the import list, a shell context processor must be created and registered with the
# app.shell_context_processor decorator.

# @app.shell_context_processor
# def make_shell_context():
#   return dict(db=db, User=User, Role=Role)

# The shell context processor function returns a dictionary that includes the database instance and the models. The
# flask shell command will import these items auto‐ matically into the shell, in addition to app, which is imported by
# default:
# $ flask shell
# >>> app
# <Flask 'hello'>
# >>> db
# <SQLAlchemy engine='sqlite:////home/flask/flasky/data.sqlite'>

#                   Database Migrations with Flask-Migrate

# only way to make it update tables is by destroying the old tables
# A better solution is to use a database migration framework.
# Flask applications can use the Flask-Migrate extension
# pip install flask-migrate

# from flask_migrate import Migrate # ...
# migrate = Migrate(app, db)
# To expose the database migration commands, Flask-Migrate adds a flask db com‐ mand with several subcommands. When you
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

#                       Email Support with Flask-Mail

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

#