import abc
import numpy 

### Abstract classes
class Object(metaclass=abc.ABCMeta):
    def __init__(self, mass: float, position: numpy.array, velocity: numpy.array):
        self._mass = mass
        self._position = position
        self._velocity = velocity
        self._last_position = position

    @property 
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, value):
        self._mass = value

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def last_position(self):
        return self._last_position

    @last_position.setter
    def last_position(self, value):
        self._last_position = value

    @property
    def velocity(self):
        return self._velocity
        
    @velocity.setter
    def velocity(self, value):
        self._velocity = value


class VerletObject(Object):
    @property
    def last_position(self):
        return self._last_position


class Method(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update_velocity(self, object: Object, acceleration: numpy.array, differenceTime: float):
        return

    @abc.abstractmethod
    def update_position(self, object: Object, differenceTime: float):
        return

class Simulation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, input):
        return
    
class Conditions(metaclass=abc.ABCMeta):
    def __init__(self, differenceTime: float, acceleration: numpy.array):
        self._differenceTime = differenceTime
        self._acceleration = acceleration

    @property
    def differenceTime(self):
        return self._differenceTime
    
    @differenceTime.setter
    def differenceTime(self, value):
        self._differenceTime = value

    @property
    def acceleration(self):
        return self._acceleration
    
    @acceleration.setter
    def acceleration(self, value):
        self._acceleration = value