from math import log
from math import factorial


def logn(n):
    return log(n,2)

def nlogn(n):
    return n*logn(n)

def np2(n):
    return n**2

def nfact(n):
    return factorial(n)