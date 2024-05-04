import numpy

def magnitude(vector: numpy.ndarray) -> float:
    return numpy.sqrt(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2))