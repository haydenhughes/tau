"""
Setting up a basic pyglet window.

`width` is the width of the window in pixels.
`height` is the height of the window in pixels.
`fullscreen` is a 1 or 0 value that enables or disables fullscreen.
`capture_mouse` is a boolean of wheather or not the window should capture the mouse
"""
import pyglet


class WindowManager:
    def __init__(self, width=800, height=600, fullscreen=0, capture_mouse=False):
        self.platform = pyglet.window.get_platform()
        self.display = self.platform.get_default_display()
        self.screen = self.display.get_default_screen()
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width=self.width,
                                           height=self.height,
                                           fullscreen=fullscreen,
                                           screen=self.screen)
