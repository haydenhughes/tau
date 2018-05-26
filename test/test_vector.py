import unittest
from engine import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vec1 = Vector()
        self.vec2 = Vector()
        self.vec3 = Vector()

    def test_polar(self):
        self.vec1.cartesian(x=5, y=-12)
        self.assertEqual(self.vec1.magnitude, 13)
        self.assertEqual(round(self.vec1.direction, 1), -67.4)

    def test_cartesian(self):
        self.vec1.polar(magnitude=8, direction=125)
        self.assertEqual(round(self.vec1.x, 2), -4.59)
        self.assertEqual(round(self.vec1.y, 2), 6.55)

    def test_multiplication(self):
        self.vec1.cartesian(x=7, y=3)
        result = self.vec1 * 3
        self.assertEqual(result.x, 21)
        self.assertEqual(result.y, 9)

    def test_addition(self):
        self.vec1.cartesian(x=1, y=-3)
        self.vec2.cartesian(x=2, y=4)
        result = self.vec1 + self.vec2
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 1)

    def test_dotproduct(self):
        self.vec1.cartesian(x=-6, y=8)
        self.vec2.cartesian(x=5, y=12)
        self.assertEqual(round(self.vec1.dot_product(self.vec2)), 66)
