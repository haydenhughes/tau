import pyglet


class Camera:
    """Creates a moveable, fixed resolution viewport.

    :Properties:
        `window` : pyglet.Window()
            A pyglet window object.
        `width` : int
            Width of the viewport in pixels.
        `height` : int
            Height of the viewport in pixels.
        `filtered` : boolean
            Toggle bilinear filtering for up scaled images. Useful for pixel
            art.
    """

    def __init__(self, window, width=320, height=200, filtered=False):
        self.window = window
        self.width = width
        self.height = height
        self._x = 0
        self._y = 0
        self.texture = pyglet.image.Texture.create(width, height,
                                                   rectangle=True)

        if not filtered:
            pyglet.gl.glTexParameteri(self.texture.target,
                                      pyglet.gl.GL_TEXTURE_MAG_FILTER,
                                      pyglet.gl.GL_NEAREST)
            pyglet.gl.glTexParameteri(self.texture.target,
                                      pyglet.gl.GL_TEXTURE_MIN_FILTER,
                                      pyglet.gl.GL_NEAREST)

    def __enter__(self):
        pyglet.gl.glViewport(0, 0, self.width, self.height)
        self.set_fixed_projection()
        return self

    def __exit__(self, *args):
        buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        self.texture.blit_into(buffer, 0, 0, 0)

        pyglet.gl.glViewport(0, 0, self.window.width, self.window.height)
        self.set_window_projection()

        aspect_width = self.window.width / float(self.width)
        aspect_height = self.window.height / float(self.height)
        if aspect_width > aspect_height:
            scale_width = aspect_height * self.width
            scale_height = aspect_height * self.height
        else:
            scale_width = aspect_width * self.width
            scale_height = aspect_width * self.height
        x = (self.window.width - scale_width) / 2
        y = (self.window.height - scale_height) / 2

        pyglet.gl.glClearColor(0, 0, 0, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glColor3f(1, 1, 1)
        self.texture.blit(x, y, width=scale_width, height=scale_height)

    def set_fixed_projection(self):
        # Override this method if you need to change the projection of the
        # fixed resolution viewport.
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, self.width, 0, self.height, -1, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def set_window_projection(self):
        # This is the same as the default window projection, reprinted here
        # for clarity.
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, self.window.width, 0, self.window.height, -1, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    @property
    def x(self):
        """x postition of the Camera.

        :type: int
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        """y postition of the Camera.

        :type: int
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def update(self):
        """Updates the camera position."""
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTranslatef(int(-self._x), int(-self._y), int(-0))
