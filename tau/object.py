from .app import objects
from .vector import Vector


class PointMass(object):
    """The most basic object.

    Attributes:
        x: A int of the current x coordinate.
        y: A int of the current y coordinate.
        mass: A float of the mass of the object.
        charge: A float of the charge (in electron voltes) of the object
        velocity: A Vector of the current velocity of the object.
        acceleration: A Vector of the current acceleration of the object.
        color: A tuple of RGB values to color the object.
            Default: (255, 255, 255)
    """

    def __init__(self,
                 x: int,
                 y: int,
                 mass: float = 1,
                 charge: float = 0,
                 velocity: Vector = Vector(),
                 acceleration: Vector = Vector(),
                 color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass

        objects.append(self)

    async def _move(self):
        # Apply physics
        for object in objects:
            if object != self:
                if self._has_collided(object):
                    self._handle_collisions(object)

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

    def __del__(self):
        objects.remove(self)
        del self

    async def update(self):
        """Called every time a second passes in the simulation."""
        await self._move()

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
