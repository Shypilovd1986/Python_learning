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
# from django.contrib.auth.decorators import login_required
# @login_required()
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

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
#  register that  model is attached to this admin model. So let's write admin.site.register, then models.Notes, and
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

#                       Creating a dynamic template
#                       views.py in folder notes
# #from django.shortcuts import render
# from . models import Notes
#
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

#          urls.py in folder notes
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('notes', views.list),
# ]
#               urls.py in main folder
#
#                from notes/templates/notes/notes_list.html
# urlpatterns = [
#     path('project_admin/', admin.site.urls),
#     path('', include('home.urls')),
#     path('smart/', include('notes.urls')),
# ]

# <html>
#     <h1>These are the notes</h1>
#     <ul>
#         {% for note in notes %}
#             <li>{{note.title}}</li>
#         {% endfor %}
#     </ul>
# </html>

# Everything that is between curly brackets is the Django template language logic. Here we're opening a list tag ul, and
# then saying that for each note we receive in the template, DTL should create a list item, the li. Notice that commands
# such as the loop happen between curly brackets and percentages, while things that should be rendered by the template
# are between double brackets.

#
#                                       Display content of a single note
#
# Let's go back to the notes app, views.py and let's create a new function here. Now, this function should receive a
# second parameter called pk for private key.

# Okay, so there's one thing still missing, which is the URL. This needs to be a slightly different URL because we need
# to be able to pass down the second parameter to that function. So let's do this by adding a new path here. So we're
# going to have notes, then slash, the minor and greater sign, and pk. Great, and now the views.detail. Okay, so what
# we're telling here is that URL will receive a new value named pk that will be an integer number.

#                   urls.py in notes folder
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.list),
#     path('notes/<int:pk>', views.detail),
# ]
# Django has an amazing traceback for us to understand where exactly the error happened. You can see right here that the
# problem started in line 11 on the notes, views.py file, which is exactly where we define the query. We only have this
# page explaining the error again because we continue to have the debug equals true in the settings file. In a
# production environment, the user would see a 500 error, which means an internal error. When an object is not found,
# the correct response is a 404 status code saying that that object does not exist. So let's change our code to make
# sure that we get the correct status code. Let's go back to the views file. And in here, let's import from django.http.
# Let's import Http404. Okay, and now we can wrap this query in a try and except block. So try and except if the Notes.
# DoesNotExist equals true, we're going to raise an Http404 with the message Note doesn't exist.

#                   views.py  from notes folder
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})


#                   Introduction to Django class-based views
# However, Django has a couple more features that we can leverage to get things even simpler. Welcome to class-based
# views.
# The first view we made was in the home app, so let's go back and change it. The only thing we need to do here is
# display a template, so we can do that by using the class-based view TemplateView class. So let's in here import from
# django.views.generic import TemplateView. Okay, so now we can create a new class called HomeView that inherits from
# TemplateView, and the only thing we need to pass here is the template name.

# We still need one more thing because our template requires some extra information

#  The last thing missing is that we need to change the way the URLs are defined, so let's go to the URLs, and in here,
#  instead of passing the home function, we're going to pass the HomeView class and we need to call a method called as
#  _view.

#  How do we handle authentication on class-based views? Well, to do that, we're going to need a mixin class. Mixins are
#  helper classes that can be used along with other classes to provide additional features. For this case, we'll use the
#  LoginRequiredMixin.

#  The only thing we need to do here now is make sure that this class, which is a mixin, is added before the
#  TemplateView, okay? The last thing missing is the login_url. So we can actually go here, add the login_url. Let's
#  still pass the admin, and that's it

#               from views.py in home folder
# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView
#
# class HomeView(TemplateView):
#     template_name = 'home/welcome.html'
#     extra_context = {'today': datetime.today()}
#
# class AuthorisedView(LoginRequiredMixin,TemplateView):
#     template_name = 'home/authorized.html'
#     login_url = '/admin'

#                   from urls.py in home folder
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('home', views.HomeView.as_view()),
#     path('authorized', views.AuthorisedView.as_view())
# ]


#   xxxxxxxxxxxxxxx             A bit more on class-based views        xxxxxxxxxxxxxx
#  Okay, now I can start our class-based view. Let's go to create a class. So let's call it NotesListView, that inherits
#  from ListView. And we need to add here, which model we're listing objects from. So let's add here a model equals to
#  notes, okay. And because our template is expecting to receive a list called notes, we should also add here that the
#  context object name is different from the default. The default is objects, but we call it notes. That's it, that's
#  our whole end point. The only thing we need to do now is change the end point URL. So let's go back here, then change
#  lists to NotesListView.as_view and that's it. We can go back here and also delete our old endpoint.

# You may be thinking what's happening here? Where is the query? The list view is already making the query for us. We
# also don't need to define the template name because we created a template name that follows the standard of that class
# based view. But if we enter a different name, it might not work. So instead we can pass here an attribute called
# template name, you guessed correctly. So we can say here, notes/notes_list.html.

#                   urls.py from notes directory
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view()),
#     path('notes/<int:pk>', views.NotesDetailView.as_view()),
# ]

#                   views.py from  folder home
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, DetailView
#
# class NotesListView(ListView):
#     model = Notes
#     context_object_name = 'notes'
#     template_name = 'notes/notes_list.html'
#
# class NotesDetailView(DetailView):
#     model = Notes
#     context_object_name = 'note'

# xxxxxxxxxxxxxx            Static files in Django       xxxxxxxxxxxxxxxxxxx

# The first thing we need to do is create a folder where we're going to store all the static files, such as the CSS and
# JavaScript files, images, videos, et cetera. So let's go here and create new folder, static. Now we need to tell
# Django that this is the folder it needs to look into when searching for static files. To do that, let's go to the
# smartnotes, then settings. Then in here, we can scroll down a little bit, and we're going to see here that there is a
# STATIC_URL already. Now we're also going to add STATICFILES_DIRS. This should be a list. And in here, we're going to
# say BASE_DIR / 'static' which will lead Django to the folder we just created. Okay, now we can go back to the static
# and create a new folder just for the CSS files and one CSS file. Let's call it style.css.

#               from settings.py in main-name directory
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     BASE_DIR/'static',
# ]

# . What we need to do now is make sure that our template and Django per se recognizes this file. So let's go to the
# notes and let's try the notes_list file. Okay, in here, the first thing we need to do is actually tell Django that
# this HTML is going to use the static files.

# So let's go to the notes and let's try the notes_list file. Okay, in here, the first thing we need to do is actually
# tell Django that this HTML is going to use the static files. So let's go curly brackets, percentages, and load static.
# Okay, now what we need here is to add a CSS file as we would in any HTML file, so let's create a head then a link, so
# the rel is going to be stylesheet, the type is going to be text/css, and on the href, we're going to use the Django
# template language to add our URL. So let's call static, then css/style.css. That's it. That's all we need to do to
# have the CSS being rendered on this file.

#               from style.css in folder static/css which we created
# .note-li{
#     color: red;
# }

#                           from notes_list.html (we add some style, in this case red colour)
# {%load static%}
# <head>
#     <link rel="stylesheet" type="text/css" href="{%static 'css/style.css' %}"/>
# </head>
# <html>
#     <h1>These are the notes</h1>
#     <ul>
#         {% for note in notes %}
#             <li class = "note-li">{{note.title}}</li>
#         {% endfor %}
#     </ul>
# </html>

#
# xxxxxxxxxxxxxxxx      How to set up a base HTML for every Django template       xxxxxxxxxxxxxxxxxxxxxxx

# What we need now is a base template. Let's create a templates folder in the static folder, and a base.html template in
# it. Okay, so in here, we can create a normal HTML file.

#  Okay, so I called this content, but you can call it whatever you like. The important thing here is to know that this
#  is a block area where we can inject things. Let's try it out.

# Let's go back to the notes, and open the notes_list template. So in here, what we can do is extends base.html. Now,
# what we can do is get rid of all this basic HTML stuff here and use this block content here. So block content, and in
# here, we can endblock. Okay, so what we're doing here, we're taking only the important part of our template, and
# wrapping it on the block content command so this can be injected on the base template.

# So what we need to do is tell Django what to look for. So let's go back. Then in here, let's go to settings file, and
# down below, we're going to find out that there is a templates, and there is a list of directories that we can add here
# So similar to what we did on the static files, we're going to add that particular folder in here. So let's do BASE_DIR
# and then slash, and then static/templates.

#                   from settings.py in main-name folder
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             BASE_DIR / 'static/templates'
#         ],

#      from base.html in folder static/templates
# {% load static %}
#
# <html>
#   <head>
#     <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
#   </head>
#   <body>
#     {% block content %}
#     {% endblock %}
#
#   </body>
# </html>

#       from notes_list.html    in folder notes/templates
# {% extends "base.html" %}
#
# {% block content %}
#     <h1>These are the notes</h1>
#     <ul>
#         {% for note in notes %}
#             <li class = "note-li">{{note.title}}</li>
#         {% endfor %}
#     </ul>
# {% endblock %}

#  What's happening here is that with this syntax, we can define the basics of our HTML in our base.html template, and
#  then we create each web page as a separate template that extends the base. So we will build each template separately
#  and just the small parts but we'll then inject it to the base template where we can have all our default
#  configurations, such as the CSS files and the JavaScript. This will allow us to keep each web page template as simple
#  as we can while keeping all the configuration in a single place. That's another power of the Django template language

#   xxxxxxxxxxxxxxxxx       Let's add some style               xxxxxxxxxxxxxxxx

# . We're going to use Bootstrap for now, so what we need to do is on the static, base.html, I'm going to change this
# CSS we just created with the link to the Bootstrap framework version five. So we can go back, delete this line, and
# that's it. I know it's a pretty big link, so you can find it on the notes of this class.

# So let's add a button on the home page that will lead us to the list of notes. So let's go to home. Welcome. Perfect.
# Here we can add, so it's going to be an a href. Let's leave it empty for now. Then in here, we're going to use two
# classes. Btn for button and btn-primary for the style.

# So how do we deal with links here? We could hard code the link to our localhost but imagine that when we deploy our
# website, we need to remember to come back and change everything. Not so good. Thankfully, the Django template language
# has a function for that. What we need to do is the following. Let's open curly brackets and percentage, and then use
# url, and then in here we're going to say notes.list. Okay, you might be wondering, okay, how Django knows which
# endpoint to link? It doesn't, and we need to tell it. So let's go back to notes, urls, and in here, what we're going
# to do is add a name. So we can give a name notes.list. That's all we need for Django dynamically define each endpoint
# we are pointing to, no matter if you're on localhost or production.

# This would look a little bit better if we could display some of the text of a note but not all of it. We can use the
# truncatechars function to do this.

# Okay, so it's still missing a couple of things, so we can't really access all the details of that particular note. So
# we're almost there. First, let's give a name to the detail URLs as well. So let's go back. Urls.py

#           urls.py from notes folder
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view(), name = "notes.list"),
#     path('notes/<int:pk>', views.NotesDetailView.as_view(), name = "notes.detail"),
# ]
#
#                   notes_detail.html
# {% extends "base.html" %}
#
# {% block content %}
# <div class = "border round">
#   <h1 class = "my-5">{{note.title}}</h1>
#   <p>{{note.notes}}</p>
# </div>
# {% endblock %}

#           notes_list.html
# {% extends "base.html" %}
#
# {% block content %}
#     <h1 class="my-5">These are the notes</h1>
#
#     <div class ="row row-cols3 g-2">
#         {% for note in notes %}
#         <div class="col">
#             <div class = "b-3 border">
#                 <a href="{% url 'notes.detail' pk=note.id  %}" class ="text-dark text-decoration-non" >
#                     <h3>{{note.title}}</h3>
#                 </a>
#                 {{note.notes|truncatechars:15}}
#             </div>
#         </div>
#         {% endfor %}
#     </div>
#
# {% endblock %}

#               base.html
# {% extends "base.html" %}
#
# {% block content %}
#
#     <body><h1>Welcome to SmartNotes!</h1></body>
#     <h3>Today is {{today}} </h3>
#     <a href="{% url 'notes.list' %}" class="btn btn-primary">Check out these smart notes</a>
#
# {% endblock %}

#   xxxxxxxxx     Create a webpage     xxxxxxxxxxxx
# Let's go back to notes, views.py and in here, let's import, well, I hope you guessed it, CreateView. Once we have this
# we can actually start our new class. So class NotesCreateView that inherits from CreateView

# . Let's understand what's going on here. First the model. So the endpoint understands what it's regarding to. Then the
# fields would be the attributes from the model that we allow a user to fill. Since we don't need to pass a created add
# field, we just define it as title and notes. Finally, we want to redirect the user to the list of existing notes so
# they can see the note they just created. This is the success_url attribute here.

# Now we can add the endpoint to the urls.py file, the same way we did to every other endpoint so far. So in here, let's
# add path. Then notes/new. And then we can call view.NotesCreateView.as_view. And let's not forget to pass a name to it
# So notes.new.

# Okay, so the last thing that's missing is the template. So let's create it. Let's call it notes_form.html.

# To send information back to the server, we'll need a form tag from the HTML. So let's add this here. Okay, so in the
# form, we can do action is equal to, we're going to use the method url, and then notes.new, which is the endpoint we
# just created. And also, the method here needs to be POST because we're sending information back to the server. Okay,
# so now what we need is to allow a user to pass back the information we define on our endpoint: title and notes.

#  So in here, we can open the inspector element, and you can see here that in the body, we have a form. And the form is
#  actually passed down to the HTML as two label tags and one input tag, and one text area. This is because Django
#  already knows which type of data each attribute expects. Thus it creates an appropriate HTML tag to receive it. Well,
#  we're still missing the Submit button, so let's add that. So in here, let's add button of type submit. The class is
#  going to be btn btn-primary. Let's add some vertical alignment. Submit.

# xxxxxxxxxx     Understanding how Django handles security in POSTs     xxxxxx
#
#  We did everything we needed to do to implement the create endpoint, but if you try to create a new note, you'll
# notice that it will actually return a 403 error, meaning that we are forbidden to do this action. Well, we're actually
# missing one less thing to our form. So if we go here, we can add curly brackets, percentage, and then a csrf_token.

#  This is a CSRF token, that stands for cross-site request forgery. What happens here is that every time a browser
#  requests a webpage that has a form, Django will send a unique token to that browser. This token will be securely kept
# and no other website can access it. When the user sends back a form, it will also send back the token, allowing Django
# to know that this request is coming from a legit user. Django will then process the request and return the appropriate
# response. However, if for some reason, a third-party have access to the user credentials, when they try to make the
# request from another browser, they won't have the token, so Django understand that this request is coming from an
# unreliable source and will not process the request, thus, preventing this type of attack. As you can see, this is an
# additional layer of security that Django is adding to your website with just a small line of code. Beyond the numerous
# features that allow you to speed up the process of creating a website, this security features are a big part of why
# developers choose Django to work with.

#                   notes_form.html in notes/templates/notes directory
# {% extends 'base.html' %}
#
# {% block content %}
#
# <form action="{% url 'notes.new' %}" method="POST"> {% csrf_token %}
#     {{ form }}
#     <button type="submit" class="btn btn-primary my-5">Submit</button>
# </form>
# {% endblock %}

#               urls.py in notes directory
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view(), name="notes.list"),
#     path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
#     path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),

#               views.py in notes directory
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView
#
# class NotesCreateView(CreateView):
#     model = Notes
#     fields = ['title', 'notes']
#     success_url = '/smart/notes'
#
#
# class NotesListView(ListView):
#     model = Notes
#     context_object_name = 'notes'
#     template_name = 'notes/notes_list.html'
#
# class NotesDetailView(DetailView):
#     model = Notes
#     context_object_name = 'note'

# xxxxxxxxx    Django forms: Powerful validation with minimal work        xxxxxxxxx

#  Model forms are the best way of doing this in Django. Let's check it out. First, we're going to create a file called
#  forms, and inside our notes app.

#  Okay, with this, we can come back to the views.py file, and in here, instead of passing the fields, we're going to
#  pass a form_class that's going to be our NotesForm. We also need to import it.

# Okay, so far what we did will result in exactly the same behavior as we have so far but the form will give us power to
# do much more. For instance, let's say that we want to add a specific behavior that just allow us to add notes that
# contains the word Django in the title.

#  Let's go back to the forms. All we need to do here is add a new method called def clean, and the field, we want to
#  add a validation. In this case, title. So in here, we can get the title from the cleaned_data, which is a dictionary.
#  The cleaned_data is returned by the form, and is particularly useful for fields with strong validation. Like for
#  instance, emails. In this scenario, it will be exactly the same value as the user passed. With this, we can actually
# start our validation. So if Django not in title, we're going to raise a ValidationError with a message. We only accept
# notes about Django. If everything goes well, we just return title.

# We can go back and on our style.css, we can add here that the ul.errorlist is not going to be displayed. So we're
# going to control this.

#                   notes_form.html from templates/notes directory
# {% extends 'base.html' %}
# {% block content %}
#
# <form action="{% url 'notes.new' %}" method="POST"> {% csrf_token %}
#     {{ form }}
#     <button type="submit" class="btn btn-primary my-5">Submit</button>
# </form>
# {% if form.errors %}
# <div class="alert alert-danger my-5 ">
#     {{form.errors.title.as_text}}
# </div>
# {% endif %}
#
# {% endblock %}

#       style.css from static/css directory
# note-li {
#     color: #ff0000;
# }
#
# ul.errorlist {
#     display:none
# }

#     from forms.py in notes directory
# from django import forms
# from django.core.exceptions import ValidationError
# from .models import Notes
#
# class NotesForm(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ("title", "notes")
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if 'Django' not in title:
#             raise ValidationError('We only accept notes about Django')
#         else:
#             return title

# xxxxxxx     Django forms are useful for layout as well!      xxxxxxxxxx

# . First, let's say that we want to change the labels of our form. Title and notes are the words we use in the backend,
# but that doesn't mean that it looks so good for our users. What we can do is, on the class meta, add a field called
# labels, and in here, let's add text, it's going to be, write your thoughts here.

# We can also add an attribute widget to inject CSS classes directly to the form. Let's go back and add a new field code
# widgets, and then, in here, let's add title, and this is going to be a forms text input, and then we're going to pass
# attributes.

#  You can see now that controlling the frontend in an easy and accessible way is also a main advantage of using model
#  forms. All this without ever changing the original template. Nice and easy.

#    from  forms.py
# from django import forms
# from django.core.exceptions import ValidationError
# from .models import Notes
#
# class NotesForm(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ("title", "notes")
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
#             'notes' : forms.Textarea(attrs={'class' : 'form-control my-5'})
#         }
#         labels ={
#             'text': 'Write your thoughts here'

#      views.py in notes directory
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
# from .forms import NotesForm
#
# class NotesUpdateView(UpdateView):
#     model = Notes
#     form_class = NotesForm
#     success_url = '/smart/notes'

#
# xxxxxxxxxxxxxxx     The U in the CRUD: Updating data          xxxxxxxxxxxxxxxxx
#
# ] Okay, so now we have the create end point, it's time to create the view update endpoint. Let's go back to the views
# file on notes. And on here, we're going to also add UpdateView. Now we can add a new class, NotesUpdateView that
# inherits from UpdateView. And we actually just need to copy these from the CreateView and paste it here. That's it,
# that's all we need to do. The only thing still missing are the URLs. So what we can do is go back here, we can copy
# and paste the details view, and then add here a /edit on the end point, change the class where is this originating to,
# and the name.

#  If you go to our template, if you notice here, we're actually hard coding which URL the form should be sent to. We
#  don't actually need this. The form is smart enough to know where to send this to. So let's get rid of this. Let's go
#  back, edit, and then submit it. If we see now, our note was edited. That's it. So editing basically comes for free
#  after you implemented the create end point.

# We can style this page a little bit, so let's go to the template. We can add a cancel button that will return from
# this page if the user changed their mind. So it can go to a href is going to be the function that have URL, and then
# let's go back to notes.list. We still need some class here, so let's type btn and then btn-secondary, and then Cancel.
# We can also go back to the details. In here we can create a new button that will take us to the edit page, so a href,
# then curly brackets, percentage url, notes.update, and then pk is equal to note.id. Let's add some class here as well,
# so btn and btn-secondary, Edit.

#      from notes_form.html
# {% extends 'base.html' %}
#
# {% block content %}
#
# <form  method="POST"> {% csrf_token %}
#     {{ form }}
#     <button type="submit" class="btn btn-primary my-5">Submit</button>
# </form>
# {% if form.errors %}
# <div class="alert alert-danger my-5 ">
#     {{form.errors.title.as_text}}
# </div>
# {% endif %}
# <a href="{% url 'notes.list' %}" class=" btn btn-secondary">Cancel</a>
#
# {% endblock %}

#           notes_detail.html
#
# {% block content %}
# <div class = "border round">
#   <h1 class = "my-5">{{note.title}}</h1>
#   <p>{{note.notes}}</p>
# </div>
#
# <a href="{% url 'notes.list' %}" class="btn btn-secondary my-5">Back</a>
# <a href="{% url 'notes.update' pk=note.id %}" class=" btn btn-secondary my-5">Edit</a>
# {% endblock %}

#         url.py from notes directory
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view(), name="notes.list"),
#     path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
#     path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
#     path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
# ]

#                   views.py from notes directory
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
# from .forms import NotesForm
#
# class NotesUpdateView(UpdateView):
#     model = Notes
#     form_class = NotesForm
#     success_url = '/smart/notes'

#     xxxxxxxxxx      The D in the CRUD: Deleting data           xxxxxxxxxxxxx

# Let's start as usual. Let's go back to the views and from here, we're going to add actually from Django views generic
# edit, let's important delete view. The delete endpoint is even simpler than all the endpoints we created until now. We
# can add a new class notes delete view that inherits from delete view, and we actually just need the model and a
# success URL. Once more, the end point URL needs to be added to the URL's file.

#

# Once more, the end point URL needs to be added to the URL's file
#                   urls.py from notes directory
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view(), name="notes.list"),
#     path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
#     path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
#     path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
#     path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
# ]

# No, we need to create a template to confirm if the user wants to delete a particular note.
# So let's add form and the methods going to be post. Since this is a form we can forget about the CSRF underlying token
# and then in here, we're going to add a message.

#  So it can be a nice red and value it's going to be confirm. Since we already have our template, we can go back to the
#  details and add yet one more button here called that will lead us to the delete. Let's make it red as well.

#  Okay, it's time to try it out. Let's go back to one particular note. Now we have the delete button and if we click
#  here, oh-oh, okay. We're getting again a template does not exist. We can see here that while it was loading the
#  template, it was looking for a template with the name notes, notes, confirm delete. So we have two alternatives here.
#  One is to change the name of our template to match the template that Django is expecting. I prefer to usually add the
#  template name to avoid having to remember which template is related to which endpoint. So we can come back here to
#  the views and add a template name. This name is also very similar to the other template names that we have. So, in my
#  opinion, this is a little bit better, but you can choose whatever you prefer.

#                        views.py    from notes directory
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
# from .forms import NotesForm
# from django.views.generic.edit import DeleteView
#
# class NotesDeleteView(DeleteView):
#     model = Notes
#     success_url = '/smart/notes'
#     template_name = 'notes/notes_delete.html'
#
# class NotesUpdateView(UpdateView):
#     model = Notes
#     form_class = NotesForm
#     success_url = '/smart/notes'
#
# class NotesCreateView(CreateView):
#     model = Notes
#     form_class = NotesForm
#     success_url = '/smart/notes'
#
#
# class NotesListView(ListView):
#     model = Notes
#     context_object_name = 'notes'
#     template_name = 'notes/notes_list.html'
#
# class NotesDetailView(DetailView):
#     model = Notes
#     context_object_name = 'note'

#     notes_delete.html from temlates/notes directory
#

#                   urls.py  from notes directory
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('notes', views.NotesListView.as_view(), name="notes.list"),
#     path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
#     path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
#     path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
#     path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
# ]

#                   notes_detail.py
# {% extends "base.html" %}
#
# {% block content %}
# <div class = "border round">
#   <h1 class = "my-5">{{note.title}}</h1>
#   <p>{{note.notes}}</p>
# </div>
#
# <a href="{% url 'notes.list' %}" class="btn btn-secondary my-5">Back</a>
# <a href="{% url 'notes.update' pk=note.id %}" class=" btn btn-secondary my-5">Edit</a>
# <a href="{% url 'notes.delete' pk=note.id %}" class=" btn btn-danger my-5">Delete</a>
# {% endblock %}

#  !!!!!!!!!!!!!!!!!    ForeignKey: How models relate to each other       !!!!!!!!!!!!!
#
# Right now, no matter if a user is logged into an account, they can create notes on the system. However, we want the
# system to be aware of who's logged in and only display the notes written by their original author. How can we do that?
# So far, we have two tables in our database, the notes table and the user table. We need to save in the notes which
# user was the author, and we can do that by creating a link between the user table and the notes table. This is what we
# called a foreign key.

# Let's go back to our model and import the user model that comes with Django by default. So from django.contrib.auth.
# models import User. Now we go to the Notes model and we add a foreign key. Now we go here and we add models.ForeignKey
# This here needs a couple of things. The first item is the model we want to create a link with. In this case, this is
# the User model we just imported. Then, the second item is going to be the on_delete. This means that we are want
# define what happens to this note if the user associated with it is deleted. In this case, we're going to use models.
# CASCADE, which means that if a user gets deleted, we also want to delete all the notes associated with them. Finally,
# we can say how we will identify this relationship on the user side. Related_name is going to be notes.

# Okay, now that we changed the model, we need to create a migration. Let's go and type python managed.py makemigrations
# and we're getting an error. The problem here is that we defined that every node needs to be associated with a user,
# but our database is already fully populated by notes without users, so we need to define what to do now. Since we have
# a user admin and it's ID is 1 we can pass this as the default user on this migration. If we pass any ID of a user that
# doesn't exist, this migration will fail, so we should pass an ID of a user that exists. Let's add one. We're going to
# provide a one-off default, and the ID is going to be 1. Okay, so now we can actually apply the changes to the database
# with python manage.py migrate.

#  python manage.py makemigrations
#  python manage.py migrate

#  Let's test our implementation and see if it works by opening the shell, so python manage.py shell. And let's import
#  the user, from django.contribute.auth.models import User, and let's get the first user. So user is going to be User
#  objects get pk is equal to 1. So this is the admin user that we've been using so far. What we can do now is actually
#  see the notes that this user has, so we can count them. And we can see that all of the five notes that we have in our
#  system is associated to that user. We can even get all the notes from here. So if we say user.notes.all, we're going
#  to have all the object notes being displayed here. That's it. Now we can start making changes to make the system user
#  aware.

# python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> user = User.objects.get(pk=1)
# >>> user
# <User: admin>
# >>> user.notes.count()
# 3
# >>> user.notes.all()
# <QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>, <Notes: Notes object (3)>]>


#               models.py  from notes
# from django.db import models
# from django.contrib.auth.models import User
#
# class Notes(models.Model):
#     title = models.CharField(max_length=200)
#     notes = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

#
#  xxxxxxxxxx         Displaying only the logged user data      xxxxxxxxxxxxx

# We also didn't add any authentication, so in order to keep privacy, we need to fix that. So let's go back here on the
# Notes views.py, and import from django.contribute.auth.mixins let's import LoginRequiredMixin. Then on the ListView,
# we need to add the LoginRequiredMixin,

#  and let's not forget to add the login_url. So for now, this is going to be the admin. This login_url means that if a
# user tried to access the list view and it's not logged in, they will be redirected to the /admin instead of seeing
# a 404.

# so now what we need is to change the query, so we can only display the queries of the logged in user, but where is the
# query? As we discussed earlier, class-based views are highly powerful and yet highly changeable. We can use the
# documentation website to check for all of the methods that we have available and find out which ones we need to change
# to get the behavior we want.

# This is the website that I look for when I want to change a class-based view. It calls ccbv because it's called classy
# class-based views. You can see here that we can change the Django version we're using.

#  So let's go to the generic list and go to ListView. In here, you can see all the classes, the methods, the attributes
#  everything we can configure in this ListView class-based view.

#  Whenever a user go to the list end point, the first method that it will call will be the get method because we're
#  making an HTTP get request.

# However, we can quickly see that there is a method here that gets the object list by calling a method called
# get_queryset.

# This is the method that we need to alter in order to list only a user notes. If we go back to the code now, we can
# actually override the get_queryset method, and instead of returning whatever it is returning by default, we're going
# to return self.request.user.notes.all.

#                from views.py  notes folder
# from django.shortcuts import render
# from . models import Notes
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
# from .forms import NotesForm
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin

# class NotesListView(LoginRequiredMixin, ListView):
#     model = Notes
#     context_object_name = 'notes'
#     template_name = 'notes/notes_list.html'
#     login_url = '/admin'
#
#     def get_queryset(self):
#         return self.request.user.notes.all()

# xxxxxxxxxxxxxxxxx             Adding a new note after ForeignKey              xxxxxxxxxxxxxxxxxx

#  The problem is that we don't say in the form to consider the logged in user as the author of that note. So we need to
#  change this.

#  So in here on the creative view, we're going to override the method--Def form valid-- that receives a self and form.
#  The first thing it is that we need to get the object, which is going to be formed at safe, and then commit is equal
# to false. Now we're going to fill the object. So self.object.user is going to receive the request user. And then we're
# going to self.object.save. And finally, we need to return an HTTP response, redirect. And then this is going to get,
# self.get success URL.

#  Let's see, the HTP response redirect is already being imported from Django HTTP response.

# . Let's understand what's going on here. So the data is sent by the user, passed inside the form, which asks a simple
# question: is this data valid. To see if the data is valid, the form would call a couple of methods that have the title
# started with clean. So clean title, clean text, like the one we changed before. If something is wrong, the method is
# valid returns false, and the class-based view will raise an exception. On the other hand, if all checks clear, the
# data is stored in a variable called clean data. And when you call form.save, that will save the object directly in the
# database. And that's it. It all's happened very smoothly.

#  So what happens here is that when we pass title and text to the form, the method is valid returns through. Then the
#  form valid method will call the save and we will try to save to the database, but although the form is returning is
#  valid, is equal through the database is forbidding us to try to save a note without a user. That's where we get our
#  error.

# . What we did here was to get in the middle of it so we can inject the logged user as part of the object. We do this
# by passing the attribute commit equals false, that creates the object, but doesn't save it to the database. Then we
# have the object when we insert the user, and then we call save, successfully saving the note with that user to the
# database. As you can see, classmate's views can be changed as you please.

#               from views.py notes directory
# from django.shortcuts import render
# from . models import Notes
# from django.http.response import HttpResponseRedirect
# from django.http import Http404
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
# from .forms import NotesForm
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# class NotesCreateView(CreateView):
#     model = Notes
#     form_class = NotesForm
#     success_url = '/smart/notes'
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

# xxxxxxxxxxxxxxx        Adding login and logout pages          xxxxxxxxxxxxxxxxxxxxxx

# Although the admin login is nice, it can only be accessed by staff members of the system. So we need to create the
# authentication interface as well. Let's do this. So first, let's go to home, then views, and then let's import here
# from django.contrib.auth.views import LoginView. And then let's create a class called LoginInterfaceView that inherits
# from LoginView

#  And then let's create a class called LoginInterfaceView that inherits from LoginView. And in here, we only need to
#  define really one thing, the template_name. So let's go call it home/login.html. Okay, so we can forget about the
#  URLs, so let's do this now, so in here, let's add a login page that inherits from views.LoginInterfaceView.as_view.

#         views.py home directory
# from django.contrib.auth.views import LoginView
#
# class LoginInterfaceView(LoginView):
#     template_name = 'home/login.html'

#         urls.py   home directory
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('home', views.HomeView.as_view()),
#     path('authorized', views.AuthorisedView.as_view()),
#     path('admin', views.LoginInterfaceView.as_view())
# ]

# , so now we can create a template. So in here, let's add the new login.html. And in here, really all we need to do is
# extends base.html to get all our configuration, and then block content. And finally, endblock. Okay, so in here what
# we need is simply a form. This form should have method equals to post. Because this is a form with method post, we
# can't forget what our dear friend csrf_token. And then we're going to use form.as_p because it's going to be rendered
# as p tags in the HTML. That's the only difference. And finally, we're going to have an input. The type's going to be
# submit. Let's add some class here.

# The problem is that Django has a default system-defined configuration for the redirect, which leads to a page we don't
# have, which is this account profile page. Because this is a global definition, we should change this not in the
# class-based views but we should change it on the settings.

# Then let's go to smartnotes, settings, and then we can add it way below here. And we can add LOGIN_REDIRECT_URL is
# going to be /smart/notes. So this is where we're going to redirect the user after it is logged in.

#               from settings.py in main directory
# LOGIN_REDIRECT_URL = '/smart/notes'

#  so similarly, we also want a logout view, right? We don't want want to have to go to the admin to do this. So let's
#  add this real quick. So on the views again, from here, we're going to also import LogoutView. And similarly, we're
#  going to create a LogoutInterfaceView that inherits from LogoutView. And the only thing we need is the template_name

# from django.contrib.auth.views import LoginView, LogoutView
# class LogoutInterfaceView(LogoutView):
#     template_name = 'home/logout.html'


# . Okay, oh, yes, and we're missing the URLs, so let's do this. We're copying logout. And logout. And for the sake of
# organization, let's add names to these URLs, shall we? So this is going to be our home page. We can actually get rid
# of this. Our system doesn't really need this. Then we have login. And finally, logout.
#               urls.py home directory
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),
#     path('authorized', views.AuthorisedView.as_view()),
#     path('login', views.LoginInterfaceView.as_view(),name='login'),
#     path('logout', views.LogoutInterfaceView.as_view(),name='logout'),
# ]

#  let's add names to these URLs, shall we? So this is going to be our home page.

# !!!!!!  we can set logout redirect page in settings.py
#  # LOGOUT_REDIRECT_URL = '/login'

#
# xxxxxxxxxxxxxx        Adding a signup page         xxxxxxxxxxxxxxx
#
# Now that we have login and logout endpoints, it is time to create a signup page. So first, let's go to
# the home, views.py. And then in here, let's important from here, from django.views.generic.edit import CreateView. And
# let's create here a class called SignupView that inherits from CreateView.

# And let's create here a class called SignupView that inherits from CreateView. And so form_class is going to be
# UserCreationForm. So template_name can be home/register.html. And finally, the success_url that's going to be the
# notes list. Oh, the creation form is actually a Django function. So django.countrib.auth.forms. We can import
# UserCreationForm, amazing!

#                   views.py    home directory
# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
#
# class SignupView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'home/register.html'
#     success_url = 'smart/notes'

# . Let's create the template. Let's go to home, then New File, register.html.

#               register.html
# {% extends 'base.html' %}
#
# {% block content %}
#
#   <form method="post" style='text-align: left; margin:0 auto; width: 600px;'>{% csrf_token %}
#     {{form.as_p}}
#     <input class="btn btn-secondary" type="submit" name="Submit">
#   </form>
# {% endblock  %}

#
#  Well, the problem here is that we are allowing a logged in user, which was the admin user I was using here to go to
#  the signup page and create a new user. What we can do is make sure that only people that are not logged deemed can
#  access the signup page. We can do this quite simply by overriding the get method. And redirecting the user if they
#  are already logged in.

# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import TemplateView
# from django.views.generic.edit import CreateView
#
# class SignupView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'home/register.html'
#     success_url = 'smart/notes'
#
#     def get(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('notes.list')
#         return super().get(request, *args, **kwargs)

#
# xxxxxxxxxxxxxx        Finishing touches          xxxxxxxxxxxxxx

# base.html

# {% load static %}
#
# <html>
#   <head>
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
#   </head>
#   <body>
#     <nav class="navbar navbar-dark bg-dark">
#       <div class="ms-auto">
#         {% if user.is_authenticated %}
#         <a href="{% url 'logout' %}" class="btn btn-outline-light me-1" >Logout</a>
#         <a href="{% url 'notes.list' %}" class="btn btn-outline-light me-1" >Home</a>
#         <a href="{% url 'notes.new' %}" class="btn btn-outline-light me-1" >Create</a>
#         {% else %}
#         <a href="{% url 'login' %}" class="btn btn-outline-light me-1" >Login</a>
#         <a href="{% url 'signup' %}" class="btn btn-outline-light me-1" >Signup</a>
#         {% endif %}
#       </div>
#     </nav>
#     <div class="my-5 text-center container">
#       {% block content %}
#       {% endblock %}
#     </div>
#   </body>
# </html>