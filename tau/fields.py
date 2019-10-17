class Field(object):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self._app = None

    def is_object_in_field(self, other):
        return (self.x < object.x < self.x + self.length) \
            and (self.y < object.y < self.y + self.width)

    def update(self):
        for object in self._app.objects:
            if self.is_object_in_field(object):
                self.apply_field()

    def apply_field(self):
        pass


class MagneticField(Field):
    def __init__(self):
        pass
