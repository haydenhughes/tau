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
        self.objects = []
        self.fields = []

    def add_objects(self, *object):
        """Add objects to the simulation.

        This is required to be able to properly track objects.

        Args:
            object: One or more objects.
        """
        self.objects.extend(object)

    def add_fields(self, *field):
        """Add fields to the simulation.

        This is required to be able to properly track objects/field
        interactions.

        Args:
            field: One or more fields.
        """
        self.fields.extend(field)

    def run(self):
        """Start simulation"""
        for object in self.objects + self.fields:
            self.push_handlers(object)
            object._app = self
            pyglet.clock.schedule_interval(object.update, self.speed)

        pyglet.app.run()
