from math import gcd, floor

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x; self.y = y

    def __str__(self): 
        return str(self.x) if self.y == 1 else f"{self.x}/{self.y}"

    def __repr__(self): 
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):
        self.normalize(); other.normalize()
        return self.x == other.x and self.y == other.y

    def __ne__(self, other): 
        return not self == other

    def __lt__(self, other): 
        return (self.x / self.y) < (other.x / other.y)

    def __le__(self, other): 
        return (self.x / self.y) <= (other.x / other.y)

    def __add__(self, other):
        return Frac(
            self.x * other.y + other.x * self.y, 
            self.y * other.y
        ).normalize()

    def __sub__(self, other):
            return Frac(
            self.x * other.y - other.x * self.y, 
            self.y * other.y
        ).normalize()

    def __mul__(self, other):
        return Frac(
            self.x * other.x,
            self.y * other.y
        ).normalize()

    def __truediv__(self, other):
        return Frac(
            self.x * other.y,
            self.y * other.x
        ).normalize()

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))

    def normalize(self):
        if self.y < 0:
            self.y = abs(self.y)
            if self.x < 0:
                self.x = abs(self.x)
            else:
                self.x = -self.x

        divisor = gcd(self.x, self.y)
        self.x //= divisor
        self.y //= divisor
        return self

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.zero = Frac(0, 1)
        self.one = Frac(1, 1)
    
    def test_normalize(self):
        self.assertEqual(Frac(2, 4).normalize(), Frac(1, 2))
        self.assertEqual(Frac(-2, 4).normalize(), Frac(-1, 2))
        self.assertEqual(Frac(2, -4).normalize(), Frac(-1, 2))
        self.assertEqual(Frac(-2, -4).normalize(), Frac(1, 2))

    def test_print(self):
        self.assertEqual(str(self.one), "1")
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")

    def test_less_equal(self):
        self.assertNotEqual(Frac(2, 4).normalize(), Frac(4, 2))
        self.assertNotEqual(Frac(-2, 4).normalize(), Frac(-1, -2))

        self.assertLess(Frac(1, 2), Frac(3, 4))
        self.assertLessEqual(Frac(1, 3), Frac(3, 9))
        self.assertGreater(Frac(2, 3), Frac(1, 3))

    def test_add(self):
        self.assertEqual(Frac(1, 4) + Frac(3, 4), self.one)
        self.assertEqual(Frac(2, 5) + Frac(3, 7), Frac(29, 35))

    def test_sub(self):
        self.assertEqual(Frac(1, 4) - Frac(3, 4), Frac(-2, 4))
        self.assertEqual(Frac(2, 5) - Frac(4, 10), self.zero)

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(3, 2) * Frac(1, 2), Frac(3, 4))

    def test_div(self):
        self.assertEqual(Frac(1, 4) / Frac(1, 2), Frac(1, 2))
        self.assertEqual(Frac(5, 10) / Frac(1, 2), Frac(1, 1))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        self.assertEqual(-Frac(1, -2), Frac(1, 2))
        self.assertEqual(-Frac(-1, -2), Frac(-1, 2))

if __name__ == "__main__":
    unittest.main()