from definitions import Method, Object, Conditions

class Simple(Method):
    def update_position(self, object: Object, conditions: Conditions):
        object.position = object.position + object.velocity * conditions.differenceTime

    def update_velocity(self, object: Object, conditions: Conditions):
        object.velocity = object.velocity + conditions.acceleration * conditions.differenceTime