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