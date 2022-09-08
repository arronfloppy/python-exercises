from euclidean_algo import *

def test_gcd_euclidean():
    assert gcd_euclidean(9,0) == 9
    assert gcd_euclidean(0,3) == 3
    assert gcd_euclidean(9,3) == 3
    assert gcd_euclidean(10,25) == 5
    assert gcd_euclidean(6,12) == 6
    assert gcd_euclidean(282,105) == 3