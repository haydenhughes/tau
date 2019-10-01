import pyglet
from tau.vector import Vector


class Rigidbody(object):
    def __init__(self,
                 x: int,
                 y: int,
                 color=(255, 255, 255),
                 velocity: Vector = Vector(),
                 mass=0):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.mass = mass

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def update(self):
        self.move()

    def gravitational(self):
        pass


class PointMass(Rigidbody):
    def update(self, dt):
        super().update()

    def on_draw(self):
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                             ('v2i', (self.x, self.y)),
                             ('c3B', self.color))
