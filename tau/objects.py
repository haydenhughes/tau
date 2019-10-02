import pyglet
import math
from tau.vector import Vector


class PointMass(object):
    """The most basic object.

    Attributes:
        x: A int of the current x coordinate.
        y: A int of the current y coordinate.
        mass: A float of the mass of the object.
        velocity: A Vector of the current velocity of the object.
        acceleration: A Vector of the current acceleration of the object.
        color: A tuple of RGB values to color the object.
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

    def _apply_acceleration(self, dt):
        # Account for gravity between objects
        for object in self.app:
            if object != self:
                self.acceleration += (self.gravitational_force(object) / self.mass)

        self.velocity += self.acceleration * dt

    def _move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    @property
    def momentum(self):
        """A read only Vector of the current momentum of the object."""
        return self.mass * self.velocity

    @property
    def kinetic_energy(self):
        """A read only float of the kinetic energy of the object in Joules."""
        return 0.5 * self.mass * (self.velocity.magnitude ** 2)

    def update(self, dt):
        """Called every time a second passes in the simulation.

        Args:
            dt: The floored (rounded down) amount of whole seconds that has
                elasped between frame refreshes. This value is generally 0.
        """
        self._apply_acceleration(dt)
        self._move()

    def on_draw(self):
        """Called every frame flip by Tau"""
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (int(self.x), int(self.y))),
                             ('c3B', self.color))

    def distance_to(self, other: 'PointMass'):
        """Calcualate the distance between objects.

        Args:
            other: Another PointMass object.

        Returns:
            A float of the amount of pixels between self and other.
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def angle_between(self, other: 'PointMass'):
        """Calcualate the angle between objects.

        Args:
            other: Another PointMass object.

        Returns:
            A float of the angle in radians from the normal (positive y axis)
            to other from self.
        """
        return math.atan2(other.x - self.x, other.y - self.y)

    def gravitational_force(self, other: 'PointMass'):
        """Calcualate the gravitational force between objects.

        Args:
            other: Another PointMass object.

        Returns:
            A float of the force in Newtons of gravity between self and other.
        """
        gf = (self.GRAVITATIONAL_CONSTANT * self.mass
              * other.mass) / (self.distance_to(other) ** 2)
        return Vector(gf * math.sin(self.angle_between(other)),
                      gf * math.cos(self.angle_between(other)))
