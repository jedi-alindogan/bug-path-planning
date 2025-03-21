import numpy as np
from utils import Utilities

MOTION_TO_GOAL = 0
BOUNDARY_FOLLOWING = 1
LEFT = 0
RIGHT = 1
DIRECTION = LEFT

# class Bug2:

"""
    Idea:
    1) given a start and goal first compute all the intersection points 
       on the line segment (start, goal) and the obstacles
    2) modify obstacle to include the list of intersection points (this
       should introduce two edges and one extra vertex per intersection)
    
    MotionToGoal
        The orignal motion-to-goal is 
        - Move toward the goal on the MLine
        - if an obstacle is hit, store the hit point and switch to 
          boundary following
        
    BoundaryFollowing
        - Consistently choose a turning direction to follow the bounardy
          until MLine is intersected
        - leave the boundary when a closer point on the MLine is found 
          and an obstacle isn't penetrated
    
    ^exit condition is path[-1] == goal


    Pseudo code:

    # ASSUME THE M LINE DOESN'T GET INTERSECTED MORE THAN ONCE BY ONE OBSTACLE
    do (1) and (2)

    Mline = [start ... list of vertices ... end]
    path = [start]

    while:
        if mode == MOTION_TO_GOAL:
            motionToGoal()
        else: 
            boundaryFollow()

    def motionTogGoal():
        # this only gets called if you're on the MLine and there is free space
        # between k and the k+1 point
        # so just append the k+1 point to the list
        path.append(Mline[k+1])
        mode -> BOUNDARY_FOLLOW()

    def boundaryFollow():
        # you should be at an Mline point here, as Mline points have been appendended to every obstacle,
        # find the obstacle that you are on

        # traverse until you reach the second M line point (this traversal should be in a consistent direction)
        # append the vertices traversed including the second Mline point
        # something like path.extend([list of vertices up to Mline Point 2])
        # then switch mode
        mode-> MOTION_TO_GOAL
"""
