import numpy as np
from obstacles import Obstacle
from map import Map
from utils import Intersections

def testIntersections():
    square = Obstacle([(0, 0), (2, 0), (2, 2), (0, 2)])
    triangle = Obstacle([(3, 3), (5, 3), (4, 5)])
    obstacles = [square, triangle]

    start = np.array([-1, -1])
    goal = np.array([6, 6])
    line = (start, goal)

    inter = Intersections()
    intersection = inter.findMinimumObstacleIntersection(line, obstacles)
    
    if intersection is not None:
        path = [start, intersection]
        print("Intersection found at:", intersection)
    else:
        path = [start, goal]
        print("No intersection found; drawing full path.")

    map_obj = Map(xbounds=(-5, 7), ybounds=(-5, 7), title="Intersections Test Map")
    fig, ax = map_obj.drawMap(obstacles=obstacles, path=path)
    map_obj.saveMap(fig, save_path="test_map.png")
    print("Map saved to test_map.png")

if __name__ == '__main__':
    testIntersections()