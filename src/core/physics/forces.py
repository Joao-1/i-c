from core.physics.interfaces import Force, Object
from core.physics.planets import Earth
import core.physics.constants as constants
from enum import Enum
import numpy

def applyForces(object: Object, forces: list[tuple[Force, dict[str, float]]]) -> numpy.array:
    resultantForce = numpy.array([0.0, 0.0, 0.0])

    for force in forces:
        match force[0]:
            case Forces.GRAVITY:
                force[1].update({"object1": object})
                resultantForce += Gravity.apply(**force[1])
            case Forces.DRAG:
                resultantForce += Drag.apply(object, force[1].get("dragCoefficient", 0.0))


    return resultantForce  

class Gravity(Force):
    def apply(object1: Object, object2: Object = Earth()) -> numpy.array:  
        distance = (object1.position + object1.radius) - (object2.position + object2.radius)
        return -(constants.GRAVITATIONAL_CONSTANT * object1.mass * object2.mass) / (distance ** 2)

class Drag(Force):
    def apply(object: Object, dragCoefficient: float) -> numpy.array:
        return -dragCoefficient * object.velocity

class Forces(Enum): 
    GRAVITY = Gravity   
    DRAG = Drag


