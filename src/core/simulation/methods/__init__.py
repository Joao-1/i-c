from enum import Enum

from core.simulation.methods.simple import Simple
from core.simulation.methods.verlet import Verlet

class Methods(Enum):
    SIMPLE = Simple
    VERLET = Verlet