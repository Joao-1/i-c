from definitions import Simulation, Object, Method, Conditions
import numpy

class FreeFall(Simulation):
    end: bool = False

    def update(self, method: Method, objects: list[Object], conditions: Conditions):
        for object in objects:
            # if object.position[1] <= 0:
            #     object.velocity[1] = 0
            #     object.position[1] = 0
            #     self.end = True  
            
            method.update_velocity(object, conditions)
            method.update_position(object, conditions)


                    
