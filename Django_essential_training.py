#  django-admin startproject smartnotes .
#
#  We can start our project by using a Django command, called Django-admin, and then a sub-command, startproject, then,
#  the name of our project, smartnotes, and then dot to indicate we want to create the project in this folder.

# Okay, so this command creates two things: a managed.py file and a folder called smartnotes, the same name we gave our
# project. The managed.py file will be the entry point of your project. With it, you'll be able to run your project
# server, manually work with the database, and much more. If you look inside the smartnotes folder, you'll notice that
# all of the files here are related to the configuration of your project. The two main files you'll use here are the
# urls.py file, where you're going to configure, well, the URLs of your project, and the settings.py.

# python manage.py runserver        As magic as this sounds, you already have everything you need to run your project.
# You can use Python, then the file, manage.py, and the command runserver to create a server using the default
# configurations we have right here. We can see here that there is some warnings in red, but you don't have to worry
# about it for now. You can also see that we're using Django Version 3.2, and that the configuration file being used is
# the smartnotes.settings. This means that this server is using this settings.py inside the smartnotes folder as the
# basis of it.

#  When dealing with big software projects, we need to make sure we are not creating a mess. The way we do this is to
#  compartmentalize our project into smaller sections that have clear boundaries from day one. That's why Django created
#  the concept of apps.

# django-admin startapp home       to create a new app called home. You can see now that we have two folders:
# smartnotes, which is our settings folder, and home, which is the Django app we just created.

#  Every time we create an app, we need to add it to the settings file so that it knows that that folder is part of the
#  project we're running. Let's open the settings.py file. And add the name of our app in the INSTALLED_APPS variable.
#  In order to make things a bit more organized, I always leave a small comment separating this app, created by us, from
#  those that were already installed by default.

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#
#     # apps     ( which we created)
#     'home',
# ]

#                   create function in our new app of project

# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here
#
# def home(request):
#     return HttpResponse('Hello world')
#


# , it's time to create our first view. Let's go to the home, then go to the views file, and write our first function.
# As you can see, this is a pre-configured file. So we need to create our functions here. Let's import from django.http
# import HttpResponse. We can delete this, and now we create def home. It receives a request. And it return an
# HttpResponse with a simple message. Hello, world! As you can see, this function is saying that every time it receives
# a request, it will return a response with the text Hello, world! Okay, but how does it know when to send a request to
# this function? Well, that's why we have the urls.py file. We can go back now to the smartnotes, urls.py, and import
# this file there so we can have access to this function.

#                                   urls.py
# from django.contrib import admin
# from django.urls import path
#
# from home import views
#
# urlpatterns = [
#     path('project_admin/', admin.site.urls),
#     path('home', views.home)

# because we have the debug equals true on the settings file, Django will list the endpoints that this project has
# available. And guess who is there. Yes, our home endpoint we just created. Now if we go to localhost home, we can see
# that we have the Hello, world! being displayed.

#  When a person goes to the home endpoint, they're making a request to that path. Django will go to the urls.py file to
#  see if it's ready to receive a request at this path. Since it is, it will go to the views file, finally arriving to
#  the function we defined. Since the function received the request, it can then respond with a message Hello, world!
#  Django uses a common pattern as the way of structuring its project called Model View Template framework, or MVT.
#  Views are responsible for handling requests and responses. In this video, you have learned that views can be as
#  simple as functions, and can respond with something as simple as pure text. There are yet two additional layers for
#  us to get familiarized with, right? These additional layers will allow us to increase our project's complexity, while
#  being simple tools to work with. The model layer handles the data and how it's stored, and we'll see more about it in
#  chapter three. The template layer allow us to render the information coming from the database into lovely HTML pages.

#                           Creating your first Django template

# it's time to learn how to return HTML pages by using the amazing Django template language. Let's start by creating a
# folder called templates inside our app folder. And inside of this folder, we'll also create another folder with the
# same name as our app, so let's call it home. This might seem weird, but it will allow us to quickly identify where a
# template is located, even if we don't know in which app we are on.

#  This is a typical organization pattern for Django templates. Inside this folder, let's create a file called
#  welcome.html. And inside it, we're going to add a basic HTML page.

# <html>
#     <header><title>SmartNotes</title></header>
#     <body><h1>Welcome to SmartNotes!</h1></body>
#
# </html>

# Okay, so now we can go back to the views file and change our base function. Instead of using the HttpResponse, we'll
# use the function render from the Django shortcuts that's already imported here. To use this function, we need to pass
# three parameters, the original request, the name of the template, and empty brackets. I know there is a warning here
# in the terminal that sounds a bit scary, but don't worry, this is normal, and we'll get to it later.

#  You might be wondering why we left the empty brackets behind, right? Although we are writing an HTML page, Django is
#  actually using a template framework to create the final HTML page that we see in the browser. We can use the brackets
#  at the end of the function as a way of passing down information from the view to the template. So let's import the
#  datetime model and pass today's date into the dictionary with a key called today, datetime.today. We can then modify
#  our template to receive a variable called today by defining it between double brackets.

# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
#
# # Create your views here.
#
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

# <html>
#     <header><title>SmartNotes</title></header>
#     <body><h1>Welcome to SmartNotes!</h1></body>
#     <h3>Today is {{today}} </h3>
# </html>

# . There it is. This is why we're not using pure HTML, but actually a backend framework for defining templates called
# Django template language, or DTL. The HTML file we wrote will pass through the detail mechanism and it will insert the
# variables passed on the dictionary of the render function down to the template. This looks simple now, but DTL allows
# us to use sophisticated programming logic for creating dynamic HTML pages with very little effort.

#               Django apps and the concept of modularization

#     building your Django project
# - start project
# - create first view
# - use templates
# - Apps and Modularization

#  As you've seen, an app is a small library that is contained inside your Django project. We can have as many apps as
#  we want, however, as the project grows, if we don't take care of it, things can start to get messy and things will
#  fly between the apps. That's why we need to understand what we need to do to make good Django apps. Good software
#  projects should be well modularize, and your Django project should be no different. That's why each app should be
#  self-contained, which means that everything you need for that app should live inside it.

# That's why we created the folder template inside it. The ideal app is one where you can delete the folder and do
# nothing else, the Django project just continued to work perfectly. So far, we're almost there, but there's still one
# thing that we need to do to clean things up. When we created our first endpoint, we had to import the fuse file from
# home into the URLs file in the smart notes folder. This creates a dependency that wouldn't allow us to quickly delete
# the home app.

# Let's make things a bit more organized. Okay, so first thing is to create another URL file inside the home app. In
# here, we're going to create a file, very similar to the one we have on the smart notes app. And let's add the same
# endpoint that we had in the previous file, views.home using the home function. Okay, so now comes the fun part, in the
# smart notes, let's get the URLs file. We can delete the dependencies that we implemented here, and now from the jungle
# URLs, we're also going to import the include function. Now, what we need to do is add an import path, but instead of
# using a function, we're going to use the include function here to pass that file as a string. So path, let's leave it
# open for now, and then let's include the home.urls file. Let's save this, and if we go back to browser, yes, as you
# can see here, nothing changed except the fact that now, if we delete the whole app, these won't give any errors
# because the app is not being important on this smart notes URLs file. There, with just a couple of tweaks, we
# eliminated a dependency and your project is following good standards of Django applications.

#           in directory project smartnotes
#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('project_admin/', admin.site.urls),
#     path('', include('home.urls'))
# ]

#               in home directory urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('home', views.home)
# ]

#                   Creating users in Django

# One of the most powerful features is the Django Admin Interface. It provides an interface. So that site administrators
# like you and me can easily view and manipulate data.

#  Django has the entire authentication system ready to go. The only thing we need to do is to make sure our database is
#  properly configured. Let's go back. And remember when we had this red message while running the run server, this
#  message is letting us know that our project has some database changes that weren't applied yet.

# python manage.py migrate
# when we had this red message while running the run server, this message is letting us know that our project has some
# database changes that weren't applied yet. The way Django knows if the database is behind the system, changes is
# through a couple of files called migrations. Migrations, explain what kind of changes a database need to perform such
# as create a new table, establish a new relationship, et cetera. Django already has the migrations for the
# authentication system ready. So what you need to do is apply them to the database and we do this by using the command
# migrate that will actually change the database.

#  python manage.py createsuperuser
# What we need is to create a super user that will have all the powers that can in this Django project. We do this by
# running the command, create super user. It's pretty straightforward. Let's make the username admin. I'm going to leave
# the email address empty, and I'll add admin as a password.

# . Okay, now we can go back to the admin interface, Admin, admin, login, and there you go. Now you have full access to
# the Django Admin Interface. And as you can see, we don't have any red messages now, while we run the run server,
# because our database is completely up to speed with the project.

#                       Django admin: Easily visualizing and creating data
# The Django admin interface allow us to quickly and easily access data that exists in the database. This means that
# users and groups, you can see here, are actually tables in our database.

# Let's create a new user, shall we? We have to go here on add user, then add a username, and let's add a password.
# adminadmin. Save. As you can see here, we can't bypass the password check on the interface, so we actually need a
# really good password here.

# . Now we have the user created. As you can see, to create a user, we just need the username and password, but there is
# more to it, such as personal information, permissions, et cetera.

# . Now we have the user created. As you can see, to create a user, we just need the username and password, but there is
# more to it, such as personal information, permissions, et cetera.

#                       User authentication in two simple steps

# @login_required()
# def authorized(request):
#     return render(request, 'home/suthorized.html', {})

#  In here, let's import from Django dot contrib dot auth dot decorators. Let's import login required. So now I can add
#  this function as a decorator to our authorized function. That's it. That's all we need to do to block the access of
#  this webpage if a user is not logged in.

#  Now let's add the home authorized dot HTML and empty square brackets. Yeah, so now we have exactly the same thing,
#  and here comes the wonderful Django simplicity. In here, let's import from Django dot contrib dot auth dot
#  decorators. Let's import login required. So now I can add this function as a decorator to our authorized function.
#  That's it. That's all we need to do to block the access of this webpage if a user is not logged in. To finalize,
#  let's go to the urls dot py and add this as a path. So let's call it authorized and views dot authorized. Now we can
#  go back and try to access the authorized endpoint. There you go. We can see the template we created. This is only
#  possible because we're logged in via the Django admin interface. If we go back to the admin and log out and try to
#  re-access the authorized area, you see here that we get a 404, meaning that this page was not found. Why is that?
#  Because we're not logged in. The complex authentication system just required a single line of code. However, a 404
#  is really not a nice flow, right? We want the user to know that they need to be logged in to access this page. The
#  ideal flow is that we redirect them to the login page. To do this, we need to go back to the views file and add a
#  parameter called login url. And let's pass this as slash admin. If we go back and try to access it again, and there
#  it is. Since we are not logged in, Django understand that it needs to redirect me to the login url, which for now was
#  defined as the admin end point.

#                   from views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.decorators import login_required
#
# # Create your views here.
#
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})
#
#
# @login_required(login_url='/project_admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

#                   urls.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.decorators import login_required
#
# # Create your views here.
#
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})
#
#
# @login_required(login_url='/project_admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

#                                       Introduction to ORMs

# - So far, you've gotten familiarized with the user models, which were completely defined by Django. Now it's time to
# understand how to create your own models and how the structure of creating models work. Django uses an object
# relational mapping system or ORM to handle database communication and changes. What you need is to write class models
# that will then be transformed by migrations into database tables. Each class known as a model is a database table and
# each class attribute is a column. The way we transform a model into a database table is by the creation of migrations.
# Migrations will have the step-by-step transformation that a database must do to apply the changes made in the code.
# You've seen that we use the command migrate to apply migrations to a database. Similarly we can use the command, make
# migrations to create migration space on the current code, the process of using a class, defining a model, creating a
# migration, and applying the immigration and the changes to the database is the ORM's job. And Django's ORM, is known
# for being one of the best ORM's for Python and SQL databases.

#                               Creating your first model

# It is time for us to learn how to create a new model using Django ORM. Let's create a new app specifically for our
# notes. So Django-admin startapp notes. Okay. Remember, now we have to go to the settings and make sure that our new
# app is added in the installed apps variable. Okay. Now we can go back to this new app and open the models.py file.
# Here is the file where we can create the models that we'll use in this app. So let's create a new class called notes
# that we'll inherit from models.Model. This way, Django knows that this is a model that will have effect on the
# database, et cetera.

#  Well first, we can add a title. A title is a short text, so we can use the type Charfield, which is a limited text
#  view. Charfield has a parameter called max length, and we should set it to a value, let's say 200. This means that
#  our title can't be over 200 characters. Okay, we also need the notes itself, right? And the notes shouldn't have a
#  limit, so instead of using Charfield, we can use the type TextField. As you can see, TextField doesn't require a max
#  length differently from Charfield. We also want to know when this note was created, so we can add a field called
#  created, that is going to be a DateTimeField. Because we don't really want to worry about this field being correctly
#  populated, we can add a parameter called auto_now_add equals to true.

# So what do we need to do now? I hope you guessed it right. We need to create migrations. Luckily, this is super easy
# to do. Let's type python manage.py makemigrations. Let's see what happened here. There is a new folder called
# migrations, and inside of it, there's a new file called 001_initial. Every first migration of an app will be named
# like this. If you open this, you can see that this is just a list of operations that instructs the database what needs
# to be done. So far, we haven't changed anything in the database, we just created the set of instructions, so
# everything continues as it is. What we need to do now is apply the migrations so we can run python manage.py migrate.
# And we're done. The changes were applied to the database and we have a shiny new table.

# python manage.py makemigrations     ,create migration
# python manage.py migrations   ,apply migrations

#         models.py
# from django.db import models
#
# # Create your models here.
# class Notes(models.Model):
#     title = models.CharField(max_length=200)
#     notes = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#                   Using admin for data creation and manipulation

#  So let's go back to the notes app and open a file called admin.py. This is where we go into add which models can be
#  displayed, and thus, modified via the Django admin interface. First, let's create a class and call it NotesAdmin.
#  This class should inherit from admin.ModelAdmin. Let's add pass here because we don't want any additional
#  configuration on this admin model.

#  Now what we need to do is import from this folder. Let's import models, and on the bottom of the file, we're going to
#  register that that model is attached to this admin model. So let's write admin.site.register, then models.Notes, and
#  NotesAdmin. Okay, that's it. Let's go back to the admin and refresh it.

#  Now we can see that the notes model is available on the admin interface. Let's use the add button here to create a
#  new note.

#  One thing that isn't really nice is that it is listed as this Notes Object One. This is fine for now, but if we have
#  a long list of notes, how can we tell which one is which? Let's go back to the admin class. Instead of pass here, we
#  can pass list_display, which is going to be a tuple, and let's pass title here. Let's save this. It restarted.

# The default configuration of admin also allows that all fields can be changed by all users. However, we can edit the
# admin model class and start adding some specialized logic. We can remove some fields from being edited. We can allow
# only staff users to write notes. There's a lot we can do, the sky's the limit. Django admin is highly configurable.

#                     admin.py
# from django.contrib import admin
# from . import models
#
# # Register your models here.
# class NotesAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#
# admin.site.register(models.Notes, NotesAdmin)

#                       models.py
# from django.db import models
#
# # Create your models here.
# class Notes(models.Model):
#     title = models.CharField(max_length=200)
#     notes = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#                       Using Django shell for creating and querying data
#
# . Django has a tool we can use to check the content of a database, which will make our life so much easier, the Django
# shell. Let's go to the terminal and type python manage.py shell. You can see here that we have a Python interpreter,
# however, this is no ordinary interpreter, it is already tightly coupled with our project, for instance, we can type
# from notes.models import Notes, which is the model we just created, and with this, we can use it to query the objects
# in the database.

# python manage.py shell

# from notes.models import Notes
# Notes, which is the model we just created, and with this, we can use it to query the objects in the database. Let's
# try to get the first note

# mynote = Notes.objects.get(pk='1')
# There, we have our note. Notes.objects is the main way of accessing data from the notes table in the database.
# The .get method will search for one object, which the pk private key is equal to one and returns that object.

# mynote.title      return value of column title with pk = 1

# Notes.objects.all
# We can also query for all objects in the database by using the method .all instead of the .get.

# new_note = Notes.objects.create(title='Second note', notes='This is the second note')
#  There, the note was added to the database. If we query it again, you can see now that we have two objects being
#  returned.

# Notes.objects.filter(title__startswith="My")
#  We can also filter notes that we want, for instance, we can query for the notes that have titles starting with the
#  word, my. Notes.objects.filter, for the title starts with the word My, yeah. The filter also returns a query set,
#  which in this case, returns the first object. We can also search by something that exists inside the notes, for
#  instance, we can try to find texts that contains the word Django.

# Notes.objects.filter(notes__icontains = 'Django')        we can try to find notes that contains the word Django

# Notes.objects.exclude(notes__icontains = 'Django')       We can also query for the opposite, we can actually filter
# notes by excluding them, so let's do the opposite notes.objects.exclude, notes that the notes contains the words
# Django.

# Notes.objects.filter(notes__icontains='Django').exclude(title__icontains='Django')
# The fun part is that query sets can also be filtered, meaning that we can add multiple filters at once, for instance,
# we can filter all the notes containing the word Django, but the title doesn't say anything about Django. Text contains
# the word Django, but exclude the ones where the title contains the word Django, there you go. As you can probably
# imagine, we can go on and on here with thousands of examples on how to query data. Django's ORM has a very neat
# interface that is very intuitive and yet highly powerful.

#