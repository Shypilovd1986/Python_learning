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
    for i in range(1, a + 1):
        f *= i
    return f


def check_list():
    a = input('type in numbers').split()
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


# build matrix with main diagonal (nested lists)
def build_matrix():
    a = int(input('Input quantity of rows '))
    b = int(input('Input quantity of columns '))
    list = []
    for i in range(a):
        list.append([])
        for j in range(b):
            if i < j:
                list[i].append(3)
            elif i == j:
                list[i].append(0)
            else:
                list[i].append(7)
    return list
