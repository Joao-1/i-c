from definitions import Simulation
from pygame.color import THECOLORS as colors
import matplotlib.pyplot as plt
import pygame as pg
import math

class Pendulum(Simulation):
    # Pendulum variables
    angularVelocity: float
    angularAceleration: float
    initialAngle: float
    angle: int
    stringLength: int
    gravity: int
    friction: float
    time: float = 0

    # Simulation variables 
    fps: int
    screenSize: tuple[int, int]
    mousePos: tuple[int, int]
    pinX: int
    pinY: int
    height: int
    leftDown = False


    def __init__(self, fps: int, screenSize: tuple[int, int] = (600, 600), initialAngle: int = 90, stringLength: int = 240, gravity: int = -1250, friction: float = -0.06, angularVelocity: float = 0, angularAceleration: float = 0):
        self.fps = fps
        self.initialAngle = initialAngle
        self.angle = initialAngle*math.pi/180
        self.stringLength = stringLength
        self.gravity = gravity
        self.friction = friction
        self.angularVelocity = angularVelocity
        self.angularAceleration = angularAceleration
        self.screenSize = screenSize
        self.pinX = self.screenSize[0]/2
        self.pinY = self.screenSize[1]/2
        self.height = self.screenSize[1]


    def handleEvents(self, events: pg.event.Event):
        for event in events:
            # Move the pendulum with the mouse
            if event.type == pg.MOUSEMOTION:
                self.mousePos = event.pos
            
            # Hold the pendulum in place
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.leftDown = True
                    self.mousePos = event.pos
            
            # Release the pendulum
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.leftDown = False

    def moveObjects(self):
        if self.leftDown:
            self.angularAceleration = 0
            self.angularVelocity = 0
            self.angle = math.atan2(self.mousePos[0] - self.pinX, self.mousePos[1] - self.pinY)
            self.stringLength = ((self.pinX - self.mousePos[0])**2 + ((self.height-self.pinY)-(self.height-self.mousePos[1]))**2)**0.5
        else:
            self.angularAceleration = self.gravity/self.stringLength * math.sin(self.angle) + self.friction*self.angularVelocity

        self.angularVelocity += self.angularAceleration/self.fps
        self.angle += self.angularVelocity/self.fps

        self.time += 1/self.fps

    def drawObjects(self, screen: pg.Surface):
        screen.fill((100, 100, 100))
        lineWidth = 4
        radius = 20

        x = self.pinX + self.stringLength*math.sin(self.angle)
        y = self.pinY - self.stringLength*math.cos(self.angle)

        pg.draw.line(screen, (0, 0, 0), (self.pinX - lineWidth/2, self.height-self.pinY), (x - lineWidth/2, self.height-y), lineWidth)
        pg.draw.circle(screen, (0, 0, 0), (self.pinX, self.height-self.pinY), lineWidth*1.5)
        pg.draw.circle(screen, colors['red'], (x, self.height-y), radius)
        pg.draw.circle(screen, (0, 0, 0), (x, self.height-y), radius, width=lineWidth)

        pg.display.flip() 

    def plotGraph(self, figure: plt.Figure):
        axes = figure.gca()
        axes.set_ylabel('Position in degrees')
        axes.set_xlabel('Time')
        # set to use lines instead of points
        
        axes.plot(self.time, self.angle*180/math.pi, 'ro')