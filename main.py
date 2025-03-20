from map import Map
from obstacles import Obstacle

def testObstacles():
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    obstacle = Obstacle(vertices)
    
    print("Vertices:")
    print(obstacle.getVertices())
    print("\nAll Edges:")
    for edge in obstacle.getEdges():
        print(edge)
    
    n = len(vertices)
    for i in range(n):
        print(f"\nFor index {i} ({vertices[i]}):")
        print("Right Edge:", obstacle.getRightEdge(i))
        print("Left Edge:", obstacle.getLeftEdge(i))

def testMap():
    square = Obstacle([(0, 0), (2, 0), (2, 2), (0, 2)])
    triangle = Obstacle([(3, 3), (5, 3), (4, 5)])
    obstacles = [square, triangle]
    trajectories = [(0,0), (1,1), (4,1)]
    map = Map(xbounds = (-5,5), ybounds = (-5,5), title = "TEST")
    map.drawMap(trajectories, obstacles, save_path='saved_map.png')
    print("Map saved to saved_map.png")

if __name__ == '__main__':
    testMap()