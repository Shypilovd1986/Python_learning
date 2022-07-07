#               Consist of course
#
# Learning objectives
# Working with logical and comparison operators
# Getting a list of numbers with the range() and list() functions
# Using mathematical functions such as round(), abs(), and pow()
# Calculating a given input's length
# Importing and using the math module
# Reading a user's command-line arguments
# Getting the current time
# Formatting dates and times with datetime
# Creating a timer
# Using urllib to get content from the Internet
# Using the JSON module to decode content

# Standard Library is built-in. An External Library is something you have to download separately from the internet. And
# usually, you're doing this to get some sort of special functionality.

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false

# NOT
# true --> false
# false --> true

# *******************      example 1      **********************
# isRaining = True
# isSunny = False
#
# if isSunny or isRaining:
#     print('The weather is fine')
#
# if not isRaining:
#     print('it\'s not raining')

# *******************      example 2      **********************
# mouse = 1
# kitten = 3
# tiger = 75
# if mouse < kitten and mouse < tiger :
#     print('Mouse is the most light')
#
# if mouse < kitten <tiger:
#     print('Kitten has middle weight')
#
# print('A'>'B', 'C'<'c', False < True)
#  The whole expression ultimately returns a Boolean value.

# firstName = 'Taylor'
# print(len(firstName))
# print(firstName.__len__())  # . And so why does this work for strings? Well, strings have a special property. We go
# "firstName.len," we see that it has the length property. And so because it has the length property, we can use the
# len built-in function. Now, since this is a built-in function, we can use different types of data as input.


#  And so we have print math.N-A-N, which stands for not a number. So this is a value, you could give something in your
#  program that's not a number.

# **********************          math         **************************

# import math
#
# print(math.nan)
# print(math.inf)  # We also have infinity
# print(-math.inf) #  negative infinity
# print(math.cos(math.pi/4))
# print(math.sin(math.pi/4))
# print(math.factorial(4))
# print(math.sqrt(23))  # square root
# print(math.gcd(52, 8))  # GCD stands for greatest common denominator,  This will give us the greatest common
# denominator between 52 and 8.
# print(math.radians(360)) # How many radians are in 360 degrees or a full circle? Well, it's 6.28, about.
# print(math.degrees(2.321))  # We could go print math.degrees to convert radians to degrees.

# *****************       random      ***************
# import random
#
# import random
# print(random.randrange(11)) # returns number between 0 and 10
# print(random.randrange(3,10))
# print(random.randint(1,11))
# lotteryWinners = random.sample(range(100),7)         #we'll have the method sample and inside of sample, we're going
# to put our population, which in this case is going to be a range between 0 and 99, so 100 numbers, and then we want
# to pick five of those numbers randomly. Then we'll go ahead and print them out, lotteryWinners, and we get five random
# numbers down here.
# print(lotteryWinners)  # --> [6, 27, 7, 3, 76, 80, 55]
# pets = ['kitten', 'dog', 'pig']
# print(random.choice(pets))
# random.shuffle(pets)   #returns none
# print(pets)
# random.shuffle(pets)
# print(pets)

# *****************       statistics      ***************
#  The statistics module allows us to calculate some common statistics, like the mean, mode, standard deviation, et
#  cetera, but it also allows us to do some more complicated things as well.

# import statistics
# mean -> average
# median -> midpoint
# mode -> most frequent value
# agesData = [10,14,16,12,10,11,13,10,12]
# print(sorted(agesData))
# print(statistics.mean(agesData))
# print(statistics.median(agesData))  #shows mid point in sorted sequence
# print(statistics.mode(agesData))
# print(statistics.variance(agesData)) #  Some more advanced statistic terms are variance and standard deviation.
# Variance stands for the average of the square differences from the mean.
# print(statistics.stdev(agesData))    # is square root of the variance

# *****************       itertools      ***************

# import itertools

#
# for x in itertools.count(50, 5):  # method count allows us to count from 50 in our case to infinity,  5 is step
#     print(x)
#     if x == 80:
#         break
#
# n = 0
# for c in itertools.cycle("Step "):  # method cycle allows us to cycle word, it's going to go on forever and ever so we
# need to add some kind of break statement
# in brackets have to be an any type of iterable
# print(c)
# if c == 't':
#     n += 1
# if n == 5:
#     break

#  Another thing we can do with itertools is infinitely repeat a certain value. And we're going to again do this with a
#  for loop.
# i = 0
# for r in itertools.repeat(23):
#     print(r)
#     i+=1
#     if i > 20:
#         break

# election = {1: 'Sem', 2: 'Bob', 3: 'Karen'}
# for p in itertools.permutations(election):  # This will give us all the possible orderings for the election.
#     print(p)
#
# for p in itertools.permutations(election.values()):  # This will give us all the possible orderings for value.
#     print(p)

#  Another thing we can calculate with itertools are combinations. However, before going into combinations, let's
#  review what they are. They are kind of like permutations in that they list a set of items, but for combinations,
#  no set has the exact same elements as another.

# colorForPainting = ['red', 'blue', 'yellow', 'brown']
# for c in itertools.combinations(colorForPainting, 3):  # 3 means 3 items of combination , less than count in iter
#     print(c)

# import sys
#  If you have an IDE that you're using, usually you can go into the configurations and add the command line arguments
#  that way. So here, if we go to edit configurations, we can go ahead and add our parameters here, and we're going to
#  have them be the same as they were in our command line, but strings, and so we'll have "1", "2",
# print('count of arguments', len(sys.argv))
# print('arguments are ', sys.argv) # What are those arguments? Well, we have the fact that this is the program that we
# are running and so it has kind of the file path for the program. And then we have the arguments that we put into
# the configurations  1, 2.

# in parameters we have to input without ,
# sys.argv.remove(sys.argv[0])    # remove 0 element from sys.argv which is a list
# print(sys.argv)
# sum = 0
# argList = sys.argv
# for arg in argList:
#     try:
#         number = int(arg)
#         sum+= number
#     except Exception:
#         print('not int value')
# print(sum)

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file

# *******************            example work with file           *********************
# st = '''
# Good day
# good weather
# good mood
# '''
# with open(r'C:\\proba' , 'w') as file:
#     file.write(st)
# print('file name is ' + file.name)
# print('mode of open is ' + file.mode)
# with open(r'C:\\proba' , 'r') as file2:
#     print(file2.read())
#     file2.seek(0)  #return to the beggining of file
#     print(file2.read(5))
#     print(file2.read(5))
#     print(file2.read(5))
#
# We've written all that we've wanted to in this file, but now let's read it. In order to read it, we must set the seek
# pointer back to zero and go through the file again. We can do this with a function called seek, or we can close and
# reopen the file and our Python program, which will reset the seek pointer for us automatically. Either way, say the
# seek pointer is back at zero, and we want to read the whole line we just wrote.

# **********************           module tempfile     **********************

# create a temporary file. To do this, we'll create a variable. So tempFile, which will hold our temporary file that
# we create and then to create the temporary file we'll access the module, so tempfile., and then the temporary file
# constructor there, and that will create our temporary file. Now that our temporary file is stored inside a tempfile

# import tempfile
#
# tempfile = tempfile.TemporaryFile()
# print(type(tempfile))
#  However, we're not done yet, and that's because this write method takes a bytes object, and here we have a string.
#  In order to turn the string into a bytes object, We add b here, and that actually turns it into a bytes literal. Now
#  that we've written something to the file, we'll need to go ahead and reset the seek pointer for the file. And so
#  we'll go tempFile.seek, set that pointer back to zero. So then we can read from this temporary file. And so to read
#  from it, we'll just go print, tempFile.read
# tempfile.write(b'What a wonderful day today')     #!!!! method write here have to take byte, so we put b before string
# tempfile.seek(0)
# print(tempfile.read())
# tempfile.close()

# **********************           module zipfile     **********************

# import zipfile
# zip = zipfile.ZipFile('MPP.zip','r')  #add our archive to variable
# print(zip.namelist()) #method namelist() shows content of archive

# for meta in zip.infolist(): # We have the metadata for f1 and we have the metadata for f2. And so you see that they're
#     # text files, you see the compression type, you see what has access to different modes.
#     print(meta)
# info = zip.getinfo('f1.txt')     # method getinfo show information about metadate of file
# print(info)
# print(zip.read('f2.txt'))        # show content of file
#
# with zip.open('f1.txt') as file:   # open file
#     print(file.read())
#
# zip.extract('f2.txt')     #extract one file
# zip.extractall()          # extract all files
#
# zip.close()

# **********************           module datetime     **********************
# import calendar
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now.date())
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.time())
# Notice some of these are methods and others are attributes. And so, date and time are methods because they're
# combining several attributes whereas these are single numbers because they're just showing the number. This can be
# super useful if you need to display the current time or date or year in your application.

#  We'll use something called shift time with the shift time method. It takes one string and what's in the string
#  determines how the contents of the now variable are displayed. First, we'll control how the day of a given week or
#  month is displayed. With %a, we can have an abbreviated day of the week with just Mon, Tues, Wed displayed. With %A,
#  we can show the full name of the day of the week. So Monday, Tuesday, et cetera. And we can also display the day as
#  the day of the month with %d. So if it was going to be the 10th day of the month, %d would translate to 10. Trying
#  this out, we'll go now.strftime %a, %A, and then %d. So this will display the abbreviated day of the week, the full
#  day of the week, and then the numbered day of the week.

# print(now.strftime('%a %A %d'))

#  We can also format the month. We'll write %b if we want the abbreviated name of the month, we'll write %B if we want
#  the full name, and %m if we want the number of the month.

# print(now.strftime('%b %B %m'))

#  we can also format time. We will have %H to display the hours, %M to show the minutes, %S to show the seconds,
#  and % for AM or PM.

# print(now.strftime('%H : %M : %S : %p'))

# If we only want two numbers for the year to be displayed, we'll use %y. If we want four numbers, we'll use %Y.

# print(now.strftime('%y %Y'))

#  Now we can use the timedelta class to get information about future and past times. To get access to it, we're going
#  to go ,timedelta, and that's because the timedelta class lives inside of the datetime module.

# tasteFuture = now + timedelta(days = 2) # now testDate holds information about the day two days from now.
# print(tasteFuture)           #!!! tasteFuture is an instance of datetime so we can use all methods of its
# tastePast = now - timedelta(weeks= 3)
# print(tastePast.time())      #!!! tastePast is an instance of datetime so we can use all methods of its
#
# if tasteFuture > tastePast:
#     print('Comparison work ')

# **********************           module calender     **********************

# cal = calendar.month(2022, 10)
# print(cal)
#
# cal2 = calendar.weekday(2022, 10, 12)   #show number of weekday in 2022 , 10 month , 12 day
# print(cal2)  # counting is going start from 0
#
# print(calendar.isleap(2024))

# # **********************           module time     **********************

# import time
# run = input('Starts ? >')
# seconds = 0
#
# if run in ('Yes','yes'):
#     while seconds <= 20:
#         time.sleep(1)
#         print(seconds, 'seconds')
#         seconds+=1

# # **********************           html.parser     **********************

#  in order to parse HTML code, we have to import the HTML parser module, and so to do this, we'll go from html.parser,
#  and from this parser we'll import the HTMLParser class.

# from html.parser import HTMLParser
#  # <h1>Hi there</h1>
#  # <--some coments-->
#  # <p>  opening paragraph tag
#  # </p> closing paragraph tag
# class HTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start tag: ", tag)
#         for attr in attrs:
#             print("attr:", attr)
#     def handle_endtag(self, tag):
#         print("End tag: ", tag)
#     def handle_comment(self, data):
#         print("Comment: ", data)
#     def handle_data(self, data):  #  And then we'll have the data, and then we'll just print out the data that we have
#         print("Data: ", data)
#
# parser = HTMLParser()
# parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")
# print()

# **********************           textwrap module     **********************

# import textwrap
#
# websiteText = """   Learning can happen anywhere with our apps on your computer,
# mobile device, and TV, featuring enhanced navigation and faster streaming
# for anytime learning. Limitless learning, limitless possibilities."""
#
# print("No Dedent:")
# print(textwrap.fill(websiteText))  # this method keeps beginning space, don't keep Enters
#
# print("Dedent")
# dedent_text = textwrap.dedent(websiteText).strip() # we'll see that it takes away this beginning space, but it keeps
# # the Enters or the words we entered on inside the body of the text.
# print(dedent_text)
#
#
# print("Fill")
# print()
# print(textwrap.fill(dedent_text, width=50))
# print(textwrap.fill(dedent_text, width=100))
#
# print("Controlling Indent")
# print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="          "))
#
# print("Shortening Text")
# short = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...") # We'll make the width, which is how
# # many columns or how many characters that we're going to go until we replaced the rest with the placeholder, and that
# # is going to be 15 here, and then we're going to go ahead and make the placeholder, which is going to be what comes
# # after our 15 columns or our 15 characters, and we'll make that just ....
# print(short)

# **********************           urllib.request      **********************
#  We are going to use the urllib module to get content from the internet.
# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

# import urllib.request  # its just a class which we are going to use
# import json
# import textwrap
#
# #  in this video, we are going to use the Google Books API. And so what's going to happen is we are going to give Google
# #  Books an ISBN number and then it's going to take that ISBN number and get some data on that specific book.
#
# with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
#     text = f.read()
#     decodedtext = text.decode('utf-8')
#     print(textwrap.fill(decodedtext, width=50))
#
# print()
#
# obj = json.loads(decodedtext)
# print(obj['kind'])
#
# print(obj['items'][0]['searchInfo']['textSnippet'])