import abc
import numpy

class Object(metaclass=abc.ABCMeta):
    def __init__(self, mass, radius: float, position: numpy.array = numpy.array([0.0, 0.0, 0.0]), velocity: numpy.array = numpy.array([0.0, 0.0, 0.0])) -> None:
        self._mass = mass
        self._radius = radius
        self._position = position
        self._velocity = velocity

    @property 
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, value):
        self._mass = value

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value

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

class Force(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply(self) -> numpy.array:
        return
    
class Planet(Object):
    def __init__(self, mass: float, radius: float, name: str, position: numpy.array = numpy.array([0.0, 0.0, 0.0]), velocity: numpy.array = numpy.array([0.0, 0.0, 0.0])) -> None:
        super().__init__(mass, radius, position, velocity)
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value	