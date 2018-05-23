import pyglet


class Camera:
    """Moves viewport.

    :Properties:
        `renderer` : tuple
            A tuple of renderer objects to attach to the camera.
    """

    def __init__(self, renderer):
        self.renderer = renderer
        self.x = 0
        self.y = 0
        self._zoom = 1

    def update(self):
        """Updates the camera position."""
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTranslatef(int(-self.x), int(-self.y), int(-0))
