""" This is an example of D & C 5 (Divide & COnquer) algorithm.
    Euclidean algorithmEuclidean's algorithm, is an efficient method 
    for computing the greatest common divisor (GCD) of two integers """



def gcd_euclidean(a, b):

    if a == 0:
       return b
    elif b == 0:
        return a
    elif a == b:
        return a
        
    divident = a if a >= b else b
    divisor = a if a < b else b
    quotient = divident // divisor
    remainder =divident % divisor

    return gcd_euclidean(divisor, remainder) 
