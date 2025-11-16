from points import Point
import math

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):         # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2
    
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2
        return Point(center_x, center_y)

    def area(self):                 # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.unit_rect = Rectangle(0, 0, 1, 1)

    def test_print(self):
        self.assertEqual(str(self.unit_rect), "[(0, 0), (1, 1)]")
        self.assertEqual(repr(self.unit_rect), "Rectangle(0, 0, 1, 1)")

    def test_equal(self):
        self.assertTrue(self.unit_rect == self.unit_rect)
        self.assertTrue(self.unit_rect != Rectangle(0, 0, 1, 2))

    def test_center(self):
        self.assertEqual(self.unit_rect.center(), Point(0.5, 0.5))
        self.assertEqual(Rectangle(-1, -1, 1, 1).center(), Point(0, 0))

    def test_area(self):
        self.assertEqual(self.unit_rect.area(), 1)
        self.assertEqual(Rectangle(-1, -1, 1, 1).area(), 4)

    def test_move(self):
        rect1 = self.unit_rect
        rect1.move(-3, -3)
        self.assertEqual(rect1, Rectangle(-3, -3, -2, -2))

        rect2 = Rectangle(0, 0, 1, 1)
        rect2.move(4, 4)
        self.assertEqual(rect2, Rectangle(4, 4, 5, 5))
    
if __name__ == "__main__":
    unittest.main()