import math


class Point:
    """References a point on a plane.

    Attributes:
        x: An integer for the x coordinate.
        y: An integer for the y coordinate.
        z: An integer for the z coordinate, used for referencing a layer.
    """

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        """Calculate distance between self and another object.

        Args:
            other: Another sprite.

        Returns:
            A float of the calculated distance in pixels.
        """
        return math.hypot(other.x - self.x, other.y - self.y)
