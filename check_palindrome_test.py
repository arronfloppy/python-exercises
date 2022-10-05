from check_palindrome import *

def test_check_palindrome():
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    assert check_palindrome("aba") == True
    assert check_palindrome("maram") == True
    assert check_palindrome("tarata") == False
    assert check_palindrome("bb") == True
