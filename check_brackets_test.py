import pytest
import check_brackets


def test_check_brackets():
	assert check_brackets.check_brackets("Hello") == True
	assert check_brackets.check_brackets("He{l}lo") == True
	assert check_brackets.check_brackets("H{e{l}l]o") == False
	assert check_brackets.check_brackets("He[)(]llo") == False
	assert check_brackets.check_brackets("He[)(]llo") == False
	assert check_brackets.check_brackets("{ [ ] ( ) }") == True
	assert check_brackets.check_brackets("{ [ ( ] ) }") == False
	assert check_brackets.check_brackets("{ [ }") == False
