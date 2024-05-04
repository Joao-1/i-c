import numpy
from core.physics.forces import applyForces
from core.physics.interfaces import Object
from core.simulation.interfaces import Conditions, Data, Method, Simulation

class FreeFall(Simulation):
    method: Method
    conditions: Conditions
    objects: list[Object]
    data: Data
    end: bool

    def __init__(self, method: Method, conditions: Conditions, objects: list[Object] = []) -> None:
        self.method = method
        self.conditions = conditions
        self.objects = objects if len(objects) != 0 else [self.method.object(25.0, 0.5, numpy.array([0.0, 100.0, 0.0]), numpy.array([0.0, 0.0, 0.0]))]
        self.data = Data()
        self.end = False  

    def update(self):
        for object in self.objects:
            if object.position[1] <= 0:
                self.end = True
                return  
            
            resultantForce = applyForces(object, self.conditions.forces)
            self.method.update_velocity(object, numpy.array([0.0, (resultantForce[1]/object.mass), 0.0]), self.conditions)
            self.method.update_position(object, numpy.array([0.0, (resultantForce[1]/object.mass), 0.0]), self.conditions)

            self.data.position.append(object.position[1])
            self.data.velocity.append(object.velocity[1])
            
        self.data.acceleration.append(resultantForce/object.mass)
        self.data.time.append(self.data.time[0 if len(self.data.time) == 0 else -1] + self.conditions.differenceTime)
                    
