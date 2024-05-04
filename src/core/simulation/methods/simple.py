import numpy
from core.physics.interfaces import Object
from core.simulation.interfaces import Method, Conditions

class Simple(Method):
    object = Object

    def update_position(object: Object, _, conditions: Conditions):
        object.position = object.position + object.velocity * conditions.differenceTime

    def update_velocity(object: Object, acceleration: numpy.array, conditions: Conditions):
        object.velocity = object.velocity + (acceleration * conditions.differenceTime)