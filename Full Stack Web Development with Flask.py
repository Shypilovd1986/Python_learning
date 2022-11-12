#                    Configuring Flask

#  So I'm going to use the venv which is a module that is packaged along with Python. And that's by using this command
#  called py-m for the module and the module name is venv, and the next parameter here is just the name of the folder or
#  that environment you want to call it. You can call whatever you want. It's very common to call it the same name, some
#  people just call it env like that. Okay, which way is entirely up to you.

# python3 -m venv venv
# we should activate virtual environment by command    source venv/bin/activate

# python3 install flask-wtf
#  So, we also need to install one more package the WTF, so let me just clear this for now. And again, just pip install
#  and then flask-wtf. And that will install the form module for us. So later on when we create our forms, we can use
#  that to create it for us very, very quickly.

# In folder venv create a file called .flaskenv and hit enter. Okay, this is an environment file, where you can actually
# set a key value pair for some environment variables. Now this option was not available in the previous version of
# Flask after version one for now we have this option, this capability, so it's pretty handy. In here, I'm just going to
# create two variables that we'll use. And the first one is called FLASK_, all caps, ENV for the environment and move to
# set that to the development environment. Now in the previous version, it was defaulted to this development environment
# But version one is defaulted to the production environment. So, when you run your application, you want to run in a
# development environment. And this is why you will set up inside this file. The second variable is called the FlASK_APP
# And this is the starting point of our application. So, I'm going to call my main.py. Okay, you can call it whatever
# you want, but this is the main entry to our application. And I don't have it yet, but we will create that later on. So
# these are the two variables I will create for this one for now. And if you do need to add more later on, you can
# always come back and add it in. So save the file.
#                       .flaskenv
# FLASK_ENV=development
# FLASK_APP=main.py

#  And then one more thing that we need to do is that in order to run these variables here, you also need a special
#  package to invoke with this. If you don't install the package, it's not going to let you do it. So let me clear this
#  screen down here in the bottom, and we need to install a package called python-dotenv.
#  pip3 install python-dotenv   !!!!!!!!!
#  And you can check to see
#  if you already have in here. So just type in the more pip list, and then you can see the list here. If you do have it
#  then it should say Python-dotenv. I don't have it, so I need to install that. So let's install that by issuing the
#  command pip install Python-dot for dotenv. Hit Enter and that's going to install the package for us. And if you list
#  that again, it should be in there now. Okay, so this is the one that we want. This one will allow us to invoke this
# environment variables. Okay, it's prompting this message here should upgrade my pip, so I'm going to do that right now
# just in case. And I think we should be good to go. So now once you are done with the environment, you also want to
# deactivate the environment and to do that anywhere in your code, you just issue the command deactivate. And that
# should be moved that green color on the left side again you can see that now we're outside of the environment and we
# are done at this point. So in the next video, we will create and run our first simple Flask application.

#  before we run that though, I want to make sure that we preserve all these packages in a safe file, just in case if we
# do need to reinstall or if you do move these data or this application to another system, you can reinstall that easily
# And that's why I created this file called requirements dot TXT, which is special file very similar to the package.json
# file, if you are familiar with Node.js application development.

# pip3 freeze > requirements.txt
# pip3 install requirements.txt

# !!!!!!!      every dot Py file is considered a module in Flask

#                                           Creating and running a simple Flask application
#
# Selecting transcript lines in this section will navigate to timestamp in the video
# . And so right in here we going to create a file called main dot Py and some people call it differently. Again, it
# doesn't matter what you call it. I would treat this as the main entry to our application.

# And you do that by issuing this command called from Flask. import the Flask class.
# And now we need to instantiate object and is typical to have the variable called app, and then we going to assign that
# to the Flask class. Want to pass in the underscore name, underscore variable that is a special variable name to
# identify the current application or module that is being rendered or passed to Flask

# And then now, we are going to create a simple route to run the application. That is by issuing this command both S
# symbol followed by the app and then route. The forward slash, that is the forward slash in the URL. That is the root
# directory if you want that to be the root directory. And then you can also add another one if you want app dot route,
# same index or home or whatever. You can have different types of URLs. These are called decorators.

# They decorate the underlying definition or function and this function can be called anything you want, usually index
# or home or default, whatever that is. That means if I go to browser, if I take the forward slash and our domain, it
# will load this function and whatever is inside here will be rendered.

#                           main.py
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return '<h1>Hallo world</h2>'

# flask run     to run development server
#
# xxxxxxxxxx        Creating the enrollment application            xxxxxxxxxxxxxxxxx

# Okay, so we're going to create a application package. Now, a package is just nothing more than a directory inside this
#  project. Some people prefer to call it just app, or I can call it the name of your actual application, which is fine,
# and the reason why I do this is because you don't want to put all your files in the rule directory. And so, what we'll
# do is that we will modify this main py module to link or load all the files inside this application folder, if you are
# a new JS developer. If you are familiar with other frameworks, that's Angular, and Vue, and React and so on. You see
# that it follows a very similar structure. You have a main file main entry application file that links to the
# underlying application inside the folder here. Okay, so in here then, I'm going to create a file called __init__.py.
# And this is the initial file that it's like a default, like an index that JS file if you're familiar with Angular and
# Vue, JS and so forth. So you will look into that file for any initialization of the file and so on. So, eventually
# we're going to move the app module, I mean the app object into this file. And then at the same time, I'm going to go
# and create two more folders and this one is called templates.

# And then at the same time, I'm going to go and create two more folders and this one is called templates. This is to
# house all of our templates, like HTML templates, basically. And I'm going to create another one called static. Okay,
# static is used for storing static data, like images and audio and videos, or any of the JavaScript files on CSS and so
# forth, okay? Anything that it's not generated dynamically will be stored in that directory.

# So, I'll into the main file here, open that up, and I'm going to copy everything here and move all of these into the
# init file. and in the main,py file
# from application import app
#
#  And if you want, you can go into the static here, and create some more folders. I can go ahead and create two more.
#  Maybe I'll call it images. And then one more for CSS. And just in case, if you do want to add some CSS, or other
#  JavaScript in here, you can always go back and add it in here


# xxxxxxxxxxx        Running and configuring the development server         xxxxxxxxxxxxx

#  to take a look at creating a config file, which is the configuration module to store some major configurations that
#  we use across the application. We'll also be creating a route py module file to store all the routing patterns in our
#  application. And then we'll need to also modify the init file to reflect these changes in the application. So let's
#  go and see how this is done.

# creating config.py module
# creating routes.py module
#
#                       config.py
# import os
# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_string'
#

#                   application/routes.py
# from application import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return '<h1>Hallo world</h2>'

#                    __init__.py
# from flask import Flask
#
# app = Flask(__name__)
#
# from application import routes


# xxxxxxxxxxxxxx      Creating the homepage        xxxxxxxxxxxxxx

# Creating the home page. In this video, we're going to create a template to store our home page, the landing page of
# our application. We'll call it the index.html, and also we'll be importing or calling the render_template function
# from the Flask module to render these templates to the browser. We'll be using the Jinja template expression to create
# code blocks and set our templates, and also, we're using in the include directory of to include any external files, so
# let's go into the code and see how this is done, so here in the application, we have the main.py file. This is the
# main entry point.

# Configuration is still here. In the application folder we have the __init__.py, and then here we have imported the
# routing from the routes.py. Okay, so when we run the application, it renders this text to the browser, and that's what
# we saw in the other video, so now, instead of having to put the text here inside this string here

#                           templates/index.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>UTA - Home Page</title>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
#           integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <link rel="stylesheet" href="static/css/main.css"/>
# </head>
# <body>
#
# <div class="container-fluid text-center top-container">
#     <img src="static/images/uta-logo-200.png">
# </div>
# <div class="container">
#
#     <div class="row">
#         <div class="col-md-12 text-center">
#             <h1>Welcome to Universal Tech Academy.</h1>
#             <h3>Let's get started.</h3>
#             <p>Already registered? <a href='login.html'>Login</a></p>
#             </div>
#     </div>
# </div>
#
# {% include "includes/footer.html" %}
# </body>
# </html>

#               templates/includes/footer.html
# <div class="container-fluid text-center bottom-container">
#     <footer>
#         <p>Copyright &copy;2019-2020. Universal Tech Academy. All rights reserved.</p>
#     </footer>
# </div>

# xxxxxxxxxxxxx           Creating navigation links and route patterns          xxxxxxxxxxxxxxxxxxx

#  And we'll do that by using something called a URL for function to resolve links. We'll also be exploring the route
#  decorator to bind a function to one or more URL patterns on the website

#  will also look at a few of the Jinja delimiters, the statements, expressions and the comments.
#                   jinja delimiters
# {% ... %}  statements
# {{ ... }}  expressions
# {# ... #}  comments


#  add variable to route , and we use it in jinja statements
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html', login = True)

# <div class="row">
#         <div class="col-md-12 text-center">
#             <h1>Welcome to Universal Tech Academy.</h1>
#             {% if login %}
#             <h3>Let's get started.</h3>
#             {% else %}
#             <p>Already registered? <a href="{{ url_for('login') }}">Login</a></p>
#             {% endif %}
#             </div>
#     </div>

# xxxxxxxxx          Creating the base template           xxxxxxxxxxxxx

# Create what is called a base template. layout.html in folder templates
# cut from the index.html common information for all files.html and paste into the file layout.html

# <!DOCTYPE html>
# <html>
# <head>
#     <title>UTA - Home Page</title>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
#           integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <link rel="stylesheet" href="static/css/main.css"/>
# </head>
# <body>
#
# <div class="container-fluid text-center top-container">
#     <img src="static/images/uta-logo-200.png">
# </div>
# <div class="container">
#
#     {% include "includes/nav.html" %}
#
#     {% block content  %}
#
#     {% endblock content %}
#      if we use method {{ self.content() }}  it will duplicate code of block content  !!!!!!
#
# </div>
#
#     {% include "includes/footer.html" %}
# </body>
# </html>

#            in the file index.html paste

# {% extends "layout.html" %}
# {% block content %}
# {% endblock content %}

#                   index.ntml
# {% extends "layout.html" %}
#
# {% block content %}
#     <div class="row">
#         <div class="col-md-12 text-center">
#             <h1>Welcome to Universal Tech Academy.</h1>
#             {% if login %}
#             <h3>Let's get started.</h3>
#             {% else %}
#             <p>Already registered? <a href="{{ url_for('login') }}">Login</a></p>
#             {% endif %}
#         </div>
#     </div>
#
# {% endblock %}

# xxxxxxxxxx        Creating child templates         xxxxxxxxxxxxxxx

# layout.html is a base template, and index.html is a child template

# xxxxxxxxxxxxx     Passing data to the view          xxxxxxxxxxxxxx

# @app.route('/courses/<term>')
# def courses(term="2019"):
#     courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}
#     , {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"},
#     {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"},
#     {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"},
#     {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]
#     return render_template('courses.html', courseData = courseData, courses = True, term=term)

# xxxxxxxxxxx      Working with the GET method          xxxxxxxxxxxx

# @app.route('/enrollment')
# def enrollment():
#     id = request.args.get('courseID')
#     title = request.args.get('title')
#     term = request.args.get('term')
#     return render_template('enrollment.html', enrollment=True, data={"id": id, "title": title, "term": term})

#  <tr>
#                <td scope='row'>{{ data['courseID'] }}</td>
#                <td>{{ data['title'] }}</td>
#                <td>{{ data['description'] }}</td>
#                <td>{{ data['credits'] }}</td>
#                <td>{{ data['term'] }}</td>
#                <td>
#                    <form action="{{url_for('enrollment')}}" method="GET" >
#                        <input type="hidden" name="courseID" value="{{data['courseID']}}">
#                        <input type="hidden" name="title" value="{{data['title']}}">
#                        <input type="hidden" name="term" value="{{data['term']}}">
#                        <button>Enroll</button>
#                    </form>
#
#                </td>
#            </tr>

#                   create enrollment.html
# {% extends "layout.html" %}
#
# {% block content %}
#     <div class="row">
#         <div class="col-md-12 text-center">
#             <h1>You are enrolled in </h1>
#             <p>Course ID: {{data.id}}</p>
#             <p>Course Title: {{data.title}}</p>
#             <p>Course Term: {{data.term}}</p>
#         </div>
#     </div>
#
# {% endblock %}


# XXXXXXXXXXXXXXX     Working with the POST method     XXXXXXXXXXXXX

# - Working with the POST method. In this video, we are going to take a look at updating the enrollment form using POST
# method, adding the GET and POST methods to the route, and accessing form data using the form object, so let's go and
# take a look.

#
# @app.route('/enrollment', methods=["GET", "POST"])
# def enrollment():
#     id = request.form.get('courseID')
#     title = request.form.get('title')
#     term = request.form.get('term')
#     return render_template('enrollment.html', enrollment=True, data={"id": id, "title": title, "term": term})


#  <form action="{{url_for('enrollment')}}" method="POST" >
#                        <input type="hidden" name="courseID" value="{{data['courseID']}}">
#                        <input type="hidden" name="title" value="{{data['title']}}">
#                        <input type="hidden" name="term" value="{{data['term']}}">
#                        <button>Enroll</button>
#                    </form>

#
# xxxxxxxxxxxxx     Sending a JSON response        xxxxxxxxxxxxxxxx

#  Okay so that is the case, then now we are going to just return the response, okay. And this one takes about six
#  parameters, but we're just interested in maybe just one or two of those and the first parameter is going to be the
#  response object. And this is typical because when you do an Ajax call you always get a response object back and that
#  response is the one that contains the data itself. So here it will contain the jdata, okay. And we want to make sure
#  that jdata has to be in JSON data. So you want to wrap that with the JSON dumps. We're going to dump it as JSON data.
#  And then the other parameter here is the mimetype. And we'll use the application dash JSON, and we can just use those
#  two, that should be fine. You can use another one called the content type and use that application JSON or whatever
#  other type and be. But I think that should be enough.

# from flask import render_template, url_for, request, Response, json

# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx=None):
#     if idx==None:
#         jdata = courseData
#     else:
#         jdata = courseData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="application/json")

# xxxxxxxxx       working with database mongodb    xxxxxxxxxxxxxx

# pip install flask-mongoengine       This is the Flask Mongo engine

#               Setting up the database

# NONGODB_SETTINGS={'db' : 'UTA_Enrollment'}  setting up a Mongodb database
# from flask_mongoengine import Mongoenging   importing Mongoengine
# db=Mongoengine()              initializing the database object
# db.init_app(app)

#                   __init__
# from flask import Flask
# from config import Config
# from flask_mongoengine import MongoEngine
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
# db=Mongoengine()
# db.init_app(app)
#
# from application import routes

#               config
# import os
#
# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
#
#     NONGODB_SETTINGS = {'db': 'UTA_Enrollment'}

#  So, now, let's go to the very bottom and create our class. This is the class of users so I'm going to call it class
#  User, again, by convention is always capitalized using the camel case right here. And then I'm going to pass into
#  this function a db document. And this is a document because it's a document object, and, also, because you're using
#  the flask MongoDB engine, it's going to allow us to use the WTF form directives to create those field like string
#  fields and text fields and then Boolean fields, and so on, and so very helpful.

# class User(db.Document):
#     user_id = db.IntField(unique=True)
#     first_name = db.StringField(max_lenght=50)
#     last_name = db.StringField(max_lenght=50)
#     email = db.StringField(unique=True, maxlenght=40)
#     password = db.StringField(max_lenght=50)

#  Okay, so now, we need to create a route for this user so that we can run and display on the browser.

# . And every time we do this, just make sure you attach at the end with the .save. You need to save it to the database,
# so I almost forgot that, just make sure. I mean you can forget that very easily. And then, now, we're going to get the
# data back to a users variable. And it's going to be from the user.objects.all. That means it's going to return
# everything from this collection called user, and pass it to this object called users. And then we're going to return
# the render template.

#
# @app.route("/user")
# def user():
#      # User(user_id=3, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
#      # User(user_id=4, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
#      users = User.objects.all()
#      return render_template("user.html", users=users)

#                           user.html
# {% extends "layout.html" %}
#
# {% block content %}
#     <div class="row">
#         <div class="col-md-12 text-center">
#
#             {% for user in users %}
#             <dl>
#                 <dt>User ID: {{ user.user_id}}</dt>
#                 <dd>Email: {{user.email}}</dd>
#                 <dd>Password: {{user.password}}</dd>
#             </dl>
#             {% else %}
#
#                 <h3>No users yet!</h3>
#             {% endfor %}
#
#         </div>
#     </div>
# {% endblock %}

#                           Creating documents and data

# mongoimport --jsonArray --db UTA_Enrollment --collection user --file users.json          import to db

#                           Creating the data models

#  We need to create a models module instead of creating inside the routes.
# Create models.py in folder application

# from application import db
# import flask
#
# class User(db.Document):
#     user_id     =   db.IntField(unique=True)
#     first_name  =   db.StringField( max_length=50 )
#     last_name   =   db.StringField( max_length=50 )
#     email       =   db.StringField( max_length=30 )
#     password    =   db.StringField( max_length=30 )
#
# class Course(db.Document):
#     course_id   =   db.StringField(unique=True, max_length=20)
#     title       =   db.StringField( max_length=50 )
#     description =   db.StringField( max_length=200 )
#     credits     =   db.IntField()
#     term            =   db.StringField( max_length=30 )
#
# class Enrollment(db.Document):
#     user_id     =   db.IntField()
#     course_id   =   db.StringField(max_length=20)

#                       in routes.py
# from application.models import User, Course, Enrollment

#
#  So before we start, we want to look at these two extensions and see what they are. So the first one is the Flask-WTF
#  extension. This is an extension to the WTForms library. This is a library of modules that allow us to create very
#  clean HTML form fields. So, you don't have to do a lot of coding using this module. And another special feature about
#  this extension of this form, is that it maintains a separation of code in presentation. This is similar to something
# called the MVC, if you're not familiar with that, that's what it is, you separate the code from the view and also from
# the controller, so this is a, example of that.

#  This is in the Jinja's template system. So, you just basically, you know, issue a command using the dot notation to,
#  this form template here, and then the WTForm extension will actually process these, apart these and then render this
#  into the browser and you will see something like that in its finished state.

# <form >
#   {{ form.hidden_tag() }}
# </form>

# . This one here is a very special function that allows you to, generate something like this. On the right side, you
# can see this one here, is what's called a CSRF token. This is a cross site request forging system that actually allows
# you to make sure that the form that you're submitting to your site is very secure. It comes from your form and your
# form only, right? If you are, a .net developer, this is also very common in many other frameworks. You'll see that
# it's also included in those frameworks as well. Just to verify your site, making sure that it's coming from your form.
# So you'll see that there is a value, it's a long string of hash key values.

# pip install flask-security
# The next one is the Flask-Security extension. This is a extension that provides a few other modules to comment on what
# that. And, so things like, basic, session authentication, password hashing, and also the HTTP and token-based
# authentications are also part of the security extension. And two very important ones are the user registration and
# login tracking, which is another extension called the Flask-Login, that will come with this security extension

# xxxxxxxxxxxx        Updating the login route and login template      xxxxxxxxxx

#                                       login.html
#     {% extends "layout.html" %}
#
#     {% block content %}
#     <h1>{{ title }}</h1>
#
#     <div class="row">
#         <div class="col-md-6 offset-md-3">
#             <h3></h3>
#             <form name="login" action="" method="post">
#                 {{ form.hidden_tag() }}  <!-- this will create that CSRF token to secure our form -->
#
#                 <p>
#                     {{ form.email.label }}<br>
#                     {{ form.email(size=35) }}
#                 </p>
#
#                 <p>
#                     {{ form.password.label }}<br>
#                     {{ form.password(size=15) }}
#                 </p>
#
#                 <p>
#                     {{ form.submit() }}
#                 </p>
#
#             </form>
#         </div>
#     </div>
#  {% endblock %}
#
#                           routes.py
#
# from application.forms import LoginForm, RegisterForm

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template("login.html", title= "Login", form=form, login=True )


# xxxxxxxxxxxxxx       Flashing messages      xxxxxxxxxxxxx

# get the flashed_messages, okay special function that stores key facts of all the flashed messages that come to this
# page basically.

# n here, when we pass the flash message, we also have another option here is to pass the category. And the second field
# is a category. We can say if you're using Bootstrap, there's the success, the danger, and the warning messages. If
# it's success, then you put that the success class. If it's a failure, then we put here the danger. And this is the
# category object.

#                   layout.html

# <!DOCTYPE html>
# <html>
# <head>
#     <title>UTA - Home Page</title>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
#           integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <link rel="stylesheet" href="{{url_for('static', filename='/css/main.css')}}"/>
# </head>
# <body>
#
# <div class="container-fluid text-center top-container">
#     <img src="{{url_for('static', filename='/images/uta-logo-200.png')}}">
# </div>
# <div class="container">
#     {% include "includes/nav.html" %}
#
#     {% with messages = get_flashed_messages(with_categories=true) %}
#         {% if messages %}
#             {% for category, message in messages %}
#                 <div class="alert alert-{{category}}">
#                     <p>{{ message }}</p>
#                 </div>
#             {% endfor %}
#         {% endif %}
#     {% endwith %}
#
#     {% block content %}
#     {% endblock %}
#
# </div>
#     {% include "includes/footer.html" %}
# </body>
# </html>

#               routes.py
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if request.form.get("email") == "test@uta.com":
#             flash("You are successfully logged in", "success")
#             return redirect("/index")
#         else:
#             flash("Sorry something went wrong.", "danger")
#     return render_template("login.html", title= "Login", form=form, login=True )


# xxxxxxxxxxx           Displaying form validation error messages     xxxxxxxxxxxxxx

#      add to main.css
# .error-message{
#     color: red;
# }

#                           login.html
#     {% extends "layout.html" %}
#
#     {% block content %}
#     <h1>{{ title }}</h1>
#
#     <div class="row">
#         <div class="col-md-6 offset-md-3">
#             <h3></h3>
#             <form name="login" action="" method="post" novalidate>
#                 {{ form.hidden_tag() }}  <!-- this will create that CSRF token to secure our form -->
#
#                 <p>
#                     {{ form.email.label }}<br>
#                     {{ form.email(size=35) }}
#                     {% for error in  form.email.errors %}
#                         <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p>
#                     {{ form.password.label }}<br>
#                     {{ form.password(size=15) }}
#                     {% for error in form.password.errors %}
#                         <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p>
#                     {{ form.submit() }}
#                 </p>
#
#             </form>
#         </div>
#     </div>
#  {% endblock %}                 {{ form.password(size=15) }}
#                     {% for error in form.password.errors %}
#                         <span class="error-message">{{ error }}</span>
#
#
# xxxxxxxxxxxx              Processing form data and updating the database              xxxxxxxxxxxxxxx

# from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash    hash it
# check_password_hash    un-hash it
#
#                               forms.py
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField,
# from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
# from application.models import User
#
# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = StringField("Password", validators=[DataRequired(), Length(min=5, max=15)])
#     remember_me = BooleanField("Remember me")
#     submit = SubmitField("Login")
#
# class RegisterForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired(),  Email()])
#     password = StringField("Password", validators=[DataRequired(), Length(min=5, max=15)])
#     password_confirm = StringField("Confirm password", validators=[DataRequired(), Length(min=5, max=15),
#                                                                    EqualTo('password')])
#     first_name = StringField("First_name", validators=[DataRequired(), Length(min=2, max=55)])
#     last_name = StringField("Last name", validators=[DataRequired(), Length(min=2, max=55)])
#     submit = SubmitField("Register Now")
#
#     def validate_email(self, email):
#         user = User.objects(email=email.data).first()
#         if user:
#             raise ValidationError('Email is already in use. Pick another one.')

#                   models.py
# from application import db
# import flask
# from werkzeug.security import generate_password_hash, check_password_hash
#
# class User(db.Document):
#     user_id     =   db.IntField(unique=True)
#     first_name  =   db.StringField( max_length=50 )
#     last_name   =   db.StringField( max_length=50 )
#     email       =   db.StringField( max_length=30, unique=True )
#     password    =   db.StringField()
#
#     def set_password(self, password):
#         self.password = generate_password_hash(password)
#
#     def get_password(self, password):
#         return  check_password_hash(self.password, password)


# xxxxxxxx    Updating registration route to interact with database    xxxxxxxxxx
#

# @app.route("/register", methods=['POST','GET'])
# def register():
#     if session.get('username'):
#         return redirect(url_for('index'))
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user_id     = User.objects.count()
#         user_id     += 1
#
#         email       = form.email.data
#         password    = form.password.data
#         first_name  = form.first_name.data
#         last_name   = form.last_name.data
#
#         user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
#         user.set_password(password)
#         user.save()
#         flash("You are successfully registered!","success")
#         return redirect(url_for('index'))
#     return render_template("register.html", title="Register", form=form, register=True)

#                   register.html

#     {% extends "layout.html" %}
#
#     {% block content %}
#
#     <div class="container">
#          <form name="login" action="" method="post" novalidate>
#         <fieldset class="form-group">
#             <legend>{{title}}</legend>
#             {{ form.hidden_tag() }}
#                 <p> {{ form.email.label }}</br>
#                     {{ form.email }}
#                     {% for error in form.email.errors %}
#                      <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p> {{ form.password.label }}</br>
#                     {{ form.password }}
#                     {% for error in form.password.errors %}
#                      <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p> {{ form.password_confirm.label }}</br>
#                     {{ form.password_confirm }}
#                     {% for error in form.password_confirm.errors %}
#                      <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p> {{ form.first_name.label }}</br>
#                     {{ form.first_name }}
#                     {% for error in form.first_name.errors %}
#                      <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p> {{ form.last_name.label }}</br>
#                     {{ form.last_name }}
#                     {% for error in form.last_name.errors %}
#                      <span class="error-message">{{ error }}</span>
#                     {% endfor %}
#                 </p>
#
#                 <p>
#                     {{ form.submit() }}
#                 </p>
#
#         </fieldset>
#         </form>
#     </div>
#     {% endblock %}

# xxxxxxxxxxx           Creating the courses page           xxxxxxxxx

# @app.route("/courses/")
# @app.route("/courses/<term>")
# def courses(term=None):
#     if term == None:
#         term = 'Spring 2019'
#     classes = Course.objects.order_by("courseID")
#     return render_template("courses.html", courseData=courseData, courses = True, term=term )

# xxxxxxxxx       Installing Postman and the Flask-RESTPlus APIs extension       xxxxxxxxxxxxxxx

#  the Postman is a API development environment for testing APIs.

#  pip install flask-restplus

# xxxxxxxxx       Fetching data using GET         xxxxxxxxxx

#  I'm going to go into the application folder inside the init folder, remember we installed the flask rest plus already
#  so we need to import that in here and then create an instance of that library.

# from flask_restplus import Api
# api = Api()

# So I'm going to go in here and say it's going to be from the flask underscore rest plus and we need to import the API
# class and then right down here which is like instantiate in API object of this API class.

# Now go into the routes, and then we need to a do a few things here, just some minor changes. I'm going to hide this
# one for now. Well, okay. This one here on the top here, we need to import the library again but we need to get the
# resource, this a resources class so, I'm going here and do again, the flask underscore rest plus. I'm going to import
# the resource. This isn't a class that actually allows or the handles all the API requests and and uh for us so, it
# makes it really really easy for us to do, so that's all we need for that one.

# from flask_restplus import Resource

# @api.route('/api', '/api/')
# class GetAndPost(Resource):
#
#     def get(self):
#         return jsonify(User.objects.all())
#
#
# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#
#     def get(self, idx):
#         return jsonify(User.objects(user_id=idx))