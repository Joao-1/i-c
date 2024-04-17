from definitions import Method, Object, Conditions

class Verlet(Method):
    def update_position(self, object: Object, conditions: Conditions):
        displacement = object.position - object.last_position
        object.last_position = object.position
        object.position = object.position + displacement  + conditions.acceleration * (conditions.differenceTime ** 2)

    def update_velocity(self, object: Object, conditions: Conditions):
        object.velocity = object.velocity + (2*conditions.acceleration * conditions.differenceTime) / 2