from definitions import Method, Object, Conditions
import numpy

class Initial(Method):
    def update_position(self, object: Object, conditions: Conditions):
        object.position = object.position + object.velocity * conditions.differenceTime

    def update_velocity(self, object: Object, conditions: Conditions):
        object.velocity = object.velocity + conditions.acceleration * conditions.differenceTime