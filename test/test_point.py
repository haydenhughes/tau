import unittest
from engine.point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(-2, 5)
        self.point2 = Point(4, -3)

    def test_distance(self):
        self.assertEqual(self.point1.distance(self.point2), 10)
