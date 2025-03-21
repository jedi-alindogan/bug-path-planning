import numpy as np
from utils import Utilities

class Obstacle:
    def __init__(self, vertices):
        self.utils = Utilities() 
        self.setVertices(vertices)
        self.setEdges(vertices)

    def __repr__(self):
        return f"Obstacle(vertices={self.vertices})"
    
    def getLength(self):
        return len(self.vertices)
    
    def setVertices(self, vertices):
        self.vertices = np.array(vertices)

    def getVertices(self):
        return self.vertices
    
    def getRightVertex(self, current_index):
        n = len(self.vertices)
        if self.isValidIndex(current_index, n):
            return self.vertices[(current_index + 1) % n]

    def getLeftVertex(self, current_index):
        n = len(self.vertices)
        if self.isValidIndex(current_index, n):
            return self.vertices[(current_index - 1) % n]
        
    def getVertexIndex(self, vertex):
        vertices = self.getVertices()
        for i, v in enumerate(vertices):
            if np.allclose(v, vertex):
                return i
        raise ValueError("Vertex not found in obstacle.")

    def setEdges(self, vertices):
        n = len(vertices)
        self.edges = [(vertices[i], vertices[(i + 1) % n]) for i in range(n)]
    
    def getEdges(self):
        return self.edges

    def getRightEdge(self, current_index):
        n = len(self.vertices)
        if self.isValidIndex(current_index, n):
            return (self.vertices[current_index], self.vertices[(current_index + 1) % n])

    def getLeftEdge(self, current_index):
        n = len(self.vertices)
        if self.isValidIndex(current_index, n):
            return (self.vertices[(current_index - 1) % n], self.vertices[current_index])
        
    def insertVertex(self, node, index):

        vertices = self.getVertices().tolist()
        n = len(vertices)
        if self.isValidIndex(index, n):
            insert_index = index + 1
            vertices.insert(insert_index, node)
            self.setVertices(vertices)
            self.setEdges(vertices)

    def closestEdge(self, point):
        best_edge = None
        best_dist = np.inf
        for edge in self.getEdges():
            d = self.utils.findPointToSegmentDistance(point, edge)
            if d < best_dist:
                best_dist = d
                best_edge = edge
        return best_edge
    
    def isValidIndex(self, index, n):
        if 0 <= index < n:
            return True
        raise IndexError("current_index out of range")
