import unittest
from engine import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(1, 2, 3)

    def test_x(self):
        self.assertEqual(self.point.x, 1)
        self.assertEqual(self.point[0], 1)

    def test_y(self):
        self.assertEqual(self.point.y, 2)
        self.assertEqual(self.point[1], 2)

    def test_z(self):
        self.assertEqual(self.point.z, 3)
        self.assertEqual(self.point[2], 3)
