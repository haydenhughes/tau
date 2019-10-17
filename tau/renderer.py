import pyglet


class Renderer(pyglet.window.Window):
    def __init__(self, tau, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tau = tau

    def on_draw(self):
        """Called every frame flip by Tau"""
        for object in self.tau.objects:
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                                 ('v2i', (int(object.x), int(object.y))),
                                 ('c3B', object.color))
