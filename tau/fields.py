import math
from .vector import Vector


class Field(object):
    """The basic field class.

    This class serves as no more then a template for building fields.

    Fields attatch to any object where the origin of the field is the position
    of the object.
    """

    def __init__(self, object):
        self._object = object
        self._x = object.x
        self._y = object.y
        self._app = None

    def radius(self, other):
        """Calculate the radius of the field.

        Calculates the distance between the center of self (the field)
        origin and another object.

        Args:
            other: A object (PointMass or other) to cacluate the distance
                between.

        """
        return math.sqrt((other.x - self._x) ** 2 + (other.y - self._y) ** 2)

    def update(self, dt):
        """Called every time a second passes in the simulation.

        This should be overridden by child classes to apply forces to objects.

        Args:
            dt: The floored (rounded down) amount of whole seconds that has
                elasped between frame refreshes. This value is generally 0.
        """
        pass

    def angle_between(self, other):
        """Calcualate the angle between objects.

        Args:
            other: Another object.

        Returns:
            A float of the angle in radians from the normal (positive y axis)
            to other from self.
        """
        return math.atan2(self._x - other.x, self._y - other.y)


class MagneticField(Field):
    def __init__(self):
        pass


class GravitationalField(Field):
    GRAVITATIONAL_CONSTANT = 6.673e-11

    def __init__(self, object):
        super().__init__(object)
        self._mass = object.mass

    def update(self, dt):
        for object in self._app.objects:
            if object != self._object:
                gf = (self.GRAVITATIONAL_CONSTANT * self._mass
                      * object.mass) / (self.radius(object) ** 2)
                print(self.angle_between(object))
                force = Vector(gf * math.sin(self.angle_between(object)),
                               gf * math.cos(self.angle_between(object)))
                object.apply_force(force)
