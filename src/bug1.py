import numpy as np
from utils import Utilities

MOTION_TO_GOAL = 0
BOUNDARY_FOLLOWING = 1
LEFT = 0
RIGHT = 1
DIRECTION = LEFT

class Bug1:
    def __init__(self, robot, goal):
        self.robot = robot
        self.goal = np.array(goal)
        self.mode = MOTION_TO_GOAL
        self.hit = None
        self.obstacle_hit = None

    def solve(self):
        while not self.robot.isAtPosition(self.goal):
            if self.mode == MOTION_TO_GOAL:
                self.motionToGoal()
            else:
                self.followBoundary()
        return self.robot.getTrajectories()

    def motionToGoal(self):
        obstacle, point = self.robot.checkObstacleHit(self.goal)
        if obstacle:
            self.obstacle_hit = obstacle
            self.robot.updateRobotPosition(point)
            self.mode = BOUNDARY_FOLLOWING
        else:
            self.robot.updateRobotPosition(self.goal)
        return

    def followBoundary(self):
        self.robot.circumnavigateObstacle(self.obstacle_hit, direction="right")
        self.robot.goToClosestPointOnObstacle(self.obstacle_hit, self.goal, direction="optimal")
        self.mode = MOTION_TO_GOAL
        return