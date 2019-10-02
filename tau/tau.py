import pyglet


class Tau(pyglet.window.Window):
    """ Helper to set up a window and manage objects.
    Attributes:
        speed: A float of how long, in seconds, a second is in the simulation.
            Default: 1/60
    """

    def __init__(self, *args, speed=1/60, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed
        self._objects = []

    def add_objects(self, *object):
        """Add objects to the simulation.

        This is required to be able to properly track objects.

        Args:
            object: One or more objects.
        """
        self._objects.extend(object)

    def __len__(self):
        return len(self._objects)

    def __getitem__(self, index):
        if index < len(self):
            return self._objects[index]
        raise IndexError('Object out of range')

    def run(self):
        """Start simulation"""
        for object in self._objects:
            self.push_handlers(object)
            object.app = self
            pyglet.clock.schedule_interval(object.update, self.speed)

        pyglet.app.run()
