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
                   'a.insert(index, object)', 'a.pop(index)', 'a.remove(value)', 'a.reverse()', 'a.sort(key=None, reverse=True)', ]
# conditionals
if 5 > 10:
    print('True')
elif 7 < 3:
    print('True')
else:
    pass

#loops

#while True:    (a !=0, 3 in list , len(a)> 0)
#   print(1)
#else:
#   print(2)
#  operator break, instructions continue, if elif else statement

# function range, create object of class range, can be use with build-in function iter which returns an iterator
# also can use with list(), tuple(), set()
v1 = range(1,10,2)
v1 = list(range(1,10,2))
#!!!!!  list, tuple, set are not iterator, can't use functions next(), and __next__

