import pytest
import point


class TestPoint:
    def test_constructor(self):
        p = point.Point(1, 2)
        assert p.x == 1
        assert p.y == 2

    def test_subtraction(self):
        p1 = point.Point(0, 0)
        p2 = point.Point(3, 4)
        assert p1-p2 == 5
        assert p2-p1 == 5

        p1 = point.Point(0, 0)
        p2 = point.Point(0, 0)
        assert p1-p2 == 0

        assert p1-p1 == 0

    def test_equal(self):
        p1 = point.Point(1, 2)
        p2 = point.Point(1, 2)
        assert p1 == p2

        assert p1 == p1

        p2 = point.Point(2, 2)
        assert not p1 == p2

        p2 = point.Point(1, 3)
        assert not p1 == p2

    def test_not_equal(self):
        p1 = point.Point(1, 2)
        p2 = point.Point(2, 1)
        assert p1 != p2

        p2 = point.Point(1, 1)
        assert p1 != p2

        p2 = point.Point(2, 2)
        assert p1 != p2

        p2 = point.Point(1, 2)
        assert not p1 != p2



