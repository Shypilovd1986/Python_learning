# list_of_immutable_types = ['int', 'float', 'str', 'tuple', 'frozen set', 'bool']
# list_of_mutable_types = ['list', 'dict', 'set']

# math operations
# math_op_list = ['*', '/', '//', '%', '+', '-']

# built-in math function
# list_of_builtin_functions = ['min', 'max', 'abs', 'pow', 'round', 'sum']

# print('1', '2', sep = 'separator', end = '\n')

# import math, trunc(), floor(), ceil(), sqrt()

# comparison_operators = ['>', '<', '==', '!=', '<=', '>=']
# not True - False, a and b - True, a or b

# str_operations = ['concatinations', 'Multiplication', 'len()', 'in', '> or <', '[index]', '[::0]']
# ord('b') - 98 ,

# methods_of_strings = ['a.upper()', 'a.lower()', 'a.count(sub,start,end)', 'a.find(sub, start)', 'a.rfind(sub, start)',
#                       'a.index(sub, start)', 'a.rindex(sub, start)', 'a.replace(old,new,count)', 'a.isalpha()',
#                       'a.isdigit()',
#                       'a.rjust(width, fillchar)', 'a.ljust(width, fillchar)', 'a.split(sep,maxsplit)',
#                       '\'separator\'.join(our list)',
#                       'a.strip()', 'a.lstrip()', 'a.rstrip()', 'a.startswith(prefix)', 'a.swapcase()',
#                       'a.partition(sep)',
#                       'a.center(width, fillchar)', 'a.capitalize()', 'a.isspace()', 'a.capitalize()', 'a.istitle()',
#                       'a.isalnum()', 'a.isidentifier()', 'a.endswith(prefix)', 'a.islower()', 'a.isupper()',
#                       'a.zfill(width)',
#                       'a.title()', 'a.isnumeric()']
# !!!!!    find return -1, index call exclusion
#
# f string, can use {3*23}, {function}
# a = 'some {0} text {1}'.format(1, 3)
# b = 'some {b} text {a}'.format(a = 'here', b = 'my')
# i= 'apples'
# c = f'I like {i}'
# d = {'name':'Dmitriy', 'age': 35}
# text1 = f'My name is {d["name"]}, age is {d["age"]}'

# list_operations = ['add list + list', 'Multiplication list * number', 'len()', 'in', '> or < for the same type',
#                    '[index]', '[::0]', 'sorted(list,key, reverse =True or False)', 'a.append(object)', 'a.clear()',
#                    'a.copy()', 'a.count(object)', 'a.extend(sequence)', 'a.index(value, start, stop)',
#                    'a.insert(index, object)', 'a.pop(index)', 'a.remove(value)', 'a.reverse()',
#                    'a.sort(key=None, reverse=True)', ]
# ******************     conditionals        *********************
# if 5 < 10 :
#     print('good')
# elif 7 > 3 :
#     print('good')
# else:
#     print('nothing')

# ***************        loops          *********************

# while True:    (a !=0, 3 in list , len(a)> 0)
#   print(1)
# else:
#   print(2)
# operator break, instructions continue, if elif else statement

# *******************         set        ************************

# set - collections of unique elements
# s1 = {}
# s2 = set(range(5))
# s3 = list(set([2, 3, 55, 3, 1, 2, 3, 1]))
# s4 = set((3, 2, 4, 1, 2, 3))
# !!!!!!!!!! set can consists only of immutable data types

# methods_of_set = ['a.add(value)', 'a.update(iterable sequence)',  # add elements
#                   'a.discard(value)', 'a.remove(value)', 'a.pop()', 'a.clear()',
#                   # remove raise error if there is not value in set
#                   'len(our set)', 'in or not in', 'a.intersection(b) or a&b, a.intersection_update(b)',
#                   # operattions of set
#                   'a.union(b) or a|b ', 'a - b', 'a ^ b', 'a==b', 'a > b or a < b']

# ****************       dict      **********

# dict - collections of key : value
# d1 = {'Misha': 34, 'Dmitriy': 35}
# d2 = dict((['Misha', 34], ['Sasha', 63]))
# d3 = dict.fromkeys((1, 2, 3), 100)  # takes iterable sequence and value
# empty dictionary creates d = {} or d = dict()

# methods_of_dict = ['check in or not in', 'for adding key d[new key]=value', 'for key in d: print(d[key])','d.clear()',
#                    'd.get(key, value that returns if such key is not in dict, for example \'there is no such key\'',
#                    'd.setdefault(key,default)  creates key with default value if there is no such key in dict',
#                    'd.pop(key) returns and remove key:value', 'd.popitem() returns and removes random key:value',
#                    'd.keys() returns object dict_keys with all keys',
#                    'd.values() returns object dict_values with all values',
#                    'd.items() returns object dict_items with all pairs of key:value',
#                    'for key,value in d.items(): print(key , value)']

# *******************      tuple      *************************
# t1 = (1, 2, 3)
# t2 = tuple([1, 2, 3])
# t3 = ()
# t4 = tuple()

# methods_of_tuple = ['len(t)', 'in or not in', 't * 2', 't1 + t2', 'min(t) or max(t) if consists of numbers',
# 't[index]', 't.index(value)', 't.count(value)']


# *********************   definition function   **************************
# def name(par):
#     pass
# operator 'return' returns some value or returns None
# also its break the function
# scope variables: built in, global, nonlocal, local
# LEGB  - local, enclosing nonlocal , global, built in scope
# *args argument in function, returns tuple
# **kwargs  return dict , n(a=2,b=4)

# ********       lambda functions        *************************

# lambda args1, args2 : expression
# l = lambda x: x**2
# l1 = lambda x: 'true' if x> 0 else 'false'
# l2 = lambda : 'some text'
# def n(x): return lambda x:x**2 can use in return

# ***************       range      ****************

# function range, create object of class range, can be use with build-in function iter which returns an iterator
# also can use with list(), tuple(), set()
# v1 = range(1, 10, 2)
# v1 = list(range(1, 10, 2))
# !!!!!  list, tuple, set are not iterator, can't use functions next(), and __next__

# ************     useful functions        ***********************

# - variable.__sizeof__() show size of memory
# - id(variable)
# - enumerate(sequence, start value if it needs) -- for example,  list(enumerate((20,10)) returns [(0,20),(1,10)]
# - map(func, iterable sequence) return object map , for example a = list(map(abs,(2,-3,2))) ---[2,3,2]
# map can use built in (list, int, abs), lambda, written ( def ) functions
# - filter(func, sequence)    like function map , but func has to return True or False , return iterator, obj of class
# filter, which consists with elements, which value  is True, example , list(filter(bool,(3,4,'',2))) -> [3,4,2]
# can take lambda, def functions, bool, None , if arg is None return sequence
# - zip , takes two iter sequences , returns obj zip , which consists of tuples() , pairs of elements from both
# sequences , list(zip((1,4,5),'today'))  -> [(1,'t'),(2,'o'),(3,'d')].  !!! can takes many arguments, zip(a,b,c,d),
# defines of smallest sequence, can be unpacked  a,b = zip((1,10), 'ad') - > a = (1,'a'), b = (10,'d')

# ***********     list comprehension  and generators     *********************
#
# lc = [(x, j) for x in range(1,20) for j in range (1,x+1) if x==j]
# lc1 = ((x, j) for x in range(1,20) for j in range (1,x+1) if x==j) #returns object of class generator can use with
# next(lc1), and lc1.__next__


# ************************************************************
# *                                                          *
# *                        OOP                               *
# *                                                          *
# ************************************************************

# Объекты состоят из данных(атрибуты) и поведение(метод)
# клас - шаблон для создания класов

# class Car:               #create class
#     name = 'Audi'

#     def move():
#           print('move')

# !!!!!!для класса функция, для обьекта метод
# a100= Car()             #create object of class Car
# Car.__dict__   # show all attribute of class  a100.__dict__ show all attribute of object

# *********      getattr(), setattr(), delattr(), hasattr()      ************

# getattr(a100, 'name', 100)     функция возвращает значение атрибута name, если такого атрибута нет то вернет 100
# Car.age = 100        поменяет атрибут или создаст новый если такого нет, !!!!!!   если поменять в объекте то
# поменяется только в нем, если в класе то поменяеться и в обьектах
# hasattr(a100, 'age')       вернет True если такое атрибут есть или False если нет
# setattr(Car, 'name', 100)     метод создает или меняет значение атрибута в классе
# delattr(Car, 'name')     or    del Car.name     удалит атрибут

# Метод - функция объявлена внутри класса , привязана к конкретному обьекту self
# self  - объект  к которому был вызван метод

# dry - is principe of writing code  - don't repeat your self

# *************       exception    ************

# if not isinstance(a100, Car):
#       raise ValueError('it's not correct class )     возбудит ошибку и выдаст сообщение

# **********         @staticmethod, @classmethod         **********
#
# class Orc:
#     profession = 'warrior'
#
#     @staticmethod         # декоратор который  говорит что функция не принимает аргумент селф, и вызывать можно как
#     def show_prof():      # обычный атрибут , тоесть через точку можно обратиться как и к обычному атрибуту и
#         print(f'my profession is {Orc.profession}')    # с класса и с объекта
#
#     @classmethod          # аргумент как правило cls , как правило делаем обработку над целым классом, делает
#     def move(cls):        № возможность вызвать и через класс и объект
#         print('orc move')
# a1 = Orc()
# a1.show_prof()
# Orc.show_prof()
# Orc.move()

# **************    патерн моносостояние  ****************

# class Elf():
#     __shared_attr = {'colour_skin': 'beige', 'race' : 'exists'}
#
#     def __init__(self):
#         self.__dict__ = Elf.__shared_attr

# !!!   теперь если меняем какойто атрибут или удаляем меняется во всех экземплярах и в самом классе
# !!!   создаст атрибуты в классе только после того как сработает хотябы один конструктор при создание объекта

# **************       Class body scope in Python       ********************
# в методах не работает принцип, что если переменной нет в методе он иет выше, ее нужно указывать явно через self.attr
# or class.attr
#
# class Ex1():
#     age = 33
#
#     def show_age(self):
#         print(f'your age is {Exc1.age}')  явно указали через self.age r class.age если просто age то не найдет
#
# e1 = Exc1()
# e1.show_age()


# *************      уровни доступа к атрибутам и методам , private, protected   ***************
#
# self._name = name       protected attribute, add one underscore before name, allows to use it with object.attribute
# self.__name = name      private attribute, add double underscore before name, cen be used only by methods
# class Bank:             # if we will check in attribute by obj.attribute it will raise error 'object has no attribute'
#
#     def __init__(self, name):
#         self.__name = name
#
#     def show_name(self):
#         print(f'Bank name is {self.__name}')
#
# b1 = Bank('Aval')
# b1.show_name()

# protected attribute says that it shouldn't use out of class   !!!!!!!!!!!!!!!
# private attribute can be used by obj._class__attribute     !!!!!!!!!!!!!!

#               DUNDER METHODS

# ******************      __class__      *****************
# b1.__class__    return __main__.Bank    , where b1 is obj of class Bank

#*******************      __repr__, __str__       ************************
# отвечают за текстовое оформление в системе
# __repr__  отвечает за то, как отображен наш объект в системе, то как его видит разработчик
# __str__   как видят объект пользователи
# class Ex2:
#     def __repr__(self):
#         return f'Object of class {self.__class__}'
# # если переопределен только __repr__ то он будет подхвачен во всех отображениях
#     def __str__(self):
#         return f'this object was created'
# #     если переопределен только __str__ то он будет отображен через принт и стр, а при обраению в консоли будет видно
# #     содержимое непереопределенного репр, тоесть объект какого класса и где находиться
# e2 = Ex2()
# print(e2)
# если переопределены оба метода то при обраению к объекту e2 , будет отображено строка с repr, если через print(e2),
# str(e2), в toolbar справа будет видна строка  str   !!!!!
#
