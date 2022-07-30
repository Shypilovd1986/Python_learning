# pip3 install pipenv     # So let's go ahead and make sure that we have Pipenv installed on our computer.

# pipenv install      #  Now, once that's finished we're going to go ahead and do a pipenv install and this is going to
# go ahead and get our directory up and running to be a Pipenv environment.

#  it creates a Pipfile and a Pipfile.lock that essentially holds all the different packages that we're going to be
#  working with here. Now what's great about Pipenv is that if we want to use our virtual environment and all the
#  different packages that we have there, we can say pipenv shell, and then we are instantly launched into this virtual
#  environment, right inside of that directory. And if we ever want to get out of this we can simply just type exit, and
#  we're back to the regular version of our terminal here.

# pipenv shell     #check on environment
# exit    # exit of environment

# pipenv install flask      # install flask
# flask     # you should see a little pop-up like this. This tells you some of the basics of Flask. This will confirm
# that it's on your computer

# export FLASK_APP=hello  # set FLASK_APP=hello   for Windows   # hello is name of our file where app was written
# flask run     #  say export, in all caps FLASK underscore app equal to and we need to give it the name of our file.
# So this is simply just telling flask, hey when you run, I want you to look for this name of file when you run the web
# server.

# a route simply just says, when someone visits this webpage, we should return back the following text. So here we're
# going to type at, lowercase app dot route and then we're going to specify which URL we want to create a route for.

# @app.route('/')
# def home():
#       return 'hello flask'

#  And in this case, we want one for the home page. So if we just do a single slash, this means that someone has visited
#  the base URL. And we want to provide some information. Next we have to give a name and a function for this route. So
#  we're going to saw def home to signify our home page here. Then this is just a regular Python function here. And
#  ultimately we just have to return back some sort of object to be displayed to the user. In this case, let's simply
#  just return a string.

# We have created a new flask project and inside of it created a flask app. In which we created one single route to say,
# if you go to the home page, return back the following text. Now if we mess with the URL at all, if we say, slash hello
# or something like that it's not going to find it. If we do a slash about, that's not going to work either. But if the
# user just simply goes to the homepage we do know what information to display there. And one last pro tip is that if
# you've ever seen this 127 number, it just simply means refer to the local machine, your computer that you're using to
# find this web content. This can also be replaced by local hosts up to you about how you want to specify either that
# number or local host. But thought you should be aware of those two being the same thing.

# 127.0.0.1:5000 == localhost:5000   the same

# Up to this point and time, we've been running our Flask app in a production environment. The big limitation of this is
# that any time we make a change to our code we have to manually go into our Terminal, hit Control + C, stop the server
# and then run it again. Now if we were to run our Flask app in a development environment, it would automatically notice
# any time changes are made to the code, and restart our server for us.

# export FLASK_ENV=development    #  we are inside the development environment.
#
# @app.route('about')
# def about():   # the name of the function and the name of the route, do not have to match.
#     return 'This is URL shortener'

#  Now one more pro tip about running the Flask application in the server. Let's go ahead and move back to the terminal.
#  Every time that you start a new terminal session and you want to test out your website, you have to specify what the
#  Flask environment is going to be, and also what the Flask app is going to be. However, if you'd like to save a step,
#  we can go back to our code editor, and rename our hello.py to app.py. Flask is smart enough to know inside of the
#  directory if there is a file named app.py, that that is the default app that it should be running.

# Now we are not able to specify that it should automatically be a development environment. So we're going to have to do
# a Control + C, and say, export, all caps FLASK_ENV and set this equal to development. But that does save us one step
# of always having to specify what the Flask app name is going to be.

# **************     Page templates in Flask with Jinja     *************

# !!!! we need to create folder templates where flask will be looking for our templates
# we need to import render_template  from flask it needs fr looking file in templates
# @app.route('/')
# def home():
#       return render_template('home.html', name_of_variable = 'Some name')

#  So this shows us that the code that we've written inside of home.html is displaying when someone comes to the route
#  of just simply a slash, meaning the home page. This templating functionality all comes thanks to Jinja. Now, Jinja is
#  this awesome template engine which is created by the same people that have created Flask. However, Jinja is used in
#  a lot of other projects than just Flask, it's pretty popular, and there's so many different options and functionality
#  that you can use with Jinja.

# in code of file home.html
# <h3> {{ name_of_variable }} </h3>    it will show name of variable which we specified at return

# *********************      Passing data into Flask apps with forms      ****************

#  And the reason for this is Flask by default has the security to say if you create a route, in this case our route for
#  the home page, our route for your URL it only allows GET requests. Now if we want to have something like a POST we
#  can, but we have to explicitly specify that. So here inside of your app.route we're going to provide one more
#  parameter and in this case, we're going to specify that we have other methods that we want to use.

#  url-of        we can use a new function called url_for which creates the URL for us based on the function name.

# ****************            Saving to a JSON file        *********************

#  And the first thing that we want to do is create a dictionary that can store the information. If you sort of think
#  abstractly about what we're doing, we want to save the code that the user has passed in. That short name as the key,
#  and then the value will be the URL that they ultimately want to get to.

# {%for message in get_flashed_messages()%}
# <h2>{{message}}</h2>
# {%endfor%}
# It's not technically Python code, it's jinjas own way of writing code. But inside of here we're going to be doing a
# for loop. And we're going to say for and we want message in and we want to do get_flashed_messages. Now this is a
# special name inside of the template that we'll check for to see if there are any messages. If they are they will be
# stored inside of this variable. Now the way to end this for loop is we've got to do a curly bracket with the two
# percentage signs in it and at the bottom of this, we're going to say endfor no spaces in that.

# app.secret_key = ''

# enctype = 'multipart/form-data'
#  we're going to have to make to this second form. So in the top form tag here on our second form, we're going to add
#  an extra field here called enctype, and make sure that it's set to multi-part slash form data. Essentially what this
#  says is that this form is allowed to have file uploads.

# from werkzeug.utils import secure_filename
#  Now this werkzeug is something that comes from the same people that have created Flask that has a lot of great
#  different tools inside of it. But this one in particular allows us to make sure any file that's uploaded we can check
#  and make sure that it's safe to save. And we get this werkzeug package because it is a dependency in Flask, so we
#  don't have to go ahead and manually bring that in, which is nice for us. So now that we have that secure file
#  function, we can come now and wrap up this F dot file name with a secure file.

# @app.route('/string:code')     #  And for this route, we're going to do a string and the regular slash to say, you
# know this is the start of the url. And then after this slash, we're going to do angle brackets. And inside of those
# angle brackets say, string colon code. And what this does is it says, look for after the first slash on the website,
# any sort of string and put it in a variable called code.

# ***********      Working with static files     * ***********

#  The first one is we have to create a directory in our project called static.
#  I want to make sure that there's a spot specifically for our users content, things that they have uploaded to us. So
#  inside of this folder, I'm going to right click and make a new folder, and the name of this folder is going to be
#  user_files.

# ****************        Implementing sessions and cookies          **********************

# if we want to use cookies, we have to import them up at the top, and we do that by adding to our long import line here
# session, and session allows us to access those cookies, so we'll go ahead and add that up at the top.

# ***************      WSGI servers and how they work           ************

# t I want to talk about something that gets thrown around all the time but you might not have great understanding of,
# and that is WSGI, which is short for web server gateway interface. WSGI is essentially a protocol for Python
# applications in order to serve websites in a uniform manner. Now that was a whole lot of words, let's talk about what
# that means practically. So within WSGI you have essentially frameworks and servers. Some examples of Python frameworks
# are going to be Flask, or Django. And some examples of servers are going to be things like Gunicorn, and uWSGI. And
# essentially what WSGI allows is to say if we have some sort of Python framework that wants to ultimately serve
# webpages, if it follows the WSGI format that means that any Python framework you choose can work with any compatible
# WSGI server, like Gunicorn, uWSGI, and there's a whole list of both sides of your framework and servers, I'm just
# sharing some of the most common. But essentially, WSGI is a protocol. It's not something special that you have to
# install. Flask and Django by default implement those, same as Gunicorn and uWSGI. So as we move forward and deploy our
# project, although we've written it in Flask we're going to integrate it with Gunicorn so that Gunicorn can ultimately
# be the one that's serving up our files.

# ***********        Deploy your Flask app with Gunicorn          **************

# flask run --host 0.0.0.0       So this essentially says, go and share this with the world, I want this to be available
# publicly. Now, assuming you don't have any firewalls on the server, and it's ready to serve this, you can see that
# it's running our website down there at the bottom at port 5000. And if we look at the very top of the terminal

# pipenv install gunicorn    if not in environment just pip install gunicorn
# sudo apt install nginx
# systemctl status nginx
