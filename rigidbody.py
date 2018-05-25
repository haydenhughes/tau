import pyglet
import math


class Vector:
    """A class for handling polar coordinate vectors.

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

    def __init__(self, direction, magnitude):
        self.direction = direction
        self.magnitude = magnitude
        self.x = self.magnitude * math.cos(math.radians(self.direction))
        self.y = self.magnitude * math.sin(math.radians(self.direction))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.x
        direction = math.degrees(math.atan(x / y))
        magnitude = math.sqrt(x ** 2 + y ** 2)
        return Vector(direction, magnitude)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.x - other.x
        direction = math.degrees(math.atan(x / y))
        magnitude = math.sqrt(x ** 2 + y ** 2)
        return Vector(direction, magnitude)

    def angle(self, other):
        """Get the angle between two vectors.

        Args:
            other: Another vector.

        Returns:
            A float in degrees of the angle between self and other vectors.
        """
        return math.degrees(math.atan2(other.y, other.x) - math.atan2(self.y, self.x))


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
        self.velocity = Vector(0, 0)

    def update(self):
        """Checks collisions and applies velocity."""

        self.x += self.velocity.x
        self.y += self.velocity.y

        for object in self.renderer.game_objects:
            if isinstance(object, RigidBody) and not object.visible:
                if self.distance(object) < (self.width/2 + object.width/2):
                    self.velocity = self.calculate_collision(object)

    def distance(self, other):
        """Calculate distance between self and another object.

        Args:
            other: Another sprite.

        Returns:
            A float of the calculated distance in pixels.
        """
        return math.sqrt((other.y - self.y) ** 2 + (other.x - self.x) ** 2)

    def calculate_collision(self, other):
        """Calculate the resault vectors of a collision.

        Args:
            other: Another RidgidBody.

        Returns:
            A Vector of how self should react to the collision.
        """
        angle = self.velocity.angle(other)
        f = (self.velocity.magnitude
             * math.degrees(math.cos(self.velocity.direction - angle))
             * (self.mass - other.mass) + 2
             * other.mass
             * other.velocity.magnitude
             * math.degrees(math.cos(other.velocity.angle - angle))) \
            / (self.mass + other.mass)

        x = f * math.degrees(math.cos(angle)) \
            - self.velocity.magnitude \
            * math.degrees(math.sin(self.velocity.angle - angle)) \
            * math.degrees(math.sin(angle))

        y = f * math.degrees(math.sin(angle))  \
            + self.velocity.magnitude  \
            * math.degrees(math.sin(self.velocity.angle - angle)) \
            * math.degrees(math.cos(angle))

        return Vector(math.degrees(math.atan(y/x)), math.sqrt(x ** 2 + y ** 2))
