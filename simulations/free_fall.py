import pygame as pg
from definitions import Simulation
import matplotlib.pyplot as plt


class FreeFall(Simulation):
    # Free fall variables
    initialVelocity: float
    velocity: float
    acceleration: float
    initialHeight: float
    height: float
    gravity: float
    differenceTime: float
    time = 0

    def __init__(self, initialVelocity: float = 0, initialHeight: float = 2000, gravity: float = 9.8, differenceTime: float = 0.01):
        self.initialVelocity = initialVelocity
        self.velocity = initialVelocity
        self.acceleration = gravity
        self.initialHeight = initialHeight
        self.height = initialHeight
        self.gravity = gravity
        self.differenceTime = differenceTime

    def moveObjects(self) -> str:
        if self.height <= 0:
            self.velocity = 0
            self.height = 0
            return "The object has hit the ground!"
        
        self.velocity += self.gravity*self.differenceTime
        self.height -= self.velocity*self.differenceTime
        self.time += self.differenceTime
        print("velocity: ", self.velocity, "height: ", self.height, "time: ", self.time)


    def drawObjects(self, screen):
        pass     
    
    def handleEvents(self, events: pg.event.Event):
        for event in events:
            pass

    def plotGraph(self, figure: plt.Figure):
        axes = figure.gca()
        axes.set_ylabel('Velocity')
        axes.set_xlabel('Time')
        # set to use lines instead of points
        
        print("time: ", self.time, "velocity: ", self.velocity)
        figure.gca().plot(self.time, self.velocity, 'ro')

