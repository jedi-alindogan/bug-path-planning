import numpy as np
from map import Map
from obstacles import Obstacle
from robot import Robot
from bug1 import Bug1

def test_bug_algorithm_separated_obstacles():
    # Define the first obstacle as a square from (0, 0) to (2, 2)
    obstacle1 = Obstacle([(0, 0), (2, 0), (2, 2), (0, 2)])
    
    # Define the second obstacle as a circle approximated by vertices.
    # Circle center at (4, 1) with radius 1, using 30 vertices.
    center = (4, 1)
    radius = 1
    num_vertices = 30
    angles = np.linspace(0, 2 * np.pi, num=num_vertices, endpoint=False)
    circle_vertices = [(center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta)) for theta in angles]
    obstacle2 = Obstacle(circle_vertices)
    
    obstacles = [obstacle1, obstacle2]
    
    # Create a map with bounds to view the scenario clearly.
    map_obj = Map(xbounds=(-5, 8), ybounds=(-5, 8),
                  title="Bug1 Separated Obstacles Test Map", obstacles=obstacles)
    
    # Set the start position to the left of both obstacles and the goal to the right.
    start = np.array([-3, 1])
    goal = np.array([7, 1])
    
    robot = Robot(map_obj, start)
    bug_algorithm = Bug1(robot, goal)
    trajectory = bug_algorithm.solve()
    
    fig, ax = map_obj.drawMap(obstacles=obstacles, trajectories=trajectory)
    map_obj.saveMap(fig, save_path='bug1_separated_obstacles_map.png')
    print("Bug1 separated obstacles test map saved to bug1_separated_obstacles_map.png")

if __name__ == '__main__':
    test_bug_algorithm_separated_obstacles()