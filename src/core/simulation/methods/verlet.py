import numpy
from core.physics.interfaces import Object
from core.simulation.interfaces import Method, Conditions
from core.physics.forces import applyForces

class VerletObject(Object):
    def __init__(self, mass: float, radius: float, position: numpy.array = numpy.array([0, 0, 0]), velocity: numpy.array = numpy.array([0, 0, 0])) -> None:
        super().__init__(mass, radius, position, velocity)
        self._last_position = position  

    @property
    def last_position(self):
        return self._last_position

    @last_position.setter
    def last_position(self, value):
        self._last_position = value

class Verlet(Method):
    object = VerletObject

    def update_position(object: VerletObject, acceleration: numpy.array, conditions: Conditions):
        # displacement = object.position - object.last_position
        # object.last_position = object.position
        # object.position = object.position + displacement + acceleration * (conditions.differenceTime ** 2)
        return

    def update_velocity(object: Object, acceleration: numpy.array, conditions: Conditions):
        # object.velocity = object.velocity + ((acceleration + [0, (applyForces(object, conditions.forces)[1]/object.mass), 0]) * conditions.differenceTime) / 2
        halfVelocity = object.velocity + (acceleration * conditions.differenceTime)/2
        object.position = object.position + halfVelocity * conditions.differenceTime
        object.velocity = halfVelocity + ((applyForces(object, conditions.forces)/object.mass) * conditions.differenceTime)/2