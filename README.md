# Tau τ

The very hacked together physics engine.

Made for me to better learn kinematics.

## Basic Usage
```python
from tau.window import Window
from tau import PointMass, Vector

window = Window()

v = Vector(1, 1)
g = Vector(0, -9.8)

mass = PointMass(400, 300, mass=1, velocity=v, acceleration=g)


window.run()
```

**Note:** `tau.window.Window` requires `pyglet` to be installed to draw the window. If being used as a library, exclude `window` and instead call `tau.tick()` in a loop.   

## Licence
Tau is distributed under the MIT Licence.
