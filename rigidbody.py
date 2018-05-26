import pyglet
import math


class Vector:
    """A class for handling vectors.

    The x and y attributes are not position and are only there to assist
    with vector math.
    Supports vector math standard operators.
    Example: `vec3 = vec1 + vec2`

    A vector's attibutes should not be editied directly but instead updated
    using the polar() and cartesian() functions.
    Vectors are created with its values as 0 so after creation the vector must
    be given values using the polar() and cartesian() methods.


    Attributes:
        direction: A float of the direction in degrees of the vector.
        magnitude: A float of the magnitude of the vector.
        x: A float of the vector's cartesian x coordinate.
        y: A float of the vector's cartesian y coordinate.
    """

    def __init__(self):
        self.magnitude = 0
        self.direction = 0
        self.x = 0
        self.y = 0

    def polar(self, magnitude=0, direction=0):
        """Update the values of a vector using the polar coordinate system.

        Args:
            magnitude: A float for magnitude of the vector.
            direction: A float for direction of the vector in degrees.
        """
        self.magnitude = magnitude
        self.direction = direction
        self.x = magnitude * math.degrees(math.cos(math.radians(direction)))
        self.y = magnitude * math.degrees(math.sin(math.radians(direction)))

    def cartesian(self, x=0, y=0):
        """Update the values of a vector using the cartesian coordinate system.

        Args:
            x: A float for the x coordinate of the vector.
            y: A float for the y coordinate of the vector.
        """
        self.x = x
        self.y = y
        self.magnitude = math.hypot(x, y)
        self.direction = math.degrees(math.atan2(y, x))

    def __add__(self, other):
        final_vector = Vector()
        x = self.x + other.x
        y = self.y + other.y
        final_vector.cartesian(x=x, y=y)
        return final_vector

    def __sub__(self, other):
        final_vector = Vector()
        x = self.x - other.x
        y = self.x - other.x
        final_vector.cartesian(x=x, y=y)
        return final_vector

    def __rsub__(self, other):
        final_vector = Vector()
        x = other.x - self.x
        y = other.x - self.x
        final_vector.cartesian(x=x, y=y)
        return final_vector

    def __mul__(self, scaler):
        final_vector = Vector()
        x = self.x * scaler
        y = self.y * scaler
        final_vector.cartesian(x=x, y=y)
        return final_vector

    def angle(self, other):
        """Get the angle between two vectors.

        Args:
            other: Another vector.

        Returns:
            A float in degrees of the angle between self and other vectors.
        """
        return math.degrees(math.atan2(other.y, other.x)
                            - math.atan2(self.y, self.x))

    def dot_product(self, other):
        """Get the dot product of two vectors.

        Args:
            other: Another vector.

        Returns:
            A float of the resulting scaler.
        """
        return self.magnitude \
            * other.magnitude \
            * math.degrees(math.cos(math.radians(self.angle(other))))


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
                if 0 < self.distance(other) <= self.width:
                    if self.elastic:
                        self.velocity = self.elastic_collision(other)
                    else:
                        self.velocity = self.inelastic_collision(other)
                        self.no_collide.append(other)

    def distance(self, other):
        """Calculate distance between self and another object.

        Args:
            other: Another sprite.

        Returns:
            A float of the calculated distance in pixels.
        """
        return math.hypot(other.x - self.x, other.y - self.y)

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
        normal_vector.cartesian(x=other.x - self.x, y=other.y - self.y)
        unit_vector.cartesian(x=normal_vector.x / normal_vector.magnitude,
                              y=normal_vector.y / normal_vector.magnitude)
        unit_tangent_vector.cartesian(-unit_vector.y, unit_vector.x)

        scaler = unit_vector.dot_product(self._current_velocity)
        v2_scaler = unit_vector.dot_product(other._current_velocity)

        tangential = unit_tangent_vector.dot_product(self._current_velocity)
        normal = (scaler * (self.mass - other.mass) + 2
                  * other.mass * v2_scaler) / self.mass + other.mass
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
             * other._current_velocity.x) / self.mass + other.mass
        y = (self.mass * self._current_velocity.y + other.mass
             * other._current_velocity.y) / self.mass + other.mass

        final_vector = Vector()
        final_vector.cartesian(x=x, y=y)
        return final_vector
