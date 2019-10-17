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
                 mass: float = 1,
                 velocity: Vector = Vector(),
                 acceleration: Vector = Vector(),
                 color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self._app = None

    def _move(self):
        # Apply physics
        for object in self._app:
            if object != self:
                if self._has_collided(object):
                    self._handle_collisions(object)

                # Apply gravity
                self.apply_force(self.gravitational_force(object))

        self.velocity += self.acceleration

        self.x += self.velocity.x
        self.y += self.velocity.y

    def _handle_collisions(self, other):
        self.velocity = other.velocity = (
            self.momentum + other.momentum) / (self.mass + other.mass)

    def _has_collided(self, other):
        # Need to account for velocity so it can't 'jump' over the the other object.
        return (self.x - self.velocity.x <= other.x <= self.x + self.velocity.x
                and self.y - self.velocity.y <= other.y <= self.y + self.velocity.y)

    def update(self, dt):
        """Called every time a second passes in the simulation.

        Args:
            dt: The floored (rounded down) amount of whole seconds that has
                elasped between frame refreshes. This value is generally 0.
        """
        self._move()

    def on_draw(self):
        """Called every frame flip by Tau"""
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (int(self.x), int(self.y))),
                             ('c3B', self.color))

    @property
    def momentum(self):
        """A read only Vector of the current momentum of the object."""
        return self.velocity * self.mass

    @property
    def kinetic_energy(self):
        """A read only float of the kinetic energy of the object in Joules."""
        return 0.5 * self.mass * (self.velocity.magnitude ** 2)

    def apply_force(self, force: Vector):
        """Apply a force to the object

        Args:
            force: A Vector of the force to apply.
        """
        self.acceleration += force / self.mass

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
