import numpy as np
from obstacles import Obstacle

class Robot:
    def __init__(self, position):
        self.position = np.array(position)

    def moveToVertex(self, goal, obstacles):