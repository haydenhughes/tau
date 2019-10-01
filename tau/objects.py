import pyglet
from tau.vector import Vector


class PointMass(object):
    """The most basic object.
    Attributes:
        x: A int of the x coordinate.
        y: A int of the y coordinate.
        mass: A float of the mass of the point mass
        velocity: A Vector of the current velocity of the point.
        color: A tuple of RGB values to color the point.
            Default: (255, 255, 255)
    """

    def __init__(self,
                 x: int,
                 y: int,
                 mass: float = 0,
                 velocity: Vector = Vector(),
                 color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.mass = mass
        self.app = None

    def update(self, dt):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def on_draw(self):
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (self.x, self.y)),
                             ('c3B', self.color))

