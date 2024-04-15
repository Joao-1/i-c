### Abstract classes
import abc

class Method(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def position(self, input):
        return

class Simulation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handleEvents(self, input):
        return

    @abc.abstractmethod
    def moveObjects(self, input):
        return
    
    @abc.abstractmethod
    def drawObjects(self, input):
        return
    
    @abc.abstractmethod
    def plotGraph(self, input):
        return