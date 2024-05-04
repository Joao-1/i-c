import numpy
from core.physics.interfaces import Object
from core.simulation.interfaces import Conditions, Method

class Viscosity(Method):
    object = Object

    def update_position(object: Object, acceleration: numpy.array, conditions: Conditions):
        gama = object.mass/conditions.dragCoefficient
        object.position = object.position + (gama * ((object.velocity + gama * acceleration) * (1 - numpy.exp(-(conditions.dragCoefficient/object.mass) * conditions.differenceTime)) - (acceleration * conditions.differenceTime))) 
    
    def update_velocity(object: Object, acceleration: numpy.array, conditions: Conditions):
        gama = conditions.dragCoefficient/object.mass
        object.velocity = ((-acceleration/gama) + object.velocity) * numpy.exp(-gama * conditions.differenceTime) - (-acceleration/gama)


class Friction:
    viscosity = Viscosity

class Motion:
    withFriction = Friction

