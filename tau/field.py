import math
from .app import fields, objects
from .vector import Vector


class Field(object):
    """The basic field class.

    This class serves as no more then a template for building fields.

    Fields attach to any object. The origin of the field is the position
    of the object.

    Attributes:
        object: An object to attach the field to
    """

    def __init__(self, object):
        self.object = object
        self._x = object.x
        self._y = object.y

        fields.append(self)

    def __del__(self):
        objects.remove(self)
        del self

    def radius(self, other):
        """Calculate the radius of the field.

        Calculates the distance between the center of self (the field)
        origin and another object.

        Args:
            other: A object (PointMass or other) to cacluate the distance
                between.

        """
        return math.sqrt((other.x - self._x) ** 2 + (other.y - self._y) ** 2)

    async def update(self):
        """Called every time a second passes in the simulation.

        This should be overridden by child classes to apply forces to objects.
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


class GravitationalField(Field):
    GRAVITATIONAL_CONSTANT = 6.673e-11

    def __init__(self, object):
        super().__init__(object)
        self._mass = object.mass

    async def update(self, dt):
        for object in objects:
            if object != self.object:
                gf = (self.GRAVITATIONAL_CONSTANT * self._mass
                      * object.mass) / (self.radius(object) ** 2)
                force = Vector(gf * math.sin(self.angle_between(object)),
                               gf * math.cos(self.angle_between(object)))
                object.apply_force(force)
