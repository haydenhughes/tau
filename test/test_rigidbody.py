import unittest
import pyglet
from engine.rigidbody import RigidBody
from engine.renderer import Renderer
from engine.point import Point


class TestRigidBody(unittest.TestCase):
    def setUp(self):
        image = pyglet.image.create(64, 64)
        self.renderer = Renderer()
        self.rb = RigidBody(image, renderer=self.renderer)
        self.rb2 = RigidBody(image, renderer=self.renderer)
        self.renderer[Point(0, 0, 0)] = self.rb
        self.renderer[Point(200, 0, 0)] = self.rb2

    def test_distance(self):
        self.assertEqual(self.rb.distance(self.rb2), 200)
