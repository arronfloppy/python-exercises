""" some basic recursion examples """

def fact(x):
    if x == 1 or x == 0:
        return x
    else:
        return x * fact(x-1)

def sum(x):
    if(x == 0):
        return 0
    else:
        return sum(x-1) + x