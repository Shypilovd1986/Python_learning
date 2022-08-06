# from flask import Flask

# app = Flask(__name__)
#
# @app.route('/')
# def hallo_world():
#     return 'Hello world'
#
# if __name__ == '__main__':
#     app.run()
#
#  So that's it, Flask projects in PyCharm are very simple it generated one file and installed half a dozen third party
# dependencies. One of the reasons I was drawn to working with Flask in the first place is this simplicity.

# /    an endpoint is just a URL. . In this case, we're responding to the site root. In your traditional HTML website,
# the root would be whatever is in index.html, it's the default content for the site.
#
#  Flask, like many web development frameworks comes with its own built-in development web server. You definitely don't
#  want to use this in production though, because it can be very brittle. But it's very convenient for development work.

# app.py  (name of our file)      and press enter. This starts the Flask development web server and you can see after it
# starts we have a running server bound to a port on local host. That's the manual way to start the server. To stop it
# press Ctrl + C

# . Flask is based on another library called Werkzeug. Werkzeug is the source of our development server and it supports
# auto reloading whenever it detects a particular environment variable in your system. Environment variables are just
# variables that you can set in the operating system and they can be different on any server. This is a great way to
# store configuration information like database connection strings, API keys, and anything else you don't really want
# in your code.

#  The web is based on a request-response mechanism. Your browser requests a resource from a site and the site returns
#  a response. Typically, it's an HTML document with links, descript files, CSS images, videos, and whatever else is
#  needed to render the page. But there's more to the response than just the HTML or the JSON data that you can see.
#  Requests and responses both have headers. Headers are metadata that describe the characteristics of the request or
#  response. One of the key pieces of information in the header is the status code.

#  The status code is useful because if you have UI code that's calling the end point, the calling program needs to know
#  if there are any problems with the request. This is true regardless of whether it's a mobile, desktop, or web
#  application calling the end point.

# ********************        URL parameters          *******************
# http://google.com/?name=Jack
#  We can add parameters to the end by adding a question mark followed by a series of key-value pairs. This allows your
#  front-end to pass in variable information directly to your endpoint.
#
# from flask import request
#  The request object is tracked by Flask automatically and it gives you access to every piece of metadata you could
#  imagine on the URL request it's matching. The request object is generally always available in your endpoint functions
#  but we do need to add an import statement in order to use it.

# @app.route('/parameters')
# def parameters():
#     name = request.args.get('name')
#     age = int(request.args.get('age'))
#     if age < 18:
#         return jsonify(message = 'Sorry ' + name + ', you are not old enough'), 401
#     else:
#         return jsonify(message = 'Wellcome '+name +'. You are old enough')

#  To do this I'll type in request.args which gives you access to all of the URL variables. And then .get, and from here
#  I just need the name of the parameter that's being passed in. In this case it is literally name. I'll do the same
#  thing for age.

# ******************              Adding an ORM (SQLAlchemy)           **********************
# SQLite because it's a file-based database. Most database software like SQL Server, Oracle, or my SQL are server-based,
# meaning you have to install and manage a database server, usually on your development machine. By using SQLite, we can
# bypass that and just use a simple database file to store our data.

#  very popular object-relational mapper or ORM to deal with our database. Relational databases typically use a query
#  language called SQL for Structured Query Language to manipulate the structure and data in our database. When using
#  an ORM, that SQL is generated for you behind the scenes.

# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String, Float, Column, Integer
# import os
#  next step is to add the configuration. So since this is a file-based database, I need to tell my application where
#  to store the file.

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'planets.db')
#  Next, I need to add some configuration variables. Now I could use something fancy, an external library, for this, but
#  it turns out that Flask has a configuration manager built into it, so I'm just going to leverage that


# we got a new tool, the Flask command line interface, or CLI. The CLI allows you to run arbitrary commands against your
# app. This is actually how we're starting our dev web server right now

# @app.cli.command('db_create')  # as an argument, pass in the name that you would like to use as your command.
# def db_create():
#     db.create_all()
#     print('Database created')
#
# @app.cli.command('db_drop')
# def db_drop():
#     db.drop_all()
#     print('Database dropped')
#
#
# @app.cli.command('db_seed')
# def db_seed():
#     mercury = Planet(planet_name='Mercury',
#                      planet_type='Class D',
#                      home_star='Sol',
#                      mass=3.258e23,
#                      radius=1516,
#                      distance=35.98e6)
#
#     venus = Planet(planet_name='Venus',
#                    planet_type='Class K',
#                    home_star='Sol',
#                    mass=4.867e24,
#                    radius=3760,
#                    distance=37.24e6)
#
#     earth = Planet(planet_name='Earth',
#                    planet_type='Class M',
#                    home_star='Sol',
#                    mass=5.972e24,
#                    radius=3959,
#                    distance=92.96e6)
#     #      We need to add these to the database as records.
#     db.session.add(mercury)
#     db.session.add(venus)
#     db.session.add(earth)
#
#     # ctrl+D  It'll duplicate the line that you're on right below it.
#
#     test_user = User(first_name='Dmitriy',
#                      last_name='Shypilov',
#                      email='shypilovd@gmail.com',
#                      password='1234'
#                      )
#     db.session.add(test_user)
#     db.session.commit()  # A lot of databases require you to use commit in order to save your changes.
#     #   Without it, the script will run normally but nothing will get done, nothing will be added to your database.
#     print('Database seeded')

# in the terminal we write
# flask db_create     to create db
# flask db_seed     to seed our db
#
#  Flask is built on top of another library you're going to see mentioned in your logs quite often Werkzeug, Werkzeug
# is a Python web services gateway interface or WSGI for short. Werkzeug is responsible for actually serving up our data
# in response to the endpoint definitions we've made in Flask. Flask is usually used to develop traditional template-
# based HTML sites and this error page belies this fact by giving you a gigantic page full of HTML.

# t Flask.JSON can't convert the data we passed into the function into actual JSON the normal JSON serializers work with
# Python dictionaries but this isn't strictly speaking a Python dictionary.

# *************     Serializing SQLAlchemy results with Marshmallow         *******************
#
#  The process of converting an object into a textual representation of that object is called serialization.

# from flask import Flask, jsonify, request
# from flask_marshmallow import Marshmallow
#
# app = Flask(__name__)
# ma = Marshmallow(app)
#
#  Now that we've established an instance of Marshmallow, we need to add a couple more classes to our code.
#
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'first_name', 'second_name', 'email', 'password')
#
# class PlanetSchema(ma.Schema):
#     class Meta:
#         fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')
#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

# I'll start with user_schema which is just my variable name and I'm going to set that equal to UserSchema like so and
# then I'm going to make a second one called users, plural, schema and I'll instantiate that one as UserSchema again but
# this time I'm going to pass in an extra parameter. Many equals True. What we're doing here is we're defining the
# ability to deserialize a single object as when you get one planet back later on when we make the route for that, maybe
# for the details versus getting a collection of records back which is what we're doing right now.

#  There's Flask-Login, which handles logging in, logging out, and session management. There's also Flask-User, which
#  handles user registration, login, logout, and role based security, like the kind I mentioned earlier. When evaluating
#  these plugins, remember traditionally Flask is used to make traditional template based websites. I don't like the
#  idea of storing session data in my API projects, so I don't use anything that requires session management. Also, if
#  you want to use one of these plugins, research how it works with your ORM if you intend to use one. There are
#  additional plugins that allow the user management plugins for Flask to work with SQLAlchemy. For API projects, I
#  prefer to use a technology called JSON Web Tokens. http://jwt.io

#  JavaScript Object Notation, or JSON, is a universal format. We've been using it so far to represent our data.

# JSON Web Tokens, or JWT, is an open standard for authenticating and verifying JADA exchanges between two parties.
# we should install flask-JWT-Extended
#  The Flask-JWT library works by adding decorators to the routes you want to protect, but at this stage we don't have
#  any like that.

# ***********************              Registering new users           ******************

# from flask_jwt_extended import JWTManager, jwt_required, create_access_token
# @app.route('/login', methods=['POST'])  # I'm going to set the methods equal to POST. The reason why that's
# controversial is that POST is usually associated with creating new records, and that's not what we're doing here. A
# purist might argue that we should be using a get request for this, but POST has been the de facto way of doing this
# for a very, very long time, and I think that's probably what most people use in real life. I'm going to leave it as
# POST.
# def login():
#     if request.is_json:  # . If it's a JSON POST, this will be true, and we just need to grab the email and the password
#         # off of the JSON POST
#         email = request.json['email']
#         password = request.json['password']
#     else:
#         email = request.form['email']
#         password = request.form['password']
#
#     test = User.query.filter_by(email=email, password=password).first()  # I'll add .first to get back the first
#     # record. We're only expecting there to be one entry since it's illegal to have two user IDs concurrently in the databas
#     if test:
#         access_token = create_access_token(identity=email)  # At this point they have succeeded, so we need to send
#         # them the Web token, the JWT Web token, so let's create that. I'll create a variable called access_token to store
#         # it. I'll set that equal to create_access_token. This is a function that's coming from the JWT Flask plugin. I can
#         # see there that it requires a single argument identity, so I'll pass in identity. What it wants here is, how are we
#         # actually identifying the user? We're using the email address for that.
#         return jsonify(message='Login succeeded', access_token=access_token)
#     else:
#         return jsonify(message='Bad email or password'), 401
#

#     in Postman , Post method and that's form fields. I'll click the Body tab, I'll select form data
#      But this time we're going to send a JSON request. To do that, we still go into the Body tab, but instead of form
#      data, this time we're going to click raw, and then we're going to set the type from Text to JSON. Now we can
#      submit a regular JSON object in here. Don't forget JSON objects are different from JavaScript objects in that
#      they have to have the double quotes around them to define the different elements.

# ************************        Setting up email         *************************

# pip install flask-mail
# from flask_mail import Mail, Message
#  Next, I need to add some configuration elements that tell the flask-mail plugin where to actually send or what server
#  to use, what mail server to use to actually send this out.

#  Now if you're like me, you probably don't have an email server running on your laptop or on your desktop computer.
#  You might have access to one at work, you might want to try using a free or a public one but I've actually got a
#  better solution for this. There's an application called mailtrap.io or just mailtrap. And basically what this does is
#  it allows you to test sending emails without ever actually sending them. So, you don't have to set up a mail server,
#  you don't have to do any of that, you just have to sign up.

# http:\\mailtrap.io
#  So, if you don't have an account here already, go ahead and click Sign up and go set yourself up and then log in. I'm
# going to go ahead and log in. And I'll select my demo inbox and I can see that there's nothing there but the part that
# I really need is over here under Credentials. So, I can see that the host that I'm supposed to type in is
# smtp.mailtrap.io. Here are the ports and the username is just going to be a long string of letters and numbers and so
# is the password. Now in this case, since this is my account

# So, this is the configuration data that we need to enter into our configuration, so let's switch back over to PyCharm
# and let's add a few configuration elements

# app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
# app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
#  So, let me switch back over and let's use environment variables just like we would in a real app. I'll type in
#  os.environ and I'm going to set the keys in my environment variable, I'm going to set my environment variable names
#  to be the same as the app key. So, I'll use MAIL_USERNAME and then I'll do the exact same thing for password

# in mailtrap site we go to Integration section and switch to Flask-mail , we copy code for our app and paste it
# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '5e5d87bad1bda2'
# app.config['MAIL_PASSWORD'] = 'b18d6e80a15c05'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# **********************          Adding planets with a POST method          ******************

# @app.route('/adding_planet', methods=['POST'])
# def adding_planet():
#     planet_name = request.form['planet_name']
#     test = Planet.query.filter_by(planet_name=planet_name).first()
#     if test:
#         return jsonify(message="There is already planet by that name"), 409  # conflict
#     else:
#         planet_type = request.form['planet_type']
#         home_star = request.form['home_star']
#         mass = float(request.form['mass'])
#         radius = float(request.form['distance'])
#
#         new_planet = Planet(planet_name=planet_name,
#                             planet_type=planet_type,
#                             home_star=home_star,
#                             mass=mass,
#                             radius=radius
#                             )
#
#         db.session.add(new_planet)
#         db.session.commit()
#         return jsonify(message="You added a planet"), 201  # A 201 status code indicates that a request was successful
#         # and as a result, a resource has been created

# ************     Securing the add planet endpoint     ******************

# e know we're using JSON web tokens. Protecting your endpoint is actually very easy. I'm just going to add another
# decorator to the method signature here. I'll go ahead and put it right below the app.route definition. And I'm just
# going to type in the at symbol followed by jwt_required.
# @app.route('/adding_planet', methods=['POST'])
# @jwt_required()
# def adding_planet():

# . I'll click Send and I should get back an access token and a message saying log in succeeded but the part that I need
# is this part right here, so I'm just going to grab this whole access token and I'm going to copy it using Command + C
# or Control + C if you're on a PC. Next, let's go back to that tab that we were on just a moment ago when we were
# testing our add_planet route. Go ahead and click the Authorization tab and change the type to Bearer Token. As soon as
# you do that, you'll get a little box here that you can click in. And I'm going to paste in the token that I just
# copied. With that passed in, I'll click Send. And I'll get back a message saying I successfully added a planet with
# the status of 201 created.

# ***********      Updating a planet using a PUT method       ***************

#  Before we dive in, I should warn you that there are a lot of Web developers out there who never use the PUT verb.
#  They basically use GET for retrieving data and POST for everything else. It works, but at that point, you aren't
#  using the verbs the way they were designed. If your front-end team doesn't use PUT, you might consider accepting
#  either PUT or POST to allow for a wider range of programming style.

# @app.route('/update_planet', methods=['PUT'])
# @jwt_required()
# def update_planet():
#     planet_id = int(request.form['planet_id'])
#     planet = Planet.query.filter_by(planet_id=planet_id).first()
#     if planet:
#         planet.planet_name = request.form['planet_name']
#         planet.planet_type = request.form['planet_type']
#         planet.home_star = request.form['home_star']
#         planet.mass = float(request.form['mass'])
#         planet.radius = float(request.form['radius'])
#         planet.distance = float(request.form['distance'])
#
#         db.session.commit()
#         return jsonify(message="You updated a planet"), 202 # The request has been accepted for processing, but the
#         # processing has not been completed.
#     else:
#         return jsonify(message = "That planet doesn't exists"), 404

# ***********     Deleting a planet with DEL     ******************

# . There are two strategies for deleting. The simplest, and the one we'll actually be doing, is to literally delete the
# record from the database. There are many apps though that never actually delete anything, they add a field to the
# table that let's you mark a record deleted without actually deleting it.
# @app.route('/remove_planet/<int:planet_id>', methods=['DELETE'])
# @jwt_required()
# def remove_planet(planet_id: int):
#     planet = Planet.query.filter_by(planet_id=planet_id).first()
#     if planet:
#         db.session.delete(planet)
#         db.session.commit()
#
#         return jsonify(message="You deleted a planet"), 202
#     else:
#         return jsonify(message = "That planet doesn't exist"), 404

# *************          Exporting your project’s requirements file        ****************

#  The first thing you need to do in any python project is to export a requirements file. This is just a text file that
#  lists all the dependencies and third party libraries we've been adding as we developed our application. When we set
#  up our product it would be a real pain to try to remember all the libraries we added along with any dependencies.
#  Unfortunately for this there's no slick GUI and PyCharm for this right now, so we'll have to do it the old fashioned
#  way using the terminal.

# #  pip freeze >requirements.txt     show all what we need to use our api
# # pythonanywhere
# # digitalocean
# # . If you go the virtual machine route, the first thing you'll want to decide is which WSGI server you want to use in
# # production. I recommend Green Unicorn. I usually also install a static web server alongside Green Unicorn, and my
# # favorite pick for the web sever is NGINX.
#
# # gunicorn.org
# # nginx.com

# ************************     EXAMPLE     ********************

# from flask import Flask, jsonify, request
# from flask_marshmallow import Marshmallow
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String, Float, Column, Integer
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required
# from flask_mail import Mail, Message
#
# import os
#
# app = Flask(__name__)
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# # So since this is a file-based database, I need to tell my application where to store the file.I'm going to add a
# # variable called basedir, base directory, So basically, all I've really done here is I've gotten the path for the
# # application itself. I'm just going to put my database file in the same folder as the running application.
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
# #
# #  Let's add a key to this, so I'll say app.config, and the name of the key is JWT_SECRET_KEY in all caps. Normally you
# # would set this equal to some secure string like a GUID or a UUID, but I'm just going to set mine to super-secret.
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # change this in real life
# app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'  # copy from https://mailtrap.io/inboxes/1839216/messages
# app.config['MAIL_PORT'] = 2525  # choose flask-mail
# app.config['MAIL_USERNAME'] = 'b79dad5c6a88fd'
# app.config['MAIL_PASSWORD'] = '855d82b592b044'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
#
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# jwt = JWTManager(app)
# mail = Mail(app)
#
#
# # turn it into a command, and I do that by adding a decorator, sort of like what we did on our routes.
# @app.cli.command('db_create')  # as an argument, pass in the name that you would like to use as your command.
# def db_create():
#     db.create_all()
#     print('Database created')
#
#
# @app.cli.command('db_drop')
# def db_drop():
#     db.drop_all()
#     print('Database dropped')
#
#
# @app.cli.command('db_seed')
# def db_seed():
#     mercury = Planet(planet_name='Mercury',
#                      planet_type='Class D',
#                      home_star='Sol',
#                      mass=3.258e23,
#                      radius=1516,
#                      distance=35.98e6)
#
#     venus = Planet(planet_name='Venus',
#                    planet_type='Class K',
#                    home_star='Sol',
#                    mass=4.867e24,
#                    radius=3760,
#                    distance=37.24e6)
#
#     earth = Planet(planet_name='Earth',
#                    planet_type='Class M',
#                    home_star='Sol',
#                    mass=5.972e24,
#                    radius=3959,
#                    distance=92.96e6)
#     #      We need to add these to the database as records.
#     db.session.add(mercury)
#     db.session.add(venus)
#     db.session.add(earth)
#
#     # ctrl+D  It'll duplicate the line that you're on right below it.
#
#     test_user = User(first_name='Dmitriy',
#                      last_name='Shypilov',
#                      email='shypilovd@gmail.com',
#                      password='1234'
#                      )
#     db.session.add(test_user)
#     db.session.commit()  # A lot of databases require you to use commit in order to save your changes.
#     #   Without it, the script will run normally but nothing will get done, nothing will be added to your database.
#     print('Database seeded')
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello world'
#
#
# @app.route('/super_simple')
# def super_simple():
#     return jsonify(message='Hello from the planetary API. !!!')
#
#
# # jsonify,  returning valid JSON ,  it's just key value pairs for the data that you want to represent. In this case we
# # have a key called Message and then the message value
#
# @app.route('/page_not_found')
# def page_not_found():
#     return jsonify(message='that resource was not found'), 404
#
#
# @app.route('/parameters')
# def parameters():
#     name = request.args.get('name')
#     age = int(request.args.get('age'))
#     # http://localhost:5000/parameters?name=Jon&age=36
#     if age < 18:
#         return jsonify(message='Sorry ' + name + ', you are not old enough'), 401
#     else:
#         return jsonify(message='Wellcome ' + name + '. You are old enough')
#
#
# @app.route('/url_variables/<string:name>/<int:age>')
# def url_variables(name, age):
#     if age < 18:
#         return jsonify(message='Sorry ' + name + ', you are not old enough'), 401
#     else:
#         return jsonify(message='Wellcome ' + name + '. You are old enough')
#
#
# @app.route('/planets', methods=['GET'])  # Essentially here you're making an array, and then you put inside of that the
# # verbs that you want to accept. You can accept more than one and you can even program your routes to behave differently
# # depending on which one it gets.
# def planets():
#     planets_list = Planet.query.all()  # We're getting this function from SQLAlchemy
#     result = planets_schema.dump(planets_list)
#     return jsonify(result)
#
#
# @app.route('/register', methods=['POST'])
# def register():
#     email = request.form['email']
#     test = User.query.filter_by(email=email).first()
#     if test:
#         return jsonify(message='This email is already exists'), 409  # give it a return code of 409 conflict.
#     else:
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         password = request.form['password']
#         user = User(first_name=first_name, last_name=last_name, email=email, password=password)
#         db.session.add(user)  # add the record, we're just going to do the same thing we did earlier in our seed script
#         db.session.commit()
#         return jsonify(message='User created successfully.'), 201
#
#     #  Next I need to see if this user's already registered or not, so I'm going to create a variable called test and
#     #  I'm going to type in User.query.filter_by and I'll type in email equals email.first. So, this is going to call
#     #  the database and we're going to look for a single user with the email address that just got passed in. Now we
#     #  don't need to deserialize this, we don't need Marshmallow for this. I just want to see if there's one there.
#
#
# @app.route('/login', methods=['POST'])  # I'm going to set the methods equal to POST. The reason why that's
# # controversial is that POST is usually associated with creating new records, and that's not what we're doing here. A
# # purist might argue that we should be using a get request for this, but POST has been the de facto way of doing this
# # for a very, very long time, and I think that's probably what most people use in real life. I'm going to leave it as
# # POST.
# def login():
#     if request.is_json:  # . If it's a JSON POST, this will be true, and we just need to grab the email and the password
#         # off of the JSON POST
#         email = request.json['email']
#         password = request.json['password']
#     else:
#         email = request.form['email']
#         password = request.form['password']
#
#     test = User.query.filter_by(email=email, password=password).first()  # I'll add .first to get back the first
#     # record. We're only expecting there to be one entry since it's illegal to have two user IDs concurrently in the databas
#     if test:
#         access_token = create_access_token(identity=email)  # At this point they have succeeded, so we need to send
#         # them the Web token, the JWT Web token, so let's create that. I'll create a variable called access_token to store
#         # it. I'll set that equal to create_access_token. This is a function that's coming from the JWT Flask plugin. I can
#         # see there that it requires a single argument identity, so I'll pass in identity. What it wants here is, how are we
#         # actually identifying the user? We're using the email address for that.
#         return jsonify(message='Login succeeded', access_token=access_token)
#     else:
#         return jsonify(message='Bad email or password'), 401
#
#
# #     in Postman , Post method and that's form fields. I'll click the Body tab, I'll select form data
# #      But this time we're going to send a JSON request. To do that, we still go into the Body tab, but instead of form
# #      data, this time we're going to click raw, and then we're going to set the type from Text to JSON. Now we can
# #      submit a regular JSON object in here. Don't forget JSON objects are different from JavaScript objects in that
# #      they have to have the double quotes around them to define the different elements.
# @app.route('/retrieve_password/<string:email>', methods=['GET'])
# def retrieve_password(email: str):
#     user = User.query.filter_by(email=email).first()
#     if user:
#         msg = Message("your planetary API password is " + user.password,
#                       sender="shypilovd@gmail.com",
#                       recipients=[email])
#         #  This is the body of the email that I'm actually going to send back. I'm going to set that equal to message. We'll
#         #  just use the constructor for message.
#         mail.send(msg)
#         return jsonify(message="password sent to " + email)
#     else:
#         return jsonify(message="That email doesn't exists"), 401
#
#
# @app.route('/planet_details/<int:planet_id>', methods=['GET'])
# def planet_details(planet_id: int):
#     planet = Planet.query.filter_by(planet_id=planet_id).first()
#     # if we got something back then we're going to return the result, but we have to serialize it first.
#     #  Now remember, we've done the heavy lifting for this already, we created two schema for each of the possibilities
#     #  on our records that are getting returned, there's one for the users and one for the planets, and for the planets
#     #  as well as the users, we made two of them for each one, we made one that was singular records and another that
#     #  was a collection of records, so here we're going to be invoking the singular records
#     if planet:
#         result = planet_schema.dump(planet)
#         return jsonify(result)
#     else:
#         return jsonify(message="That planet doesn't exist"), 404
#
#
# @app.route('/adding_planet', methods=['POST'])
# @jwt_required()  # Protecting your endpoint is actually very easy. I'm just going to add another decorator to the method
# def adding_planet():  # signature here.
#     planet_name = request.form['planet_name']
#     test = Planet.query.filter_by(planet_name=planet_name).first()
#     if test:
#         return jsonify(message="There is already planet by that name"), 409  # conflict
#     else:
#         planet_type = request.form['planet_type']
#         home_star = request.form['home_star']
#         mass = float(request.form['mass'])
#         radius = float(request.form['distance'])
#
#         new_planet = Planet(planet_name=planet_name,
#                             planet_type=planet_type,
#                             home_star=home_star,
#                             mass=mass,
#                             radius=radius
#                             )
#
#         db.session.add(new_planet)
#         db.session.commit()
#         return jsonify(message="You added a planet"), 201  # A 201 status code indicates that a request was successful
#         # and as a result, a resource has been created
#
#
# @app.route('/update_planet', methods=['PUT'])
# @jwt_required()
# def update_planet():
#     planet_id = int(request.form['planet_id'])
#     planet = Planet.query.filter_by(planet_id=planet_id).first()
#     if planet:
#         planet.planet_name = request.form['planet_name']
#         planet.planet_type = request.form['planet_type']
#         planet.home_star = request.form['home_star']
#         planet.mass = float(request.form['mass'])
#         planet.radius = float(request.form['radius'])
#         planet.distance = float(request.form['distance'])
#
#         db.session.commit()
#         return jsonify(message="You updated a planet"), 202  # The request has been accepted for processing, but the
#         # processing has not been completed.
#     else:
#         return jsonify(message="That planet doesn't exists"), 404
#
#
# @app.route('/remove_planet/<int:planet_id>', methods=['DELETE'])
# @jwt_required()
# def remove_planet(planet_id: int):
#     planet = Planet.query.filter_by(planet_id=planet_id).first()
#     if planet:
#         db.session.delete(planet)
#         db.session.commit()
#
#         return jsonify(message="You deleted a planet"), 202
#     else:
#         return jsonify(message = "That planet doesn't exist"), 404
#
# # database modul
# # It's telling it we want to use that particular library, db.Model,
# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)  # uniquely identifies a record in the database
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True)
#     password = Column(String)
#
#
# class Planet(db.Model):
#     __tablename__ = 'planets'
#     planet_id = Column(Integer, primary_key=True)  # uniquely identifies a record in the database
#     planet_name = Column(String)
#     planet_type = Column(String)
#     home_star = Column(String)
#     mass = Column(Float)
#     radius = Column(Float)
#     distance = Column(Float)
#
#
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'first_name', 'second_name', 'email', 'password')
#
#
# class PlanetSchema(ma.Schema):
#     class Meta:
#         fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')
#
#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
# # , I'll start with user_schema which is just my variable name and I'm going to set that equal to UserSchema like so and
# # then I'm going to make a second one called users, plural, schema and I'll instantiate that one as UserSchema again but
# # this time I'm going to pass in an extra parameter. Many equals True. What we're doing here is we're defining the
# # ability to deserialize a single object as when you get one planet back later on when we make the route for that, maybe
# # for the details versus getting a collection of records back which is what we're doing right now.
#
# planet_schema = PlanetSchema()
# planets_schema = PlanetSchema(many=True)
#
# if __name__ == '__main__':
#     app.run()
#
# #  pip freeze >requirements.txt     show all what we need to use our api
# # pythonanywhere
# # digitalocean
# # . If you go the virtual machine route, the first thing you'll want to decide is which WSGI server you want to use in
# # production. I recommend Green Unicorn. I usually also install a static web server alongside Green Unicorn, and my
# # favorite pick for the web sever is NGINX.
#
# # gunicorn.org
# # nginx.com