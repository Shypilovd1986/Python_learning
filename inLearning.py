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

# 7%3 and 7//3 returns int   7/3 returns float
# x = .1 + .1 +.1 -.3
# print(x)