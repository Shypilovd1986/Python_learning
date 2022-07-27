# *********************        drawing   in  turtle    *******************
#
# import turtle
# screen = turtle.Screen()
# screen.bgcolor('cyan')    #set background of screen
# screen.title('Drawing line')
#
# my_turtle = turtle.Turtle()
# my_turtle.shape('circle')    #set shape of pointer
# my_turtle.pensize(7)  #set thickness of line
# my_turtle.forward(100)    #draw line
# my_turtle.left(90)     #change angle for 90 deegres
# my_turtle.penup()   # up pen from the screen , it will not write on the screen
# my_turtle.forward(100)
# my_turtle.pendown()  # down pen on the screen , it will write on the screen
# my_turtle.forward(100)
# my_turtle.back(50)  # draw line in back forward

# my_turtle.fillcolor('yellow')   #set color for filling objects
# my_turtle.begin_fill()          #begin filling
# my_turtle.circle(50)
# my_turtle.end_fill()            #end filling
#
# my_turtle.color('purple')   # change color of drawing
#
# my_turtle.left(90)
# my_turtle.forward(50)
#
# for line in range(0,8):
#     my_turtle.forward(50)
#     my_turtle.back(50)
#     my_turtle.left(45)
#
# turtle.penup()
# turtle.goto(200,200)
# turtle.pendown()
# my_turtle.hideturtle()   #hide your turtle so that you don't have it showing anymore.
# turtle.done()  # end your program

# a = input()

# *************************     example with annotation    *******************

# def summ (a: int, b: int) -> int:
#     c:int = a+b
#     return c
# d = summ(2,3)
# print(d)

# In general, annotations for parameters take the form of optional expressions that follow the parameter's name.
# The second way of using these is within function return types, which are represented using the arrow operator after a
# function's parameter list.
# And the third is variable assignment to tell a Python runtime what type of variable it's expected to be.

# ************************    only for python 3.10    ****************
# def http_error(status):
#     match status:
#         case 400:
#             return "bas request"
#         case 404:
#             return "not found"
#         case _:
#             return "something wrong with internet"

# ************************       creating class      ************
# class Vehicle():
#     def __init__(self, type_of_vehicle):
#         self.type_of_vehicle = type_of_vehicle
#
# class Car(Vehicle):
#     def __init__(self, model, car):
#         super().__init__(car)
#         self.model = model
#
#     def drive_left(self):
#         print(f'{self.model} drives left')
#
# if __name__ == '__main__':
#     Mercedes = Car('Mercedes', 'Carr')
#     print(Mercedes.model, Mercedes.type_of_vehicle)

# ******************      working with files       ************************
#
# if __name__ == '__main__':
#     with open(r'C:\MPP\test_file.txt', 'w') as list_of_purposes:
#         list_of_purposes.write('It was very good day \n')
#         print(list_of_purposes.mode)
#
#     with open(r'C:\MPP\test_file.txt', 'a+') as list_of_purposes:
#         list_of_purposes.write('some good things might happens')
#
#     with open(r'C:\MPP\test_file.txt', 'r') as list_of_purposes:
#         text = list_of_purposes.readlines()
#         for i in text:
#             print(i)

# ******************      working with os, path, time      ************************

#  So this module gives us the ability to work with operating system related features.
# import os
# from os import path
# import time
# from datetime import date, datetime, timedelta
#
# print(os.name) # show name of operating system
# print('Is path existing? ', path.exists(r'C:\MPP\test_file.txt'))
# print('Is it file? ', path.isfile(r'test_file.txt'))
# print('Is it directory? ', path.isdir(r'test_file.txt'))
# print('Full path of file is: ', path.realpath('test_file.txt'))  #show full path for file or
# # path.relpath()('test_file.txt'))   if we need relative path
# print(path.split(path.realpath('test_file.txt')))  # split on path and name
# t = time.ctime(path.getmtime('test_file.txt'))  #show last modification time of file
# print(t)
# print(datetime.fromtimestamp(path.getmtime('test_file.txt')))
# current_time = datetime.now()  # current time
# print(current_time)

# ******************      working with  filesystem shell methods      ************************

# import os
# from os import path
# import shutil
# print(path.exists('test_file.txt'))
# from zipfile import ZipFile
# def main():
#     if path.exists('test_file.txt'):
#         src = path.realpath('test_file.txt')
#         dst = src + '.bak'      # create new path
#         shutil.copy(src, dst)    #copy file from ther path src to path dst
#         os.rename('test_file.txt.bak', 'new_name_test_file.txt')  #rename file

# shutil.make_archive('test_archive', 'zip', "Path of directory")   #make archive with name
# test_archive and extension zip

# with ZipFile('testzip.zip', 'w') as newzip:      # make archive
#     newzip.write('Python_base.py')   #write file to archive
# list_files = os.listdir('C:/MPP/')  # make list of consistent in directory
# with open(r'C:/MPP/list_files.txt', 'w') as file_text:
#     for i in list_files:
#         file_text.write(i)
#         file_text.write('\n')

# os.mkdir('C:/MPPP')   # create directory
# print(os.path.getsize('Postman.py'))     #show size of file

# **************        working with date       *****************

# from datetime import datetime, date, time, timedelta
# today = date.today()
# print(today.day, today.month, today.year)
# list_of_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print('Today is ', list_of_day[today.weekday()])
# print(datetime.date(datetime.now()))
# print(datetime.time(datetime.now()))
# now = datetime.now()
# print(now.strftime('Current year is %Y, %a, %d, %B'))
# print(now.strftime('locale date and time is %c'))
# print(now.strftime('locale date is %x'))
# print(now.strftime('locale time is %X'))
# print(now.strftime('Current time is %I : %M : %S %p'))  # %p   - pm or %a  - am , %I - 12-hour format
# print(now.strftime('24-hour time is  %H : %M'))
#
# some_day = timedelta(days=230, hours=12, minutes=35)
# print(some_day)
# print(datetime.now()+timedelta(days=65))  #show date in 65 days
# print(now.replace(1993))    #replace year

# *************    working with calendar module     ***************

# import calendar
# c = calendar.TextCalendar(calendar.TUESDAY)
# str = c.formatmonth(2022, 4)
# print(str)

# str1 = c.formatyear(2022)
# print(str1)

# c1 = calendar.HTMLCalendar(calendar.TUESDAY)
# str1 = c.formatmonth(2022, 4)
# print(str1)
#
# for i in calendar.month_name:
#     print(i)
#
# print()
#
# for i in calendar.day_name:
#     print(i)

# ***********************      Fetching Internet data      **********************

# import urllib.request  # in order to make a request to a web server
# # this module provides the classes and code I need to make HTTP requests.
# def main():
#     weburl = urllib.request.urlopen('http://www.google.com')  #  This will give me back a web response object.
#     print('result code: ', weburl.getcode())
#     data = weburl.read()
#     print(data)
# main()

# ***********************      working with fibonacci      **********************

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(10))

# ***********************      working with json      **********************

# import json
# import urllib.request
#
# def printResults(data):
#     theJSON = json.loads(data) # use json module to load the string data into a dictionary
#
# def main():
#     urlData = 'https://www.linkedin.com/learning/python-decorators/what-are-decorators?autoSkip=true&autoplay=true&' \
#               'resume=false&u=106534538'
#     webUrl = urllib.request.urlopen(urlData)  #open the URL and read the data
#     print('result code: ' + str(webUrl.getcode()))
# main()

# from html.parser import HTMLParser     # for parsing html text
# import xml.dom.minidom
#
# def main():
#     doc = xml.dom.minidom.parse('name_of_file.xml')    #  So this will parse the XML file and create an in-memory DOM
#     # object that I can manipulate.
#     print(doc.nodeName)  # print node name of the document
#     print(doc.firstChild.tagName)   #  print tag name

#             syntax of all
# all(
#     condition(item)
#     for item in iterable
# )
# import string
# list_of_punctuation = string.punctuation
# print(list_of_punctuation)
#
# def contains_punctuation(input_str):
#     return any(char in list_of_punctuation
#         for char in input_str
#     )

