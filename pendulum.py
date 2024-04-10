import pygame as pg
from pygame.color import THECOLORS as colors
import math


size = width, height = 600, 600

pg.init()
screen = pg.display.set_mode(size = size)
pg.display.set_caption("Pendulum Simulation") 

# Variables
# world variables
running = True
fps = 60
clock = pg.time.Clock()
gravity = -1250
mousePos = (width/2, height/2)
leftDown = False

# Pendulum variables
length = 240
radius = 20
pendColor = colors['blue']
lineWidth = 4
pinX = width/2
pinY = height/2
initialAngle = 90
friction = -0.06 ## default value is -0.06
a = initialAngle * math.pi/180 #  angle in radians
angularVelocity = 0  # angular velocity

# Logic    

def handleEvents():
    global running
    global mousePos
    global leftDown

    for event in pg.event.get():
        ## Move the pendulum with the mouse
        if event.type == pg.MOUSEMOTION:
            mousePos = event.pos
        
        ## Hold the pendulum in place
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftDown = True
                mousePos = event.pos
        
        ## Release the pendulum
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                leftDown = False

prevA = a
prevV = angularVelocity
delta = 1/fps
def moveObjects():
    global angularVelocity, a, length, prevA, prevV
    if leftDown:
        aA = 0
        angularVelocity = 0
        a = math.atan2(mousePos[0] - pinX, mousePos[1] - pinY)
        length = ((pinX - mousePos[0])**2 + ((height-pinY)-(height-mousePos[1]))**2)**0.5
    else:
        aA = gravity/length * math.sin(a) + friction*angularVelocity

    angularVelocity += aA/fps
    a += angularVelocity/fps
    # these are obtained using a taylor expansion of a(t + h) around a(t)... much more accurate
    # a = prevA + delta*prevV + ((delta**2)/2)*(gravity/length)*(math.sin(prevA)) + ((delta**3)/6)*(gravity/length)*prevV*math.cos(prevA)
    # aV = prevV + delta*(gravity/length)*math.sin(prevA) + ((delta**2)/2)*(gravity/length)*prevV*math.cos(prevA) + ((delta**3)/6)*(gravity/length)*(-(prevV**2)*math.sin(prevA) + (gravity/length)*math.sin(prevA)*math.cos(prevA))
    # prevA = a
    # prevV = aV

def drawObjects():
    x = pinX + length*math.sin(a)
    y = pinY - length*math.cos(a)

    pg.draw.line(screen, (0, 0, 0), (pinX - lineWidth/2, height-pinY), (x - lineWidth/2, height-y), lineWidth)
    pg.draw.circle(screen, (0, 0, 0), (pinX, height-pinY), lineWidth*1.5)
    pg.draw.circle(screen, pendColor, (x, height-y), radius)
    pg.draw.circle(screen, (0, 0, 0), (x, height-y), radius, width=lineWidth)

# Main Loop

while running:
    handleEvents()
    screen.fill((100, 100, 100))

    moveObjects()
    drawObjects()

    pg.display.flip() # push the contents of screen Surface to the display

    pg.display.set_caption(f'Pendulum Sim ------ (fps = {str(round(clock.get_fps()))})')

    # clock.tick computes time since previous call.  fps argument will make it delay to keep program running at desired frame rate
    #clock.tick(fps)
    clock.tick_busy_loop(fps) # is more accurate than clock.tick

