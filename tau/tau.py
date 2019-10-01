import pyglet


class Tau(pyglet.window.Window):
    """ Helper to set up a window and manage object drawing."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        pyglet.app.run()
