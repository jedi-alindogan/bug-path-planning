import numpy as np

class Obstacle:
    def __init__(self, vertices):
        self.setVertices(vertices)
        self.setEdges(vertices)

    def __repr__(self):
        return f"Obstacle(vertices={self.vertices})"
    
    def setVertices(self, vertices):
        self.vertices = vertices

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
        
    def getIndexFromVertex(self, vertice):
        try:
            return self.vertices.index(vertice)
        except ValueError:
            raise ValueError("The given vertex is not in the obstacle.")
    
    def isValidIndex(self, index, n):
        if 0 <= index < n:
            return True
        raise IndexError("current_index out of range")
