
from operator import truediv


def check_palindrome(value):
    """ check if value is a palindrome """
    if len(value) == 0 or len(value) == 1:
        return True
    elif value[0] != value[len(value)-1]:
        return False
    
    return check_palindrome(value[1:len(value)-1])

