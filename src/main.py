import matplotlib.pyplot as plt
from core.physics.forces import Forces
from core.physics.equations import Motion
from core.simulation.interfaces import Conditions
from core.simulation.methods import Methods
from core.simulation.simulations.freeFall import FreeFall

def main():
    simulations = [
        FreeFall(Methods.SIMPLE.value, conditions=Conditions(differenceTime=0.1, forces=[(Forces.GRAVITY, {}), (Forces.DRAG, {"dragCoefficient": 0.8})], dragCoefficient=0.8)),
        FreeFall(Methods.VERLET.value, conditions=Conditions(differenceTime=0.1, forces=[(Forces.GRAVITY, {}), (Forces.DRAG, {"dragCoefficient": 0.8})], dragCoefficient=0.8)),
        FreeFall(Motion().withFriction.viscosity, conditions=Conditions(differenceTime=0.1, forces=[(Forces.GRAVITY, {}), (Forces.DRAG, {"dragCoefficient": 0.8})], dragCoefficient=0.8)),
    ]

    while True:
        stop = False

        for simulation in simulations:
            if simulation.end == True:
                continue

            simulation.update()

            stop = simulation.end
        
        if stop == True:
            print("End of simulations")
            break
    
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].set(ylabel='position (m)')
    axs[0, 0].plot(simulations[0].data.time[1:], simulations[0].data.position, color='red', label='Simple')
    axs[0, 0].plot(simulations[1].data.time[1:], simulations[1].data.position, linestyle='--', color='green', label='Verlet')
    axs[0, 0].plot(simulations[2].data.time[1:], simulations[2].data.position, linestyle='--', color='blue', label='Theory')
    axs[0, 0].legend()

    RDPositionRed: list[float] = []
    for redPosition, TheoryPosition in zip(simulations[0].data.position, simulations[2].data.position):
        da = (abs(redPosition - TheoryPosition)/TheoryPosition)*100
        RDPositionRed.append(100) if da > 100 or da < 0  else RDPositionRed.append(da)

    RDPositionGreen: list[float] = []
    for greenPosition, TheoryPosition in zip(simulations[1].data.position, simulations[2].data.position):
        da = (abs(greenPosition - TheoryPosition)/TheoryPosition)*100
        RDPositionGreen.append(100) if da > 100 or da < 0 else RDPositionGreen.append(da)

    axs[0, 1].set(ylabel='R.D (%)')
    axs[0, 1].yaxis.tick_right()
    axs[0, 1].plot(simulations[0].data.time[1:len(simulations[2].data.time)], RDPositionRed, color='red', label='Simple')
    axs[0, 1].plot(simulations[1].data.time[1:len(simulations[2].data.time)], RDPositionGreen, color='green', label='Verlet')
    axs[0, 1].legend()

    axs[1, 0].set(ylabel='velocity (m/s)')
    axs[1, 0].set(xlabel='time (s)')
    axs[1, 0].plot(simulations[0].data.time[1:], simulations[0].data.velocity, color='red', label='Simple')
    axs[1, 0].plot(simulations[1].data.time[1:], simulations[1].data.velocity, color='green', label='Verlet')
    axs[1, 0].plot(simulations[2].data.time[1:], simulations[2].data.velocity, linestyle='--', color='blue', label='Theory')
    axs[1, 0].legend()

    RDVelocityRed: list[float] = []
    for redVelocity, TheoryVelocity in zip(simulations[0].data.velocity, simulations[2].data.velocity):
        da = -(abs(redVelocity - TheoryVelocity)/TheoryVelocity)*100
        RDVelocityRed.append(100) if da > 100 or da < 0  else RDVelocityRed.append(da)

    RDVelocityGreen: list[float] = []
    for greenVelocity, TheoryVelocity in zip(simulations[1].data.velocity, simulations[2].data.velocity):
        da = -(abs(greenVelocity - TheoryVelocity)/TheoryVelocity)*100
        RDVelocityGreen.append(100) if da > 100 or da < 0 else RDVelocityGreen.append(da)

    axs[1, 1].set(ylabel='R.D (%)')
    axs[1, 1].set(xlabel='time (s)')
    axs[1, 1].yaxis.tick_right()
    axs[1, 1].plot(simulations[0].data.time[1:len(simulations[2].data.time)], RDVelocityRed, color='red', label='Simple')
    axs[1, 1].plot(simulations[1].data.time[1:len(simulations[2].data.time)], RDVelocityGreen, color='green', label='Verlet')
    axs[1, 1].legend()

    fig.savefig("free_fall.png")

    import csv

    with open('free_fall.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Time (s)', 'Position Simple (m)', 'Position Verlet (m)', 'Position Theory (m)', 'R.D Position Simple (%)', 'R.D Position Verlet (%)', 'Velocity Simple (m/s)', 'Velocity Verlet (m/s)', 'Velocity Theory (m/s)', 'R.D Velocity Simple (%)', 'R.D Velocity Verlet (%)'])

        for time, positionSimple, positionVerlet, positionTheory, RDPositionSimple, RDPositionVerlet, velocitySimple, velocityVerlet, velocityTheory, RDVelocitySimple, RDVelocityVerlet in zip(simulations[0].data.time[1:], simulations[0].data.position, simulations[1].data.position, simulations[2].data.position, RDPositionRed, RDPositionGreen, simulations[0].data.velocity, simulations[1].data.velocity, simulations[2].data.velocity, RDVelocityRed, RDVelocityGreen):
            writer.writerow([time, positionSimple, positionVerlet, positionTheory, RDPositionSimple, RDPositionVerlet, velocitySimple, velocityVerlet, velocityTheory, RDVelocitySimple, RDVelocityVerlet])

if __name__ == '__main__':
    main()
