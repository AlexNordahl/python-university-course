from math import gcd

def add_frac(frac1, frac2):
    result = [
        frac1[0] * frac2[1] + frac2[0] * frac1[1],
        frac1[1] * frac2[1]
    ]
    return normalize(result)

def sub_frac(frac1, frac2):
    result = [
        frac1[0] * frac2[1] - frac2[0] * frac1[1],
        frac1[1] * frac2[1]
    ]
    return normalize(result)

def mul_frac(frac1, frac2):
    result = [
        frac1[0] * frac2[0],
        frac1[1] * frac2[1]
    ]
    return normalize(result)

def div_frac(frac1, frac2):
    result = [
        frac1[0] * frac2[1],
        frac1[1] * frac2[0]
    ]
    return normalize(result)

def is_positive(frac):
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    normalize(frac1)
    normalize(frac2)
    return frac1[0] == frac2[0] and frac1[1] == frac2[1]

def frac2float(frac):
    return frac[0] / frac[1]

def normalize(frac):
    if frac[1] < 0:
        frac[1] = abs(frac[1])
        if frac[0] < 0:
            frac[0] = abs(frac[0])
        else:
            frac[0] = -frac[0]

    divisor = gcd(frac[0], frac[1])
    frac[0] //= divisor
    frac[1] //= divisor
    return frac

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac(self.zero, self.zero), self.zero)
        self.assertEqual(add_frac([7, 1], [8, 1]), [15, 1])
        self.assertEqual(add_frac([7, 7], [8, 8]), [2, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac(self.zero, self.zero), self.zero)
        self.assertEqual(sub_frac([7, 1], [8, 1]), [-1, 1])
        self.assertEqual(sub_frac([7, 7], [8, 8]), self.zero)

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [0, 3]), self.zero)
        self.assertEqual(mul_frac([1, 2], [2, 2]), [1, 2])
        self.assertEqual(mul_frac([2, 1], [3, 1]), [6, 1])
        self.assertEqual(mul_frac([2, 1], [3, 1]), [6, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.zero, [1, 1]), self.zero)
        self.assertEqual(div_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(div_frac([2, 1], [3, 1]), [2, 3])
        self.assertEqual(div_frac([3, 4], [4, 3]), [9, 16])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 1]), True)
        self.assertEqual(is_positive([-1, 1]), False)
        self.assertEqual(is_positive([1, -1]), False)
        self.assertEqual(is_positive([-1, -1]), True)
        self.assertEqual(is_positive(self.zero), False)

    def test_is_zero(self):
        self.assertEqual(is_zero(self.zero), True)
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.zero, [0, 2]), True)
        self.assertEqual(cmp_frac([1, 3], [3, 9]), True)
        self.assertEqual(cmp_frac([27, 9], [9, 3]), True)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), True)
        self.assertEqual(cmp_frac([-1, 2], [-1, -2]), False)

    def test_frac2float(self):
        self.assertEqual(cmp_frac(self.zero, [0, 2]), True)
        self.assertEqual(cmp_frac([1, 3], [3, 9]), True)
        self.assertEqual(cmp_frac([27, 9], [9, 3]), True)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), True)
        self.assertEqual(cmp_frac([-1, 2], [-1, -2]), False)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()