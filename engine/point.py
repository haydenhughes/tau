from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y', 'z'])):
    """A named tuple for referencing a point on a plane.

    Attributes:
        x: An integer for the x coordinate.
        y: An integer for the y coordinate.
        z: An integer for the z coordinate, used for referencing a layer.
    """
    pass
