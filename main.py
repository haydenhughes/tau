from tau import Tau, PointMass, Vector

app = Tau(resizable=True)

vel = Vector()

mass1 = PointMass(app, 10, 100, velocity=vel)
mass2 = PointMass(app, 10, 200, velocity=vel)

app.run()
