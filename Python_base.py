# *******************      data types in Python      *******************
list_of_immutable_types = ['int', 'float', 'str', 'tuple', 'frozen set', 'bool']
list_of_mutable_types = ['list', 'dict', 'set']

# ****************     math operators      ********************
math_op_list = ['*', '/', '//', '%', '+', '-']

# *************      built-in math functions      ***********************
list_of_builtin_math_functions = ['min', 'max', 'abs', 'pow', 'round', 'sum']

# *************      built-in functions    ******************
# print('1', '2', sep = 'separator', end = '\n')
# ord('a') -> 97  takes one argument type string , returns code of symbol
# type(obj) returns type of argument
# len(x) returns amount elements of collections
# dir(x) returns variables of modules, function, program, folder
# id(x) returns id of variable
# class.__doc__, function.__doc__, class.method.__doc__  returns doc string
# hex(3) returns in Hexadecimal numeral system
# oct(3) returns in Octal numeral system
# bin(3) returns in Binary numeral system
# eval('0b10111') -> 23
# object.__sizeof__() returns value of memory in bytes

# *********************     del statement    ***********************
# The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used
# to delete variables, lists, or parts of a list etc.
comparison_operators = ['>', '<', '==', '!=', '<=', '>=']
# not True - False, a and b - True, a or b


#  ***************      string methods   **************************
methods_of_strings = ['a.upper()', 'a.lower()', 'a.count(sub,start,end)', 'a.find(sub, start)', 'a.rfind(sub, start)',
                      'a.index(sub, start)', 'a.rindex(sub, start)', 'a.replace(old,new,count)', 'a.isalpha()',
                      'a.isdigit()',
                      'a.rjust(width, fillchar)', 'a.ljust(width, fillchar)', 'a.split(sep,maxsplit)',
                      '\'separator\'.join(our list)',
                      'a.strip()', 'a.lstrip()', 'a.rstrip()', 'a.startswith(prefix)', 'a.swapcase()',
                      'a.partition(sep)',
                      'a.center(width, fillchar)', 'a.capitalize()', 'a.isspace()', 'a.capitalize()', 'a.istitle()',
                      'a.isalnum()', 'a.isidentifier()', 'a.endswith(prefix)', 'a.islower()', 'a.isupper()',
                      'a.zfill(width)',
                      'a.title()', 'a.isnumeric()']
# find return -1, index call exclusion


'''
f string, can use {3*23}, {function}
a = 'some {0} text {1}'.format(1, 3)
b = 'some {b} text {a}'.format(a = 'here', b = 'my')
i= 'apples'
c = f'I like {i}'
d = {'name':'Dmitriy', 'age': 35}
text1 = f'My name is {d["name"]}, age is {d["age"]}'
'''

#  ***************      list methods   **************************
list_operations = ['add list + list', 'Multiplication list * number', 'len()', 'in', '> or < for the same type',
                   '[index]', '[::0]', 'sorted(list,key, reverse =True or False)', 'a.append(object)', 'a.clear()',
                   'a.copy()', 'a.count(object)', 'a.extend(sequence)', 'a.index(value, start, stop)',
                   'a.insert(index, object)', 'a.pop(index)', 'a.remove(value)', 'a.reverse()', 'a.sort(key=None',
                   'reverse=True)', ]

#  ***************      set methods   **************************
# a = {2,3,4} - unique collection, can consists only unhashable type
set_operations = ['a.add(4)', 'a.update("iterable objects")', 'a.discard(x) delete from set x',
                  'a.remove(x) returns error if x not in set ', 'a.pop()', 'a.clear()']
# a={1,2,3,4}, b= {3,4,5,6}, a&b-> {3,4}, the same method a.intersection(b), to rewrite a.intersection_update(b)
# a | b, a.union(b), to rewrite a |=b
# a - b , a-=b
# a^b = {1,2,5,6}
#  a > b , returns True if all elements of set b are in a

# ****************      dict     ********************
# d = dict.fromkeys(['a','b'],100) creates dictionary with keys a, b and values 100
# d = {}, d = dict() creates empty dictionary
# d[key] returns value
# d[key] = value , creates new pair key,value
# 'some key' in d, check is there key in dict, returns True or False
# del d['key'] delete pair with key
# d.clear() clear dict
# for i in d:
#     print(i)  will print only keys
# d.values() returns object of type dict_values like list
# d.keys() returns object of type dict_keys like list
# d.items() returns object of type dict_items, like list that consists of tuples (key, value)
# for key,value in d.items():
#     print('key is ', key, 'value is ', value)  print keys and values of dict
# d.get(key), returns value, if add second parameter returns if no such key, for ex. d.get(key,'no such key')
# d.setdefault(key) check is there key returns value ,if is not there ,create pair with this key and None value, we can
# add second parameter , default value d.setdefault(key,value)
# d.pop(key) returns value and delete pair
# d.popitem() returns random value and delete this pair
# d1 = d.copy() copy dict

# ****************      tuple      ********************
# t = (1,2,3)
# t = tuple(iter sequence), t = tuple(range(1,10))
# t.index('s'), t.count('s')
# t + t1, t * 2, 3 in t

# ***************     conditionals     *****************
# if 5 > 10:
#     print('True')
# elif 7 < 3:
#     print('True')
# else:
#     pass

# ****************      loops     ********************
# while True:    (a !=0, 3 in list , len(a)> 0)
#   print(1)
# else:
#   print(2)
#  operator break, instructions continue, if elif else statement

# ********************     iterable objects    ******************
# string, list, set, tuple,
# function range, create object of class range, can be use with build-in function iter which returns an iterator
# also can use with list(), tuple(), set()
# v1 = range(1,10,2)
# v1 = list(range(1,10,2))
# !!!!!  list, tuple, set are not iterator, can't use functions next(), and __next__

# **********      functions eval and exec      *************
# eval('2*3') takes one argument string, one expression
# exec('print("hello world")') takes one argument string, can take block of code with loops, if  etc

# ************     module math        *********************
# import math
# module of math operations
# math.trunc(32.3) -> 32 truncate fractional portion of value
# math.sqrt(3) takes the square root of value
# math.floor(3.5) -> 3 round number to bottom value
# math.ceil(3.5) -> 4 round number to top value


#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  MODULES XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# ***********      module random     *******************
# import random
# random.randint(1,100) returns random number
# random.random() returns random number between 0 and 1
# random.shuffle(x) shuffle sequence x
# random.choice(x) takes random argument from sequence x

# ***********      module __builtins__     *******************
# automatically loads built-in namespace of interpreter

# ***********      module time     *******************
# import time
# time.strftime('%Y%M%D%H%M')

# ***********      module os     *******************
# import os
# os.mkdir('C:\\m1') create new catalog
# os.path.exists('C:\\m1') check if exists catalog with path, returns true or false

# ***********      module sys     *******************
# import sys
# sys.version returns version of python
# sys.getrefcount(object)  returns count of ref on object

# ***********      module copy     *******************
# import copy
# a = copy.copy(b) copy b in a
# a1 = copy.deepcopy(x) copy x in a1 with all nested parts

# ***********************      системы счисления     ************************
# 16-ричная система счисления начинаеться с 0х, 0Х , потом строка с (0-9), (A-F) нижний и верхний регистр
# 8-ричная 0о, 0О, строка из (0-8)
# 2-чная 0b и 0B потом цифры (0-1)
# для преобразования в 10ричную можно int('запись', система счисления ), например int('0x20',16) -> 32,
# или eval('0x20')
