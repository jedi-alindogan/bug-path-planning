import numpy as np
from map import Map
from obstacles import Obstacle
from utils import Intersections

def testIntersections():
    # Create obstacles
    square = Obstacle([(0, 0), (2, 0), (2, 2), (0, 2)])
    triangle = Obstacle([(3, 3), (5, 3), (4, 5)])
    obstacles = [square, triangle]

    # Define start and goal points
    start = np.array([-1, -1])
    goal = np.array([-1, 6])
    line = (start, goal)

    # Find the closest intersection along the line (if any)
    inter_obj = Intersections()
    minIntersection, minObstacle = inter_obj.findMinimumObstacleIntersection(line, obstacles)

    # Define the path: if an intersection is found, draw to it; else, draw full line to goal.
    if minIntersection is not None:
        path = [start, minIntersection]
        print("Intersection found at:", minIntersection)
    else:
        path = [start, goal]
        print("No intersection found; drawing full line.")

    # Create a map and draw obstacles and the path
    map_obj = Map(xbounds=(-5, 7), ybounds=(-5, 7), title="Test Map")
    fig, ax = map_obj.drawMap(obstacles=obstacles, path=path)
    map_obj.saveMap(fig, save_path='map.png')
    print("Map saved to saved_map.png")

if __name__ == '__main__':
    testIntersections()