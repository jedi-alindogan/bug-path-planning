import numpy as np
from obstacles import Obstacle
from utils import Utilities

class Robot:
    def __init__(self, environment, initial_position):
        self.map = environment
        self.utils = Utilities() 
        self.setPosition(initial_position)
        self.setTrajectories([self.getPosition()])

    def setPosition(self, position):
        self.position = np.array(position)

    def getPosition(self):
        return self.position
    
    def getPositionFromIndex(self, index):
        trajectories = self.getTrajectories()
        return trajectories[index]
    
    def setTrajectories(self, trajectories):
        self.trajectories = trajectories

    def getTrajectories(self):
        return self.trajectories
    
    def appendTrajectory(self, trajectory):
        self.trajectories.append(trajectory)

    def updateRobotPosition(self, position):
        self.setPosition(position)
        self.appendTrajectory(self.getPosition())

    def checkObstacleHit(self, goal):
        trajectory = (self.getPosition(), goal)
        intersections = self.utils.findAllObstacleIntersections(trajectory, self.map.obstacles)
        for obstacle, point in intersections:
            if not self.isAtPosition(point):
                return obstacle, point
        return None, None
    
    def isAtPosition(self, goal):
        return np.allclose(self.getPosition(), goal)

    def goToVertex(self, obstacle, index, direction="optimal"):
        start_index = obstacle.getVertexIndex(self.getPosition())

        if direction == "optimal":
            n = obstacle.getLength()
            vertices = obstacle.getVertices()
            i = start_index
            total_distance_right = 0.0
            while i != index:
                next_index = (i + 1) % n
                edge = vertices[next_index] - vertices[i]
                total_distance_right += np.linalg.norm(edge)
                i = next_index
            i = start_index
            total_distance_left = 0.0
            while i != index:
                next_index = (i - 1) % n
                edge = vertices[next_index] - vertices[i]
                total_distance_left += np.linalg.norm(edge)
                i = next_index
            direction = "right" if total_distance_right <= total_distance_left else "left"

        current_index = start_index
        while True:
            if direction == "right":
                next_vertex = obstacle.getRightVertex(current_index)
                current_index = (current_index + 1) % obstacle.getLength()
            elif direction == "left":
                next_vertex = obstacle.getLeftVertex(current_index)
                current_index = (current_index - 1) % obstacle.getLength()
            else:
                raise ValueError("Direction must be 'right', 'left', or 'optimal'")
            self.updateRobotPosition(next_vertex)
            if current_index == index:
                break
    
    def circumnavigateObstacle(self, obstacle, direction="right"):
        edge = self.utils.findEdgeFromPoint(self.getPosition(), obstacle)
        index = obstacle.getVertexIndex(edge[0])
        obstacle.insertVertex(self.getPosition(), index)
        self.goToVertex(obstacle, index+1, direction)

    def goToClosestPointOnObstacle(self, obstacle, goal, direction="right"):
        edge = obstacle.closestEdge(goal)
        closest_point = self.utils.findClosestPointOnLine(goal, edge)
        index = obstacle.getVertexIndex(edge[0])
        obstacle.insertVertex(closest_point, index)
        self.goToVertex(obstacle, index + 1, direction)
