# Tau τ

The very hacked together physics engine.

Made for me to better learn kinematics.

## Basic Usage
```python
from Tau import Tau, PointMass, Vector

app = Tau()

v = Vector(1, 1)
g = Vector(0, -9.8)

mass = PointMass(400, 300, mass=1, velocity=v, acceleration=g)

app.add_objects(mass)
app.run()
```

## Licence
Tau is distributed under the MIT Licence.
