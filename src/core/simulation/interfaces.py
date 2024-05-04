import abc
import numpy 
from core.physics.interfaces import Object
from core.physics.forces import Forces

class Conditions(metaclass=abc.ABCMeta):
    def __init__(self, differenceTime: float, forces: list[tuple[Forces, dict[str, float]]], dragCoefficient: float = 0.1) -> None:
        self._differenceTime = differenceTime
        self._forces = forces
        self._dragCoefficient = dragCoefficient

    @property
    def differenceTime(self):
        return self._differenceTime
    
    @differenceTime.setter
    def differenceTime(self, value):
        self._differenceTime = value

    @property
    def forces(self):
        return self._forces
    
    @forces.setter
    def forces(self, value):
        self._forces = value

    @property
    def dragCoefficient(self):
        return self._dragCoefficient
    
    @dragCoefficient.setter
    def dragCoefficient(self, value):
        self._dragCoefficient = value
    

class Method(metaclass=abc.ABCMeta):
    @property
    def object(self):
        return self._object

    @abc.abstractmethod
    def update_velocity(object: Object, acceleration: numpy.array, conditions: Conditions):
        return

    @abc.abstractmethod
    def update_position(object: Object, acceleration: numpy.array, conditions: Conditions):
        return

class Data(metaclass=abc.ABCMeta):
    def __init__(self):
        self._position = []
        self._velocity = []
        self._acceleration = []
        self._time = [0]

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        self._acceleration = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value    

class Simulation(metaclass=abc.ABCMeta):
    def __init__(self, end: bool = False, objects: list[Object] = []) -> None:
        self._end = end
        self._objects = objects
        self._data = Data()

    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, value):
        self._end = value

    @property
    def objects(self):
        return self._objects
    
    @objects.setter
    def objects(self, value):
        self._objects = value

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    @abc.abstractmethod
    def update(self, input):
        return

