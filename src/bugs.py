import numpy as np
from utils import Intersections

MOTION_TO_GOAL = 0
BOUNDARY_FOLLOWING = 1
        
class Bug1:
    def __init__(self, robot, start, goal, obstacles):
        '''

        '''
        self.robot = robot
        self.curr = start
        self.goal = goal
        self.hit  = None
        self.mode = MOTION_TO_GOAL
        self.path = [start]
        self.obstacles = obstacles

    def solve(self):
        '''
            Returns a path (list of vertices) that takes the robot
            from start to goal.
        '''
        while True: # exit condition is path[-1] = goal or there is no feasible path (need to figure this part)
            if self.mode == MOTION_TO_GOAL:
                self.motionToGoal()
            else:
                self.followBoundary()

    def motionToGoal(self):
        '''
            Move on a straight line toward the goal, or until an obstacle is hit,
            then return the hit point location.
        '''
        # Move toward the goal or the first obstacle intersection
        hit, obstacle_hit = Intersections.findMinimumObstacleIntersection([self.curr, self.goal], self.obstacles)
        if hit == None:
            hit = self.goal
        
        # Add hit point to path
        self.path.append(hit)
    
    def followBoundary(self):
        # "Circumnavigate ith obstacle (return to hit),
        #  Move to closest point,
        #  Switch to Motion-to-Goal Mode if path to qF departs 
        #       from boundary else return failure

        pass








            


