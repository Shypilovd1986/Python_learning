# ***********    module random    ***********
# from random import randint
# randint(1,200)  takes random numbers from range of values 1 - 200
# random()  returns random number from 0 to  1
# shuffle(a), shuffles mutable sequence a
#
# ************   os     *************
# import os
# - os.mkdir('C:\\m1')    -   create file m1
# - print(os.path.exists('C:\\m1'))   return True if file exists or False if not
# - print(os.getcwd())   switch to the terminal
# - os.path.splitext('name file'), split extension from file, return tuple with name and extension
# - os.path.abspath('file name')   return absolute path of file
# - os.walk('search directory')     shows all files and directories in search directory
# - os.path.join('root', 'file')    concatenate two values and return path tp the file
# - os.path.isdir('dir name ')     return True if dir name is directory
# - os.path.isfile('file name ')     return True if file name is file
# - os.mkdir('dir name')     create directory
# - os.path.split('htttp://google.com')    return tuple with  ('htttp:', 'google.com'), uses the path.split function
# to break apart the input URL into the head and tail.
# -
# --    learn urllib  library !!!



# *************      json       *****************
# import json

# JSON  -JavaScript Object Notation, A common use of JSON is to read data from a web server, and display the data in a
# web page. Применяется в веб-приложениях как для обмена данными между браузером и сервером (AJAX), так и между
# серверами (программные HTTP-сопряжения).
# !!!!!!!  use only double quotes not single
# str_json = строка из джейсона
# data = json.loads(str_json)   - переведет из строки джейсон в словарь
# new_json = json.dumps(data, indent=2) переведет словарь в строку джейсон


# with open('my.json', 'w') as file:
#     json.dump(new_json, file, indent=2)    создаст и запишет в файл джейсон нашу строку
# with open('my.json', 'r') as file:
#     data1 = json.load(file)               считает нашу строку из джейсона
# !!!!  decoding JSON -> Python
# object -> dict
# array ->list
# string -> str
# number(int) -> int
# number(real) -> float
# true -> True
# false -> False
# null -> None

# ***************       module  string         ******************

# check if password has number in it , careful digits is string '0123456789', if you are going to check in int ,
# we should transform to  str
# from string import digits
# class Account:
#     def __init__(self, password):
#         self.password = password
#
#     @staticmethod
#     def check_is_include_password(password):
#         for digit in digits:
#             print(digit)
#             if digit in str(password):
#                 return True
#         return False
# a1 = Account(323)
# print(a1.check_is_include_password(a1.password))

# ****************     platform   ************
# import platform
# print('This is python version {}'.format(platform.python_version()))   # print Python version


# ***************        testing module    ************
# if __name__ == '__main__': main()   run function main, if it's main module
#!/usr/bin/env python 3       - Shebang line, show path to interpreter, can be point as absolute path
