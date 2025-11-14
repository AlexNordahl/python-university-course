def add_poly(poly1, poly2):
    poly1 = poly1 + [0] * max(len(poly2) - len(poly1), 0)

    for i, num in enumerate(poly2):
        poly1[i] += num

    return trim_trailing_zeros(poly1)

def sub_poly(poly1, poly2):
    poly1 = poly1 + [0] * max(len(poly2) - len(poly1), 0)

    for i, num in enumerate(poly2):
        poly1[i] -= num

    return trim_trailing_zeros(poly1)

def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, num1 in enumerate(poly1):
        if num1 == 0:
            continue
        for j, num2 in enumerate(poly2):
            if num2 == 0:
                continue
            result[i + j] += num1 * num2 

    return trim_trailing_zeros(result)

def is_zero(poly):
    return trim_trailing_zeros(poly) == [0]

def eq_poly(poly1, poly2):
    trim_trailing_zeros(poly1)
    trim_trailing_zeros(poly2)
    if len(poly1) != len(poly2):
        return False
    
    for i in range(len(poly1)):
        if poly1[i] != poly2[i]:
            return False
    return True

def eval_poly(poly, x0): pass           # poly(x0), algorytm Hornera

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n):
    original = poly
    for _ in range(n - 1):
        poly = mul_poly(poly, original)
    return poly

def diff_poly(poly):                    # derivative
    result = []

    for i, num in enumerate(poly):
        if num == 0 or i == 0:
            continue
        result.append(i * num)

    return result

def trim_trailing_zeros(poly):
    for num in reversed(list(poly)):
        if num != 0 or len(poly) == 1:
            return poly
        else:
            poly.remove(num)
    return poly

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]

    def test_trim_trailing_zeros(self):
        self.assertEqual(trim_trailing_zeros([1, 0, 0]), [1])

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly([1, 0], [0, 1]), [1, 1])
        self.assertEqual(add_poly([1, 0], [0, 0, 0, 1]), [1, 0, 0, 1])
        self.assertEqual(add_poly([0, 0, 0, 1], [1, 0]), [1, 0, 0, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly([1, 0], [0, 1]), [1, -1])
        self.assertEqual(sub_poly([1, 0], [0, 0, 0, 1]), [1, 0, 0, -1])
        self.assertEqual(sub_poly([0, 0, 0, 1], [1, 0]), [-1, 0, 0, 1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly([1, 1], [1, 1]), [1, 2, 1])
        self.assertEqual(mul_poly([3, 2, 0], [2, 0, 2]), [6, 4, 6, 4])
        self.assertEqual(mul_poly([0], [1, 2, 3]), [0])
        self.assertEqual(mul_poly([1, 2, 3], [0]), [0])
        self.assertEqual(mul_poly([1], [5, 6, 7]), [5, 6, 7])
        self.assertEqual(mul_poly([2], [5, 6, 7]), [10, 12, 14])
        self.assertEqual(mul_poly([1, 0, 3], [2, 4]), [2, 4, 6, 12])
        self.assertEqual(mul_poly([-1, 2], [3, -4]), [-3, 10, -8])
        self.assertEqual(mul_poly([1, 1, 1], [1, 1, 1]), [1, 2, 3, 2, 1])
        self.assertEqual(mul_poly([10, 20, 30], [1, 2]), [10, 40, 70, 60])
        self.assertEqual(mul_poly([5], [6]), [30])
        self.assertEqual(mul_poly([0, 0, 1], [0, 0, 1]), [0, 0, 0, 0, 1])         

    def test_is_zero(self):
        self.assertEqual(is_zero([0]), True)
        self.assertEqual(is_zero([0, 0, 0]), True)
        self.assertEqual(is_zero([1]), False)
        self.assertEqual(is_zero([1, 0, 0]), False)

    def test_eq_poly(self):
        self.assertEqual(eq_poly([1], [1]), True)
        self.assertEqual(eq_poly([1, 0, 0], [1]), True)
        self.assertEqual(eq_poly([1], [1, 0, 0]), True)

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self):
        self.assertEqual(pow_poly([1, 1, 1], 3), [1, 3, 6, 7, 6, 3, 1])
        self.assertEqual(pow_poly([0, 0, 1], 2), [0, 0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([1, 2, 3, 4]), [2, 6, 12])
        self.assertEqual(diff_poly([0, 0, 0, 4]), [12])
        self.assertEqual(diff_poly([0, 2, 0, 4]), [2, 12])


if __name__ == '__main__':
    unittest.main()