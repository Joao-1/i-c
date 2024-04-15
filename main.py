import pygame as pg
from simulations.free_fall import FreeFall
from simulations.pendulum import Pendulum
import matplotlib.pyplot as plt
import matplotlib.animation as animation

running = True
size = 600, 600
fps = 60
visual = False
graph = True
pendulum = Pendulum(fps)
freeFall = FreeFall(differenceTime=0.01)

def main():
    simulation = Pendulum(fps)

    if visual:
        pg.init()
        clock = pg.time.Clock()
        screen = pg.display.set_mode(size)

    if graph:
        global figure
        figure = plt.figure()
        figure.show()

    while running:
        if simulation.moveObjects() != None:
            break
        
        if visual:
            simulation.handleEvents(pg.event.get())
            simulation.drawObjects(screen)

            pg.display.set_caption(f'Sim - (fps = {str(round(clock.get_fps()))})')
            pg.display.flip()
            clock.tick_busy_loop(fps) 
    
        if graph:
            simulation.plotGraph(figure)

            figure.canvas.draw()
            figure.canvas.flush_events()
if __name__ == '__main__':
    main()