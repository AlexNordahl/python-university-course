from rectangles import Rectangle
from points import Point
import pytest

@pytest.fixture
def unit_rect():
    return Rectangle(0, 0, 1, 1)

def test_print(unit_rect):
    assert str(unit_rect) == "[(0, 0), (1, 1)]"
    assert repr(unit_rect) == "Rectangle(0, 0, 1, 1)"

def test_equal(unit_rect):
    assert unit_rect == unit_rect
    assert unit_rect != Rectangle(0, 0, 1, 2)

def test_center(unit_rect):
    assert unit_rect.center() == Point(0.5, 0.5)
    assert Rectangle(-1, -1, 1, 1).center() == Point(0, 0)

def test_area(unit_rect):
    assert unit_rect.area() == 1
    assert Rectangle(-1, -1, 1, 1).area() == 4

def test_move(unit_rect):
    unit_rect.move(-3, -3)
    assert unit_rect ==  Rectangle(-3, -3, -2, -2)

    rect2 = Rectangle(0, 0, 1, 1)
    rect2.move(4, 4)
    assert rect2 == Rectangle(4, 4, 5, 5)

def test_from_points(unit_rect):
    points = (Point(0, 0), Point(1, 1))
    rect1 = Rectangle.from_points(points)

    assert rect1 == unit_rect.copy()

def test_top():
    assert Rectangle(0, 0, 1, 1).top == 1
    assert Rectangle(0, 0, -1, -1).top == 0

def test_left():
    assert Rectangle(0, 0, 1, 1).left == 0
    assert Rectangle(0, 0, -1, -1).left == -1

def test_bottom():
    assert Rectangle(0, 0, 1, 1).bottom == 0
    assert Rectangle(0, 0, -1, -1).bottom == -1

def test_right():
    assert Rectangle(0, 0, 1, 1).right == 1
    assert Rectangle(0, 0, -1, -1).right == 0

def test_width():
    assert Rectangle(0, 0, 1, 1).width == 1
    assert Rectangle(-2, -1, 3, 5).width == 5
    assert Rectangle(5, 0, -5, 0).width == 10

def test_height():
    assert Rectangle(0, 0, 1, 1).height == 1
    assert Rectangle(-2, -1, 3, 5).height == 6
    assert Rectangle(0, 5, 0, -5).height == 10

def test_corners():
    r = Rectangle(0, 0, 1, 1)

    assert r.topleft == Point(0, 1)
    assert r.topright == Point(1, 1)
    assert r.bottomleft == Point(0, 0)
    assert r.bottomright == Point(1, 0)

    r2 = Rectangle(-1, -2, 3, 4)

    assert r2.topleft == Point(-1, 4)
    assert r2.topright == Point(3, 4)
    assert r2.bottomleft == Point(-1, -2)
    assert r2.bottomright == Point(3, -2)
