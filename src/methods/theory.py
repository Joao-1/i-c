from definitions import Method, Object, Conditions
import numpy

class Theory(Method):
    def update_position(self, object: Object, conditions: Conditions):
        object.position = object.position + object.velocity * conditions.differenceTime - (1/2) * conditions.acceleration * conditions.differenceTime ** 2

    def update_velocity(self, object: Object, conditions: Conditions):
        object.velocity = object.velocity + conditions.acceleration * conditions.differenceTime