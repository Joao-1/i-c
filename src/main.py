from simulations.free_fall import FreeFall
import matplotlib.pyplot as plt
from methods.initial import Initial
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
    simulationMethod = FreeFall()
    simulationTheory = FreeFall()
    objectsMethod = [Object(10.0, numpy.array([0, 10000]), numpy.array([0, 0]))]
    objectsTheory = [Object(10.0, numpy.array([0, 10000]), numpy.array([0, 0]))]
    method = Initial()
    theory = Theory()

    conditions = Conditions(differenceTime=0.01, acceleration=numpy.array([0, -9.8]))

    timeData = [0]
    positionData = {
        "method": [objectsMethod[0].position[1]],
        "theory": [objectsTheory[0].position[1]]
    }
    velocityData = {
        "method": [objectsMethod[0].velocity[1]],
        "theory": [objectsTheory[0].velocity[1]]
    }

    while running:
        # Method simulation
        simulationMethod.update(method, objectsMethod, conditions)

        if simulationMethod.end:
            break
        
        positionData["method"].append(objectsMethod[0].position[1])
        velocityData["method"].append(objectsMethod[0].velocity[1])

        # Theoretical simulation

        simulationTheory.update(theory, objectsTheory, conditions)

        if simulationTheory.end:
            break
        
        positionData["theory"].append(objectsTheory[0].position[1])
        velocityData["theory"].append(objectsTheory[0].velocity[1])

        time += conditions.differenceTime
        timeData.append(time)

        print("PositionMethod: ", objectsMethod[0].position, "VelocityMethod: ", objectsMethod[0].velocity, "Time: ", time)
        print("PositionTheory: ", objectsTheory[0].position, "VelocityTheory: ", objectsTheory[0].velocity, "Time: ", time)
    

    plt.figure()
    plt.subplot(211)
    plt.ylabel('Height (m)')
    plt.plot(timeData, positionData["method"])  
    plt.plot(timeData, positionData["theory"], linestyle='--', color='red')


    plt.subplot(212)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.plot(timeData, velocityData["method"])
    plt.plot(timeData, velocityData["theory"], linestyle='--', color='red')

    plt.savefig("free_fall.png")


if __name__ == '__main__':
    main()
