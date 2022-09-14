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

