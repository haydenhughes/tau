import math


class Field(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._app = None

    def radius(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def update(self):
        pass


class MagneticField(Field):
    def __init__(self):
        pass
