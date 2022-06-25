# Python Philosophy:
# - beautiful is better than ugly
# - explicit is better than implicit
# - simple is better than complex
# - complex is better than complicated
# - readability counts
#  import this   - to see all statements

# statement is a unit of execution  (line of code, one statement per line , return statement)
# expression is a unit of evaluation  (x, (x,y), True, f(), x*y, x=y)

# comments introduced by pound sign (#)
# x = 43
# print('x is = {}'.format(x))    # format method, or f string f'x is ={x}'

# if and it's block doesn't change the scope, as usual block too
# if True:
#     z = 2
# print(z)

# key word 'if'
# key word 'def'
#
# fibonacci
# a, b = 0, 1
# while b < 1000:
#     print(b, end = ' ', flush = True)
#     a, b = b, a + b

# built in types :
# int, str, bool, None

# example f string
# x = 'some text {:>10}'.format('here')    # {:>10} indents 10 whitespace
# x = 'some text {:>010}'.format('here')    # {:>10} indents 10 whitespace, count symbols in format's argument and add 0
# # till quantity symbols will not be 10
# print((x))
# y = 0x0a
# print(f'{y:05}')    # напечатает ф строку, 05 - означает что если значение у больше меньше чем 5 символов то до  5
# символов будет дополнено нолями

# 7%3 and 7//3 returns int   7/3 returns float
# x = .1 + .1 +.1 -.3
# print(x)

# from decimal import Decimal
# x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# print(x)   # in this case returns 0.0

# x = 7 - 5  -> True
# bool(None)   -> evaluate as False

# < less than , > greater than , <= less than or equal , == double equal, >= greater than or equal
# x is y , x is not y, x in y,  x not in y
# hungry = True
# x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'   !!!!!
# print(x)
# print('Feed the bear now!' if hungry else 'Do not feed the bear.')

# + Addition
# - Subtraction
# * Multiplication
# / Division
# // Integer division
# % Remainder (Modulo)
# ** Exponent
# - Unary negative
# + Unary

# bitwise operators
# & and
# | or
# ^ Xor
# << shift left
# >> shift right

# Boolean operators
# and   ,And
# or    ,Or
# not   ,Not
# in    Value in set
# not in    Value not in set
# is      some object identity
# is not    ,not some object identity

# if __name__ == '__main__': main()
# main means main file

# *args  is a variable argument list, returns tuple
# a = [2,1,4]
# def n(*args):
#     for s in args:
#         print(a)
# n(a) -> [2,1,4]
# n(*a) -> 2 , 1 ,4     !!!!!!! unpack list

# *kwargs  is a keyword arguments
# def main():
#     kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') # we can unpack kitten(**d)  where d is dict
#
# def kitten(**kwargs):
#     if len(kwargs):
#         for k in kwargs:
#             print('Kitten {} says {}'.format(k, kwargs[k]))
#     else: print('Meow.')
# if __name__ == '__main__': main()

# i = start
# while i <= stop:
#     yield i
#     i += step
# yield like return, but will not stop loop

# def generator(start,stop):
#     while (start<=stop):
#         yield start
#         print(f'start={start}')
#         start+=1
# for counter in generator(3,4):
#     print(f'counter={counter}')
#
# result:
# counter=3
# start=3
# counter=4
# start=4

