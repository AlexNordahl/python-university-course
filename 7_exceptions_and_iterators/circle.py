from points import Point
from math import pi, sqrt

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius ** 2

    def move(self, x, y): 
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        center_dist = sqrt((other.pt.x - self.pt.x) ** 2 + (other.pt.y - self.pt.y) ** 2)

        if self.radius >= center_dist + other.radius:
            return self
        elif other.radius >= center_dist + self.radius:
            return other

        return Circle((self.pt.x + other.pt.x) / 2, (self.pt.y + other.pt.y) / 2, (center_dist + self.radius + other.radius) / 2)

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_print(self):
        self.assertEqual(str(Circle(1, 1, 3)), "Circle(1, 1, 3)")

    def test_eq_ne(self):
        self.assertTrue(Circle(1, 1, 1) == Circle(1, 1, 1))
        self.assertTrue(Circle(1, 1, 1) != Circle(1, 1, 2))

    def test_area(self):
        self.assertEqual(Circle(0, 0, 1).area(), pi * 1 ** 2)
        self.assertEqual(Circle(0, 0, 2).area(), pi * 2 ** 2)

    def test_move(self):
        circle = Circle(1, 1, 1)
        circle.move(1, 1)
        self.assertEqual(circle, Circle(2, 2, 1))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 1).cover(Circle(2, 0, 1.5)), Circle(1, 0, 2.25))
        self.assertEqual(Circle(0, 0, 1).cover(Circle(3, 0, 1)), Circle(1.5, 0, 2.5))
        self.assertEqual(Circle(0, 0, 3).cover(Circle(1, 1, 1)), Circle(0, 0, 3))
        self.assertEqual(Circle(1, 1, 1).cover(Circle(0, 0, 3)), Circle(0, 0, 3))
        self.assertEqual(Circle(0, 0, 1).cover(Circle(0, 0, 3)), Circle(0, 0, 3))
        self.assertEqual(Circle(0, 0, 3).cover(Circle(0, 0, 1)), Circle(0, 0, 3))

if __name__ == "__main__":
    unittest.main()