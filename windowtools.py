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
