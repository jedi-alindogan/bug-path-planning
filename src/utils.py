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

    def isPointOnSegment(self, point1, point2, point, tol=1e-9):
        """Check if point point lies on the line segment between point1 and point2.

        Parameters:
            point1 (list or tuple): [x1, y1] first endpoint of the segment.
            point2 (list or tuple): [x2, y2] second endpoint of the segment.
         point (list or tuple): [x0, y0] point to check.
            tol (float): tolerance for floating-point comparisons.

        Returns:
            bool: True if point is on the segment, False otherwise.
        """
        x1, y1 = point1
        x2, y2 = point2
        x0, y0 = point

        # Check collinearity using the determinant condition
        if abs((x2 - x1) * (y0 - y1) - (y2 - y1) * (x0 - x1)) > tol:
            return False  # Not collinear

        # Check if the point is within the bounding box of the segment
        return min(x1, x2) - tol <= x0 <= max(x1, x2) + tol and min(y1, y2) - tol <= y0 <= max(y1, y2) + tol
    
    def findEdgeFromHit(self, hit, obstacle, tol=1e-9):
        for (idx, edge) in enumerate(obstacle.getEdges()):
            point1, point2 = edge
            if self.isPointOnSegment(point1, point2, hit, tol):
                return edge
        print(f"Point {hit} was not on obstacle boundary.")
        return None
    
