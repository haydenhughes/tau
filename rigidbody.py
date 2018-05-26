import pyglet
import math


class Vector:
    """A class for handling vectors.

    The x and y attributes are not position and are only there to assist
    with vector math.
    Supports vector addition and subtraction using the +  and - operator.
    Example: `vec3 = vec1 + vec2` or `vec3 = vec1 - vec2`

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
        self.magnitude = magnitude
        self.direction = direction
        self.x = magnitude * math.degrees(math.cos(math.radians(direction)))
        self.y = magnitude * math.degrees(math.sin(math.radians(direction)))

    def cartesian(self, x=0, y=0):
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
        return math.degrees(math.atan2(other.y, other.x) - math.atan2(self.y, self.x))

    def dot_product(self, other):
        """Get the dot product of two vectors.

        Args:
            other: Another vector.

        Returns:
            A float of the resulting scaler.
        """
        return self.magnitude * other.magnitude * math.degrees(math.cos(math.radians(self.angle(other))))


class RigidBody(pyglet.sprite.Sprite):
    """A sprite that obeys physics.

    RigidBody is subclass of pyglet.sprite.Sprite().

    image is a pyglet.resources.Load() object which is passed to the
    parent class.

    Attributes:
        mass: A float of the mass of the object in kg. (Default: 1)
        renderer: A renderer object of which is used to check collisions
                  with objects managed by that renderer.
        velocity: A vector of the velocity of the object. (Default: `Vector(0,0)`)
    """

    def __init__(self, image, mass=1, renderer=None):
        super().__init__(image)
        self.mass = mass
        self.renderer = renderer
        self.velocity = Vector()
        self._current_velocity = Vector()
        self._current_velocity.polar(0, 0)
        self.velocity.polar(0, 0)

    def move(self):
        self._current_velocity = self.velocity
        self.x += self.velocity.x
        self.y += self.velocity.y

    def check_collisions(self):
        for other in self.renderer.game_objects:
            if id(self) != id(other):
                if 0 < self.distance(other) <= self.width:
                    self.velocity = self.calculate_collision(other)

    def distance(self, other):
        """Calculate distance between self and another object.

        Args:
            other: Another sprite.

        Returns:
            A float of the calculated distance in pixels.
        """
        return math.hypot(other.x - self.x, other.y - self.y)

    def calculate_collision(self, other):
        """Calculate the resault vectors of a collision.

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

        scaler = unit_vector.dot_product(self.velocity)
        v2_scaler = unit_vector.dot_product(other._current_velocity)

        tangential = unit_tangent_vector.dot_product(self.velocity)
        normal = (scaler * (self.mass - other.mass) + 2 * other.mass * v2_scaler) / self.mass + other.mass
        tangential_vector = unit_tangent_vector * tangential
        normal_vector = unit_vector * normal

        out_vector = tangential_vector + normal_vector

        return out_vector
