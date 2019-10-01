from tau import Tau, PointMass, Vector
from tau.objects import Planet

app = Tau(resizable=True)

vel = Vector(1, -1)

mass1 = Planet(300, 300, mass=20e10)
mass2 = PointMass(100, 400, velocity=vel, mass=1)

app.add_objects(mass1, mass2)

app.run()
