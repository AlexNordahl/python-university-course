import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other): # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other): # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.center = Point(0, 0)

    def test_print(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_equal(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(2, 3))

    def test_vector_operations(self):
        self.assertEqual(Point(1, 2) + Point(2, 3), Point(3, 5))
        self.assertEqual(Point(1, 2) - Point(1, 2), self.center)
        self.assertEqual(Point(1, 2) * Point(1, 2), 5)
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(3, 4).length(), 5)


if __name__ == "__main__":
    unittest.main()