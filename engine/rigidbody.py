import pyglet
import math
from engine.vector import Vector
from engine.point import Point


class RigidBody(pyglet.sprite.Sprite):
    """A sprite that obeys physics.

    RigidBody is subclass of pyglet.sprite.Sprite().

    image is a pyglet.resources.Load() object which is passed to the
    parent class.

    Attributes:
        mass: A float of the mass of the object in kg. (Default: 1)
        renderer: A renderer object of which is used to check collisions
                  with objects managed by that renderer.
        velocity: A vector of the velocity of the object.
        elastic: A boolean of wheather or not the
                 object is elastic (like a ball).
        no_collide: A list of object that the RigidBody cannot collide with.
    """

    def __init__(self, image, mass=1, renderer=None, elastic=False):
        super().__init__(image)
        self.mass = mass
        self.renderer = renderer
        self.elastic = elastic
        self.no_collide = []
        self.velocity = Vector()
        self._current_velocity = Vector()
        self._current_velocity.polar(0, 0)
        self.velocity.polar(0, 0)

    def move(self):
        """Apply the velocity transformations."""
        self._current_velocity = self.velocity
        self.x += self.velocity.x
        self.y += self.velocity.y

    def check_collisions(self):
        """Check for collisions with other objects.
        This MUST be ran before running any object.move() functions.
        """
        for other in self.renderer.game_objects:
            if id(self) != id(other) and other not in self.no_collide:
                if self.x < other.x + other.width \
                        and self.x + self.width > other.x \
                        and self.y < other.y + other.height \
                        and self.height + self.y > other.y:

                    if self.elastic:
                        self.velocity = self.elastic_collision(other)
                    else:
                        self.velocity = self.inelastic_collision(other)

    def elastic_collision(self, other):
        """Calculate the result vectors of a elastic collision.

        The mathmatical equation assumes that the object is a circle.

        Args:
            other: Another RidgidBody.

        Returns:
            A Vector of how self should react to the collision.
        """
        normal_vector = Vector()
        unit_vector = Vector()
        unit_tangent_vector = Vector()
        normal_vector.cartesian(x=(other.x + other.width/2) - (self.x + self.width/2),
                                y=(other.y + other.height/2) - (self.y + self.height/2))
        unit_vector.cartesian(x=normal_vector.x / normal_vector.magnitude,
                              y=normal_vector.y / normal_vector.magnitude)
        unit_tangent_vector.cartesian(-unit_vector.y, unit_vector.x)

        scaler = unit_vector.dot_product(self._current_velocity)
        v2_scaler = unit_vector.dot_product(other._current_velocity)

        tangential = unit_tangent_vector.dot_product(self._current_velocity)
        normal = (scaler * (self.mass - other.mass) + 2
                  * other.mass * v2_scaler) / (self.mass + other.mass)
        tangential_vector = unit_tangent_vector * tangential
        normal_vector = unit_vector * normal

        out_vector = tangential_vector + normal_vector

        return out_vector

    def inelastic_collision(self, other):
        """Calculate the result vectors of a inelastic collision.

        Args:
            other: Another RidgidBody.

        Returns:
            A Vector of how self should react to the collision.
        """
        x = (self.mass * self._current_velocity.x + other.mass
             * other._current_velocity.x) / (self.mass + other.mass)
        y = (self.mass * self._current_velocity.y + other.mass
             * other._current_velocity.y) / (self.mass + other.mass)

        final_vector = Vector()
        final_vector.cartesian(x=x, y=y)
        return final_vector


class RigidBodyController:
    """A class for handling the collision checking and moving of rigid bodies.

    Attribues:
        `renderer`: The renderer object that handles the rigid bodies
    """

    def __init__(self, renderer=None):
        self.renderer = renderer

    def rigid_bodies(self):
        """A generator that return all rigid bodies handled by the renderer."""
        for game_object in self.renderer.game_objects:
            if isinstance(game_object, RigidBody):
                yield game_object

    def update(self):
        """Update the rigid bodies. Should be called in and update method."""
        rigid_bodies = list(self.rigid_bodies())
        # check_collisions must be ran for every object before running move.
        for rb in rigid_bodies:
            rb.check_collisions()

        for rb in rigid_bodies:
            rb.move()
