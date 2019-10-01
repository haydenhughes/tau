import pyglet


class Tau(pyglet.window.Window):
    """ Helper to set up a window and manage objects.
    Attributes:
        framerate: A float of the amount of time in seconds each frame is
            displayed.
    """

    def __init__(self, *args, framerate=1/60, **kwargs):
        super().__init__(*args, **kwargs)
        self.framerate = framerate
        self._objects = []

    def add_objects(self, *object):
        self._objects.extend(object)

    def __len__(self):
        return len(self._objects)

    def __getitems__(self, index):
        if index < len(self):
            return self._objects[index]
        raise IndexError('Object out of range')

    def run(self):
        for object in self._objects:
            self.push_handlers(object)
            pyglet.clock.schedule_interval(object.update, self.framerate)

        pyglet.app.run()
