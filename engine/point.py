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

    def angle(self, other):
        """Get the angle between two points in 2D.

        Args:
            other: Another point.

        Returns:
            A float in degrees of the angle between self and other points.
        """
        return math.degrees(math.atan2(other.y, other.x)
                            - math.atan2(self.y, self.x))

    def distance(self, other):
        """Calculate distance between self and another object.

        Args:
            other: Another sprite.

        Returns:
            A float of the calculated distance in pixels.
        """
        return math.hypot(other.x - self.x, other.y - self.y)
