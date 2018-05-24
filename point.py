from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y', 'z'])):
    """A named tuple for referencing a point on a plane.

    :Parameters:
        `x` : int
            x coordinate
        `y` : int
            y coordinate
        `z` : int
            z coordinate
    """
    pass
