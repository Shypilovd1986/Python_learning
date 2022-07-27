#  A decorator is a callable that takes another function as an argument, extending the behavior of that function without
#  explicitly modifying that function. So a decorator has the ability to run additional code before and after each call
#  to a function that it wraps. This means that decorators can access and modify input arguments and return values.
from functools import wraps  # decorator which change __doc__ and __name__ in wrapper function

# ***********************      example     **********************************

# def my_decorator(func):
#     '''decorator function'''
#     @wraps(func)
#     def wrapper():
#         '''return F-I-B-O-N-A-C-C-I'''
#         print('+------------------+')
#         print('|                  |')
#         result = func()
#         print('    ', result)
#         print('|                  |')
#         print('+------------------+')
#         return result
#
#     # wrapper.__name__ = func.__name__
#     # wrapper.__doc__ = func.__doc__
#     return wrapper
#
#
# @my_decorator
# def pfib():
#     return 'Fibonacci'
#
#
# # pfib = my_decorator(pfib)
#
# if __name__ == '__main__':
#     print(pfib())

# *********************     html bold and italic tag     ***************

# def bold(func):
#     ''' Bold decorator '''
#
#     @wraps(func)
#     def wrapper():
#         result = '<b>' + func() + '</b>'
#         return result
#
#     return wrapper
#
#
# def italic(func):
#     ''' Italic decorator '''
#
#     @wraps(func)
#     def wrapper():
#         result = '<i>' + func() + '</i>'
#         return result
#
#     return wrapper
#
#
# @italic
# @bold
# def some_text():
#     return 'Fibonacci'
#
#
# if __name__ == '__main__':
#     print(some_text())

# code using args and kwargs
# def func(*args, **kwargs):
#     m = ''
#     s = func(*args, **kwargs)
#     for i, char in enumerate(s):
#         c = 'x' if start <= i < end else char
#         m += c
#     return m

# ***************     Decorators with *args and **kwargs    ***********

# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something before
#         result = func(*args, **kwargs)
#         # Do something after
#         return result
#     return wrapper
#
# @decorator
# def func():
#     pass

# *********************    using timer   ****************

# from time import perf_counter
# from functools import wraps
#
#
# def timer(func):
#    @wraps(func)
#    def wrapper(*args, **kwargs):
#        start = perf_counter()
#        result = func(*args, **kwargs)
#        end = perf_counter()
#        duration = end - start
#        arg = str(*args)
#        print(f'{func.__name__}({arg}) = {result} --> {duration:.8f}s')
#        return result
#    return wrapper
#
# @timer
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# if __name__ == '__main__':
#     fib(3)
#     fib(20)

# **********************         Decorators with *args and **kwargs        ***************
# *******************       Use decorators as a cache       ********************

# Python also has a built-in decorator for memorizing functions. This is LRU cache from functools.

from functools import update_wrapper, lru_cache

# class Count:
#     def __init__(self, func):
#         update_wrapper(self, func)  # the purpose of the update wrapper is to ensure that we have the correct doc string
#         # and name of the function.
#         self.func = func
#         self.cnt = 0
#
#     def __call__(self, *args, **kwargs):
#         self.cnt += 1
#         print(f'current count is {self.cnt}')
#         result = self.func(*args, **kwargs)
#         return result


#  Now, you might be interested to know that the order of the decorators does matter. So if you have the timer decorator
#  close to the function, like this, then we are just timing the runtime of our function fib. Now if we want to swap the
#  decorators around, so that LRU cache is closer to the function call, so I move LRU cache closer to the fit function,
#  now, we're timing the runtime of our function fib as before, plus, the time it takes to do the cache lookup. Now,
#  there isn't a huge difference in between these two. They're way quicker than not using a cache, but it's important
#  that we understand what we're doing.
# @lru_cache(maxsize=None) #  This indicates that there's no limit to the size of the cache.
# @Count
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# fib(10)
#
# **************************     create virtual environment     ****************
#
#  Now a good way to do this is to use a virtual environment, which is a copy of the Python interpreter into which you
#  can install packages privately, and this doesn't affect the global Python interpreter installed in your system. So
#  virtual environments are great because they prevent version conflicts in your systems Python interpreter.

#  !!!!!!!!!!!!!!!    for Windows
# mkdir flask_example
# cd flask_example
# python -m venv venv_name
#  .\venv\Scripts\activate    #to activate venv

#  !!!!!!!!!!!!!!!    for Linux Ubuntu
# mkdir flask_example
# cd flask_example
# python -m venv venv_name
# source venv/bin/activate
# pip install flask
# import flask

# from flask import Flask
#
# app = Flask(__name__)


#  So we say, app equals flask, and we pass in dunder name. Let's create a function print underscore fib, that will
#  print out the string Fibonacci on our web browser, but as an HTML heading. So def print fib. And we want to return
#  the string Fibonacci, but we'll use a HTML heading. Now when you send a request to a web server from your web browser
#  , this request is forwarded to the flask application instance. So the flask instance needs to know what code it needs
#  to run, for each of the URL requested. And so there needs to be a mapping, between the URL and the associated Python
#  function. This is called a root or a route, depending on where you live in the world.

# @app.route('/')     #  this means when you go to the main page on the server, you will see Fibonacci in large letters,
# def print_fib():                # as this is returned by the print fib function.
#     return '<h1>Fibonacci</h1>'
#
