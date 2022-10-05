

def gcd_euclidean(a, b):

    """ This is an example of D & C (Divide & COnquer) algorithm.
        Euclidean's algorithm, is an efficient method 
        for computing the greatest common divisor (GCD) of two integers """

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
