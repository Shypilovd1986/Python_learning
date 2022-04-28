# algorithm of Euklid
def algorithm_of_Euklid():
    a = a1 = int(input('input number 1 '))
    b = b1 = int(input('input number 2 '))

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    else:
        print(f'The lowest common multiple of {a1} and {b1} is {a}')

# find factorial of number
def fact_of_number(a):
    # a = int(input('input number for finding it\'s factorial\n'))
    f = 1
    for i in range(1,a+1):
        f*=i
    return f