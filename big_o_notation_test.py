
from big_o_notation import logn, nfact, nlogn, np2


def test_big_o_notation():
    for n in range(10,100):
        """ print("n " + str(n))
        print(" logn " + str( logn(n) ) ) """
        assert logn(n) <= n <= nlogn(n) <= np2(n) <= nfact(n)