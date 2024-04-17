from simulations.free_fall import FreeFall
import matplotlib.pyplot as plt
from methods.simple import Simple
from methods.verlet import Verlet
from methods.theory import Theory
from definitions import Object, Conditions
import numpy

global running
running = True
size = 600, 600
fps = 60
visual = False
graph = True

def main():
    time = 0
    simulationSimple = FreeFall()
    simuationVerlet = FreeFall()
    simulationTheory = FreeFall()
    objectsSimple = [Object(10.0, numpy.array([0, 10000]), numpy.array([0, 0]))]
    objectsVerlet = [Object(10.0, numpy.array([0, 10000]), numpy.array([0, 0]))]
    objectsTheory = [Object(10.0, numpy.array([0, 10000]), numpy.array([0, 0]))]
    simple = Simple()
    verlet = Verlet()
    theory = Theory()

    conditions = Conditions(differenceTime=10, acceleration=numpy.array([0, -9.8]))

    timeData = [0]
    positionData = {
        "simple": [objectsSimple[0].position[1]],
        "verlet": [objectsVerlet[0].position[1]],
        "theory": [objectsTheory[0].position[1]]
    }
    velocityData = {
        "simple": [objectsSimple[0].velocity[1]],
        "verlet": [objectsVerlet[0].velocity[1]],
        "theory": [objectsTheory[0].velocity[1]]
    }

    while running:
        if time > 60: 
            break

        # Simple simulation
        simulationSimple.update(simple, objectsSimple, conditions)

        if simulationSimple.end:
            break
        
        positionData["simple"].append(objectsSimple[0].position[1])
        velocityData["simple"].append(objectsSimple[0].velocity[1])

        # Verlet simulation
        simuationVerlet.update(verlet, objectsVerlet, conditions)

        if simuationVerlet.end:
            break

        positionData["verlet"].append(objectsVerlet[0].position[1])
        velocityData["verlet"].append(objectsVerlet[0].velocity[1])

        # Theoretical simulation
        simulationTheory.update(theory, objectsTheory, conditions)

        if simulationTheory.end:
            break
        
        positionData["theory"].append(objectsTheory[0].position[1])
        velocityData["theory"].append(objectsTheory[0].velocity[1])

        time += conditions.differenceTime
        timeData.append(time)

    

    print("PositionSimple: ", positionData["simple"][-1], "VelocitySimple: ", velocityData["simple"][-1], "Time: ", time)
    print("PositionVerlet: ", positionData["verlet"][-1], "VelocityVerlet: ", velocityData["verlet"][-1], "Time: ", time)
    print("PositionTheory: ", positionData["theory"][-1], "VelocityTheory: ", velocityData["theory"][-1], "Time: ", time)
    
    print("Simple length: ", len(positionData["simple"]))
    print("Verlet length: ", len(positionData["verlet"]))
    print("Theory length: ", len(positionData["theory"]))
    


    plt.figure()
    plt.subplot(211)
    plt.ylabel('Height (m)')
    plt.plot(timeData, positionData["simple"], color='red')  
    plt.plot(timeData, positionData["verlet"], linestyle='--', color='green')
    plt.plot(timeData, positionData["theory"], linestyle='--', color='blue')


    plt.subplot(212)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.plot(timeData, velocityData["simple"], color='red')
    plt.plot(timeData, velocityData["verlet"], color='green')
    plt.plot(timeData, velocityData["theory"], linestyle='--', color='blue')

    plt.savefig("free_fall.png")


if __name__ == '__main__':
    main()
