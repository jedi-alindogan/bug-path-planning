import numpy as np

MOTION_TO_GOAL = 0
BOUNDARY_FOLLOWING = 1

# move these somewhere else like utils.py
def line_to_line_intersection(line1, line2):

def line_to_obstacle_intersections(line, obstacle):
    intersections = []
    for edge in obstacle:
        intersection = line_to_line_intersection(line, edge)
        if intersection:
            intersections.append(intersection)
    return intersections
        
class Bug1:
    def __init__(self, start, goal, Map):
        '''

        '''
        self.curr = start
        self.goal = goal
        self.hit  = None
        self.mode = MOTION_TO_GOAL
        self.path = [start]
        self.obstacles = Map.obstacles

    def search(self):
        '''

        '''

        # Motion-to-Goal Mode
        if self.mode == MOTION_TO_GOAL:
            # "Move on a straight line toward goal, 
            #  Move until obstacle is hit, 
            #  Store hit point location"

            # Compute intersections
            


            # Switch to Boundary-Following Mode
            self.mode = BOUNDARY_FOLLOWING
        
        # Boundary-Following Mode
        else:
            # "Circumnavigate ith obstacle (return to hit),
            #  Move to closest point,
            #  Switch to Motion-to-Goal Mode if path to qF departs 
            #       from boundary else return failure

            pass
    
    def get_intersections(self, point): # change name if needed
        intersections = []
        for obstacle in self.obstacles:
            # Here, I think you can add to lists to append them
            intersections = intersections + \
                line_to_obstacle_intersections([self.curr, point], obstacle)






            


