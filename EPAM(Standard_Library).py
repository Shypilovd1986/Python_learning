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

import itertools

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
# zip = zipfile.ZipFile('MPP.zip','r')
# print(zip.namelist())

# for meta in zip.infolist(): # We have the metadata for f1 and we have the metadata for f2. And so you see that they're
#     # text files, you see the compression type, you see what has access to different modes.
#     print(meta)
# info = zip.getinfo('f1.txt')
# print(info)
# print(zip.read('f2.txt'))
#
# with zip.open('f1.txt') as file:
#     print(file.read())
#
# zip.extract('f2.txt')
# zip.extractall()
#
# zip.close()

# **********************           module datetime     **********************
# from datetime import datetime
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

