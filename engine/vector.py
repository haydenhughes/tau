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
        self.x = magnitude * math.cos(math.radians(direction))
        self.y = magnitude * math.sin(math.radians(direction))

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
            * math.cos(math.radians(self.angle(other)))
