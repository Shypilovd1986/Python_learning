# pipenv graph      I'll see a graph of dependencies

# pipenv install name_what install .
# pipenv isntall    will install dependencies from Pipfile.lock

# pipenv shell    switch between env

# pipenv check     I have my dependencies checked for vulnerabilities.
# At the time of this recording though this may be a bit cumbersome. There is an issue with the API key for safety. The
# workaround for that is to type in
# export PIPENV_PYUP_API_KEY=""          And this should fix the issue. So if you encounter a API problem you should
# simply type that in

# . At the time of this recording I recommend you check out a tool called Bandit. Bandit is a code analysis tool that
# scans your code for vulnerabilities. Now while this is by no means a substitute for a good code review.

# A few words about encryption and injection
# So things to consider are always using protocols like HTTPS. Now that certificates are virtually free, there really
# isn't an excuse not to.
#  Always encrypt sensitive customer data and consider encrypting all company computers.
#  Next, I want to talk about injection which is OWASP Top Ten's number one. Specifically, I want to show you how the
#  Python documentation is a great resource when it comes to dealing with security.

#                        Explicit assertions with Python

# One of the many perks of using the Python language is what could be considered a built-in assertion engine. Assert is
# great for testing and debugging, but should never ever be used for high stakes production environments.

# pipenv run python -O name_file.py    to run python file

# pipenv run django-admin startproject feed   will create new directory feed , where store settings, open file
# settings.py , in this file we will find:

# secret key   ,key should be secret, especially the one used in production.

# debug  Now, once again, we're warned that in production and this should be set to false. If it's set to true and there
# is some sort of exception raised, a lot of times, way too much information is given out as a response, so make sure
# that this is set to false in production.

# allowed_host       this allows us to restrict the domain names that this server is allowed to serve. When debug is set
# to true, it automatically allows our local hosts.

# installed_apps      we'll see the installed applications

#  we'll see the middleware definition and these are great security features that you get out of the box with minimal
#  to no effort whatsoever. You see SecurityMiddleware, SessionMiddleware, you'll see the CsrfViewMiddleware and so on
#  so forth. And further down there is template definitions. And the default database created is SQLite, and most of the
#  time you'll end up swapping it for Postgres or right away, and you see the auth_password_validators that once again,
#  you don't have to work for implement.

#                           Generating new projects

# Such information include secret keys, database passwords and tokens. Secrets should be kept out of source code and
# source control. And must be replaced if there's even a suspicion that they have been compromised.

#   Let's look at a basic way to keep a secret out of our application. So I'm going to head over to my exercise file to
#   03, 03_03_begin, feed, feed, settings.py And over at line 23 you'll see the secret key. Which as the name implies is
#   a secret. So the first thing I'll do is cut it. I'll head over to my terminal. And here I am again at 03, 03_03_
#   begin. And I'm going to create a file with one command. So echo. And I'm going to paste this secret key. And then
#   type in greater than. Secret_key.txt. By the way this is straight out of the Django documentation and that I highly
#   encourage you check out. I'm going to go ahead and hit Enter.
# echo 'django-insecure-v&o-k^k6%kaczn5w(!*pjlp1-fwc+1mv4u0ak9r(*=0@ku4v*_' > secret_key.txt

# in file settings.py
# with open('secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
# And I'm going to say that the secret key is f.read.strip. Now in the Django documentation the secret key is stored at
# the etc directory.  The base directory is going to be constantly committed to source control. And there is a good
# chance that somebody along the way will forget to ignore this file.

# first step move secret key from file settings.py to secret_key.txt, and open file
# in file settings.py
# with open('secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# second step is change name admin on more diffiucult in file urls.py  ,
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('appstaff/', admin.site.urls),
# ]

#  And this is just something to make this a little bit harder on the usual hacker.

# !!!!  We must add file secrt_key.txt to file .gitignore

#                           Safe serializing

#   Now whether an API is consumed by a single page application, a mobile application, or even another API, it's
# important to note that APIs are often less observed by people, and therefore more susceptible to overexposure of data.

# pipenv run python manage.py createsuperuser      And here I have a Django application with an API, and in order to
# explore this API a little bit, we're going to create a superuser.

#   pipenv run python manage.py migrate
#  pipenv run python manage.py createsuperuser    will create a superuser, input password and name
# pipenv run python manage.py runserver         And now let's go ahead and run this server, so pipenv run python
# manage.py runserver. And I'm told that a server is running at local host 8000, and the specific route that I'll go to
# is localhost:8000/posts/. And Django REST framework gives us this interface for interacting with our API while in
# development. So I'm going to log in.

# from rest_framework import serializers
#
# from .models import Post
#
#
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         lookup_field = 'slug'
#         fields = '__all__'
#
#     created = serializers.DateTimeField(format='%a, %d %b %Y')
#


# And right off the bat, you will see that I'm using Django REST framework, which is a great tool for creating REST API
# using Python and Django. And one of the great things about it is that it comes with powerful serialization mechanism.
# If you're using something like Flask or Django without Django REST framework, I still recommend you use something for
# serialization. Another tool would be something like Marshmallow. But here, since I'm using REST framework, I can use
# their robust serializer. And here on line six you'll see that I define a post serializer using the model serializer
# class. And in the meta class, on line eight, I assign the model of post, which is my Django model. On line nine, the
# lookup field is slug, which is great. But then on line 10, we have the issue. The fields are specified as all, which
# means anything on this Django model just basically gets thrown into this API indiscriminately. Already we see issues
# with this. We had the post ID serialized unintentionally, but down the road, even greater problems can arise. This is
# because anything that gets added to the post automatically gets added to the API without any thought as far as
# security goes. So how do we fix this? On line 10, I change this all to a list. And in that list, I explicitly say what
# I want serialized. So here, I'll add author, text, created, and this is a good start. If I go over I'll see that my ID
# should not be serialized at this point. Let's go over to my terminal, make sure it's running again. Pipenv run python
# manage.py runserver. And if I refresh, I'll see that my ID is not serialized.
#
# . However, the author still shows its ID. And I can do a little better, so let's go back to the code. And on line 13,
# I'm going to go ahead and say that author is a serializers.SlugRelatedField. And it needs a query set. So for that,
# I'm going to import the user model. So from django.contrib.auth, import get_user_model. And the queryset value equals
# get_user_model. Invoke the function, .objects.all. Finally I need to specify that the slug_field is username. Go ahead
# and save that. And head over to my terminal, where the server was restarted. And if I head over to the browser and
# refresh, I'll see that the author is ro, it's no longer the author ID, and the text is Hello Secure Py.

# from django.contrib.auth import get_user_model
# from rest_framework import serializers
#
# from .models import Post
#
#
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         lookup_field = 'slug'
#         fields = ['author', 'text', 'created']
#
#     created = serializers.DateTimeField(format='%a, %d %b %Y')
#     author = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

#                        Permissions

#  Now often you'll hear the words, permission and authentication used interchangeably in software and this often leads
#  to the absence of permissions. So authentication deals with who the user is, authenticating who they are with
#  credentials while permissions refers to what the user can see and do.

# from rest_framework import status
#
# from rest_framework.test import APIClient
#
# import pytest
#
# from ..models import Post, Profile
# from .test_utils import author, non_author, PostFactory
#
#
# @pytest.mark.django_db
# def test_author_permissions(client, author):
#     """should only allow authors to read posts"""
#     PostFactory(author=author)
#     client.force_login(author)
#     permitted_response = client.get('/posts/')
#
#     assert permitted_response.status_code == status.HTTP_200_OK
#     assert len(permitted_response.json()) == 1
#
#
# @pytest.mark.django_db
# def test_author_no_permissions(client, non_author):
#     """should not allow non-authors to read posts"""
#     client.force_login(non_author)
#     blocked_response = client.get('/posts/')
#     assert blocked_response.status_code == status.HTTP_403_FORBIDDEN
#     assert (
#         blocked_response.json()['detail']
#         == 'You do not have permission to perform this action.'
#     )

#                           Flask secrets

#   . So the two things to keep in mind is, just like in Django, we have to keep that secret key out of source code and
#   source control, and the secret key must be pretty random. How do we do that? Well, luckily the Flask documentation
#   offers some advice. Let's head over to our terminal to give this a go. So the Flash documentation gives us one line
#   to use in order to generate something random for our secret key.

# pipenv run python -c 'import os; print(os.urandom(64))' > secret_key.txt       generate random key to file

#       Flask doesn't offer much in the way of opinion as to how you should structure your project. Here, I use a single
#  file, but especially as your project goes, I encourage you to go ahead and break it down into more modules to keep
#  things neat and organized. So right at the top, you'll see some imports. Notably on line 6, I use things from Flask
#  Login which is an add-on for authentication. Then on line 7 you'll see that I use features from Marshmallow which
#  helps with serialization. Then on line 8, there are things from Werkzeug which is the toolbox that Flask is built
#  upon. On line 13, I instantiate a Flask app and right after that is a good point to configure the secret key. So for
#  that, I'm going to go ahead and start a new line and I'll say with open('secret_key.txt') and the mode is readbytes,
#  'rb' as f: app.secret_key = f.read and I need to invoke that with parenthesis, ().strip(), also invoke. So that's a
#  little bit more work having to generate something random and then configure it. You'll see that when you develop with
#  Flask you have great flexibility and freedom but a lot of those features that you may have taken for granted if
#  you've worked with something like Django, you now have to take care of, yourself. So next, we're going to look at
#  another feature that you have to implement, yourself, when it comes to security a Flask application. This is a really
#  important one as it can compromise not only your users' use of your Website, but other Websites, as well.

# !!!!  The Django user model takes care of this for you. But with Flask, this is up to you to implement. Let's take a
# look at how this is done. In hash !!

# import sys
# import os
# import uuid
# import click
# from flask import Flask, jsonify, request
# from flask_login import LoginManager, login_user, login_required, logout_user
# from marshmallow import Schema, fields, ValidationError
# from werkzeug.security import generate_password_hash, check_password_hash
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Float
#
# app = Flask(__name__)
# with open('secret_key.txt', 'rb') as f:
#     app.secret_key = f.read().strip()
#
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# app.config[
#     'SQLALCHEMY_DATABASE_URI'
# ] = f"sqlite:///{os.path.join(BASE_DIR, 'statuses.db')}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# login_manager = LoginManager()
#
# login_manager.init_app(app)
#
#
# class Author(db.Model):
#     __tablename__ = 'authors'
#     id = Column(Integer, primary_key=True)
#     handle = Column(String)
#     email = Column(String, unique=True)
#     password = Column(String)
#     slug = Column(String, default=lambda: str(uuid.uuid4()))
#     status = db.relationship('Status', backref='author', lazy='dynamic')
#
#     def set_password(self, password):
#         self.password = generate_password_hash(
#             method='pbkdf2:sha512:150000', password=password
#         )
#
#     def check_password(self, password):
#         return check_password_hash(self.password, password)
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.id
#
#
# class Status(db.Model):
#     __tablename__ = 'statuse'
#     id = Column(Integer, primary_key=True)
#     slug = Column(String, default=lambda: str(uuid.uuid4()))
#     text = Column(String(length=55))
#     author_id = db.Column(Integer, db.ForeignKey('authors.id'))
#
#
# def init_db():
#     db.create_all()
#     click.secho('DB created succesfull', bg='green')
#
#
# @app.cli.command('create_db')
# def create_db():
#     init_db()
#
#
# @app.cli.command('seed_db')
# def seed_db():
#     author = Author(handle='foo', email='fooo@example.com', password='passs')
#     status_1 = Status(text='foooo', author_id=author.id)
#     status_2 = Status(text='foooo baz', author_id=author.id)
#     db.session.add(author)
#     db.session.add(status_1)
#     db.session.add(status_2)
#
#
# class RegesterAuthorSchema(Schema):
#     handle = fields.String(required=True)
#     email = fields.Email(required=True)
#     password = fields.Str(load_only=True)
#
#
# class LoginAuthorSchema(Schema):
#     email = fields.Email(required=True)
#     password = fields.Str(load_only=True)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return Author.query.filter_by(id=user_id).first()
#
#
# @app.route('/register', methods=['POST'])
# def register():
#     try:
#         schema = RegesterAuthorSchema()
#         data = schema.load(request.json)
#         email = data['email']
#         author_exists = Author.query.filter_by(email=email).first()
#         if author_exists:
#             return jsonify(message='cannot create user'), 409
#
#         handle = data['handle']
#         author = Author(handle=handle, email=email)
#         author.set_password(data['password'])
#         db.session.add(author)
#         db.session.commit()
#         return jsonify(message='registration successful'), 201
#
#     except ValidationError as error:
#         return jsonify(error.messages), 409
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         schema = LoginAuthorSchema()
#         data = schema.load(request.json)
#         email = data['email']
#         author = Author.query.filter_by(email=email).first()
#         if not author:
#             return jsonify(message='wrong credentials'), 401
#         if author.check_password(data['password']):
#             login_user(author)
#             return jsonify(message='success'), 200
#         else:
#             return jsonify(message='wrong credentials'), 401  # TODO status
#     except ValidationError as error:
#         return jsonify(error.messages), 409
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return jsonify(message='success'), 200
#
#
# @app.route('/confidential', methods=['GET'])
# @login_required
# def confidential():
#     return jsonify(
#         [
#             {'secret_one': 'The moon is made of cheese.'},
#             {'secret_two': 'The tooth fairy is real.'},
#         ]
#     )
#
# if not 'pytest' in sys.argv[0]:
#     app.run(debug=True)