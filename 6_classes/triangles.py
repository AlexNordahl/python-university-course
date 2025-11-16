from points import Point
import copy

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):              # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):             # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    
    def __eq__(self, other):        # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        return self.get_points() == other.get_points()

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):               # zwraca środek (masy) trójkąta
        x_s = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y_s = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x_s, y_s)

    def area(self):
        heron = 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) + 
            self.pt2.x * (self.pt3.y - self.pt1.y) +
            self.pt3.x * (self.pt1.y - self.pt2.y)
        )
        return heron

    def move(self, x, y):
        self.pt1.x += x; self.pt1.y += y
        self.pt2.x += x; self.pt2.y += y
        self.pt3.x += x; self.pt3.y += y
        return self

    def get_points(self):
        return set([self.pt1, self.pt2, self.pt3])

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.center = Point(0, 0)
        self.basic_trg = Triangle(0, 0, 3, 0, 0, 3)

    def test_print(self):
        self.assertEqual(str(self.basic_trg), "[(0, 0), (3, 0), (0, 3)]")
        self.assertEqual(repr(self.basic_trg), "Triangle(0, 0, 3, 0, 0, 3)")

    def test_equal(self):
        self.assertTrue(self.basic_trg == Triangle(3, 0, 0, 0, 0, 3))
        self.assertTrue(self.basic_trg != Triangle(3, 0, 0, 4, 0, 3))

    def test_center(self):
        self.assertEqual(self.basic_trg.center(), Point(1, 1))
        self.assertEqual(Triangle(3, 5, -1, 3, 4, -2).center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(self.basic_trg.area(), 4.5)
        self.assertEqual(Triangle(3, 5, -1, 3, 4, -2).area(), 15)

    def test_move(self):
        test_trg1 = copy.deepcopy(self.basic_trg)
        test_trg2 = copy.deepcopy(self.basic_trg)
        self.assertEqual(test_trg1.move(3, 3), Triangle(3, 3, 6, 3, 3, 6))
        self.assertEqual(test_trg2.move(-3, -3), Triangle(-3, -3, 0, -3, -3, 0))

if __name__ == "__main__":
    unittest.main()