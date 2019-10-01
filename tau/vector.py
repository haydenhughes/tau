import math


class Vector(object):
    """A class for handling vectors.

    The x and y attributes are not position and are only there to assist
    with vector math.
    Supports vector math standard operators.
    Example: `vec3 = vec1 + vec2`

    Attributes:
        x: X polar coordinate of vector.
        y: Y polar coordinate of vector.
        direction: A float of the direction in radians of the vector.
        magnitude: A float of the magnitude of the vector.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return math.hypot(self.x, self.y)

    @property
    def direction(self):
        return math.atan2(self.y, self.x)

    def set_cartesian(self, magnitude: float, direction: float):
        self.x = magnitude * math.cos(direction)
        self.y = magnitude * math.sin(direction)

    def __add__(self, other: 'Vector'):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scaler: float):
        return Vector(self.x * scaler, self.y * scaler)

    def angle(self, other: 'Vector'):
        """Get the angle between two vectors.

        Args:
            other: Another vector.

        Returns:
            A float in radians of the angle between self and other vectors.
        """
        return math.atan2(other.y, other.x) - math.atan2(self.y, self.x)

    def dot_product(self, other: 'Vector'):
        """Get the dot product of two vectors.

        Args:
            other: Another vector.

        Returns:
            A float of the resulting scaler.
        """
        return self.magnitude * other.magnitude \
            * math.cos(self.angle(other))
