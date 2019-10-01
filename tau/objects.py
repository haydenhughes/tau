import pyglet
import math
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
    GRAVITATIONAL_CONSTANT = 6.673e-11

    def __init__(self,
                 x: int,
                 y: int,
                 mass: float = 0,
                 velocity: Vector = Vector(),
                 acceleration: Vector = Vector(),
                 color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.app = None

    def apply_acceleration(self):
        self.velocity += self.acceleration

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def update(self, dt):
        self.apply_acceleration()
        self.move()

    def on_draw(self):
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (int(self.x), int(self.y))),
                             ('c3B', self.color))

    def distance_to(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def angle_between(self, other):
        return math.atan2(self.x - other.x, self.y - other.y)


class Planet(PointMass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def gravitational_force(self, other):
        gf = (self.GRAVITATIONAL_CONSTANT * self.mass
              * other.mass) / (self.distance_to(other) ** 2)
        return Vector(gf * math.cos(self.angle_between(other)),
                      gf * math.sin(self.angle_between(other)))

    def apply_acceleration(self):
        for object in self.app:
            if object != self:
                object.acceleration += self.gravitational_force(object)
        super().apply_acceleration()
