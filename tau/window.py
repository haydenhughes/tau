import pyglet
import asyncio
from .app import objects, main


class Window(pyglet.window.Window):
    """Creates a basic representation of the simulation.

    This module requires pyglet to be installed.
    """

    def __init__(self, *args, speed=1/60, **kwargs):
        super().__init__(*args, **kwargs)
        pyglet.clock.schedule_interval(self.update, speed)

    def update(self, dt):
        """Acts as an application loop to all physics updates."""
        asyncio.run(main())

    def on_draw(self):
        """Called every frame flip by Tau"""
        for object in objects:
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                                 ('v2i', (int(object.x), int(object.y))),
                                 ('c3B', object.color))

    def run(self):
        """Proxy pyglet run function."""
        pyglet.app.run()
