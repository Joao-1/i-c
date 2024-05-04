import numpy
from core.physics.constants import EARTH_MASS, EARTH_RADIUS
from core.physics.interfaces import Planet

class Earth(Planet):
    def __init__(self):
        super().__init__(EARTH_MASS, EARTH_RADIUS, "Earth")


