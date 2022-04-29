# data types in Python
list_of_immutable_types = ['int', 'float', 'str', 'tuple', 'frozen set', 'bool']
list_of_mutable_types = ['list', 'dict', 'set']

# math operations
math_op_list = ['*', '/', '//', '%', '+', '-']

# built-in math function
list_of_builtin_functions = ['min', 'max', 'abs', 'pow', 'round', 'sum']

# print('1', '2', sep = 'separator', end = '\n')

# import math, trunc(), floor(), ceil()

comparison_operators = ['>', '<', '==', '!=', '<=', '>=']
# not True - False, a and b - True, a or b

str_operations = ['concatinations', 'Multiplication', 'len()', 'in', '> or <', '[index]', '[::0]']
# ord('b') - 98 ,

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

list_operations = ['add list + list', 'Multiplication list * number', 'len()', 'in', '> or < for the same type',
                   '[index]', '[::0]', 'sorted(list,key, reverse =True or False)', 'a.append(object)', 'a.clear()',
                   'a.copy()', 'a.count(object)', 'a.extend(sequence)', 'a.index(value, start, stop)',
                   'a.insert(index, object)', 'a.pop(index)', 'a.remove(value)', 'a.reverse()',
                   'a.sort(key=None, reverse=True)', ]
# conditionals
if 5 > 10:
    print('True')
elif 7 < 3:
    print('True')
else:
    pass

# loops

# while True:    (a !=0, 3 in list , len(a)> 0)
#   print(1)
# else:
#   print(2)
#  operator break, instructions continue, if elif else statement

# function range, create object of class range, can be use with build-in function iter which returns an iterator
# also can use with list(), tuple(), set()
v1 = range(1, 10, 2)
v1 = list(range(1, 10, 2))
# !!!!!  list, tuple, set are not iterator, can't use functions next(), and __next__

# set - unoder collections of unique elements
s1 = {}
s2 = set(range(5))
s3 = list(set([2, 3, 55, 3, 1, 2, 3, 1]))
s4 = set((3, 2, 4, 1, 2, 3))

methods_of_set = ['a.add(value)', 'a.update(iterable sequence)',  # add elements
                  'a.discard(value)', 'a.remove(value)', 'a.pop()', 'a.clear()',
                  # remove raise error if there is not value in set
                  'len(our set)', 'in or not in', 'a.intersection(b) or a&b, a.intersection_update(b)',
                  # operattions of set
                  'a.union(b) or a|b ', 'a - b', 'a ^ b', 'a==b', 'a > b or a < b']

# dict - collections of key : value
d1 = {'Misha': 34, 'Dmitriy': 35}
d2 = dict((['Misha', 34], ['Sasha', 63]))
d3 = dict.fromkeys((1, 2, 3), 100)  # takes iterable sequence and value
# empty dictionary creates d = {} or d = dict()

methods_of_dict = ['check in or not in', 'for adding key d[new key]=value', 'for key in d: print(d[key])', 'd.clear()',
                   'd.get(key, value that returns if such key is not in dict, for example \'there is no such key\'',
                   'd.setdefault(key,default)  creates key with default value if there is no such key in dict',
                   'd.pop(key) returns and remove key:value', 'd.popitem() returns and removes random key:value',
                   'd.keys() returns object dict_keys with all keys', 'd.values() returns object dict_values with all values',
                   'd.items() returns object dict_items with all pairs of key:value',
                   'for key,value in d.items(): print(key , value)']

