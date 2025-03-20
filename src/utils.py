import numpy as np

class Intersections:

    def findLineIntersection(self, line1, line2):
        A, B = map(np.array, line1)
        C, D = map(np.array, line2)
        L1 = np.array([B[1] - A[1], A[0] - B[0]])
        L2 = np.array([D[1] - C[1], C[0] - D[0]])
        c1 = L1.dot(A)
        c2 = L2.dot(C)
        det = np.linalg.det(np.vstack((L1, L2)))
        if np.isclose(det, 0):
            return None
        x = (L2[1] * c1 - L1[1] * c2) / det
        y = (L1[0] * c2 - L2[0] * c1) / det
        return np.array([x, y])

    def findObstacleIntersections(self, line, obstacle):
        intersections = []
        for edge in obstacle.getEdges():
            pt = self.findLineIntersection(line, edge)
            if pt is not None:
                intersections.append(pt)
        return np.vstack(intersections) if intersections else None

    def findMinimumObstacleIntersection(self, line, obstacles):
        start = np.array(line[0])
        minIntersection = None
        minDist = np.inf
        minObstacle = None
        for obstacle in obstacles:
            pts = self.findObstacleIntersections(line, obstacle)
            if pts is not None and pts.size:
                dists = np.linalg.norm(pts - start, axis=1)
                idx = np.argmin(dists)
                if dists[idx] < minDist:
                    minDist = dists[idx]
                    minIntersection = pts[idx]
                    minObstacle = obstacle
        return minIntersection, minObstacle
