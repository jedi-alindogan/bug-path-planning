import numpy as np

class Utilities:
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
                if (self.isPointOnSegment(line[0], line[1], pt) and
                    self.isPointOnSegment(edge[0], edge[1], pt)):
                    intersections.append(pt)
        return np.vstack(intersections) if intersections else None

    def findAllObstacleIntersections(self, line, obstacles):
        start = np.array(line[0])
        intersections = []
        
        for obstacle in obstacles:
            pts = self.findObstacleIntersections(line, obstacle)
            if pts is not None and pts.size:
                for pt in pts:
                    dist = np.linalg.norm(pt - start)
                    intersections.append((dist, obstacle, pt))
        
        intersections.sort(key=lambda x: x[0])
        
        return [(obstacle, pt) for _, obstacle, pt in intersections]

    def isPointOnSegment(self, point1, point2, point):
        x1, y1 = point1
        x2, y2 = point2
        x0, y0 = point
        cross_prod = (x2 - x1) * (y0 - y1) - (y2 - y1) * (x0 - x1)
        if not np.isclose(cross_prod, 0):
            return False
        if not (min(x1, x2) <= x0 <= max(x1, x2) or np.isclose(x0, min(x1, x2)) or np.isclose(x0, max(x1, x2))):
            return False
        if not (min(y1, y2) <= y0 <= max(y1, y2) or np.isclose(y0, min(y1, y2)) or np.isclose(y0, max(y1, y2))):
            return False
        return True

    def findEdgeFromPoint(self, point, obstacle):
        for edge in obstacle.getEdges():
            point1, point2 = edge
            if self.isPointOnSegment(point1, point2, point):
                return edge
        print(f"Point {point} was not on obstacle boundary.")
        return None
    
    def findPointToSegmentDistance(self, point, edge):
        P = np.array(point)
        A, B = np.array(edge[0]), np.array(edge[1])
        AB = B - A
        t = np.dot(P - A, AB) / np.dot(AB, AB)
        t = np.clip(t, 0, 1)
        proj = A + t * AB
        return np.linalg.norm(P - proj)

    def findClosestPointOnLine(self, point, line):
        A, B, P = map(np.array, (*line, point))
        AB = B - A
        denom = np.dot(AB, AB)
        if np.isclose(denom, 0):
            # The line segment is degenerate; return one of the endpoints (A).
            return A
        t = np.dot(P - A, AB) / denom
        t = np.clip(t, 0, 1)
        return A + t * AB

    def findClosestPointOnObstacle(self, point, obstacle):
        minDist = np.inf
        minPoint = None

        for edge in obstacle.getEdges():
            candidate = self.findClosestPointOnSegment(point, edge)
            dist = np.linalg.norm(candidate - np.array(point))

            if dist < minDist:
                minDist = dist
                minPoint = candidate

        return minPoint

    # def computeDistance(self, points):
    #     points = np.array(points)
    #     diffs = np.diff(points, axis=0)
    #     distances = np.linalg.norm(diffs, axis=1)
    #     return np.sum(distances)

    # def findShortestPathOnObstacle(self, point1, point2, obstacle):
    #     # Find edges containing the points
    #     edge1 = self.findEdgeFromPoint(point1, obstacle)
    #     edge2 = self.findEdgeFromPoint(point2, obstacle)

    #     if edge1 is None or edge2 is None:
    #         raise ValueError("One or both points are not on the obstacle boundary.")

    #     # **Case 1: Both points are on the same edge**
    #     if edge1 == edge2:
    #         return [point1, point2]  # Shortest path is the direct segment

    #     # **Case 2: Points are on different edges, traverse the obstacle boundary**
        
    #     # Determine the closest vertices
    #     v1, v2 = edge1  # Endpoints of edge containing point1
    #     u1, u2 = edge2  # Endpoints of edge containing point2

    #     # Find the closest vertices to the points
    #     closest_v1 = v1 if np.linalg.norm(np.array(point1) - np.array(v1)) < np.linalg.norm(np.array(point1) - np.array(v2)) else v2
    #     closest_v2 = u1 if np.linalg.norm(np.array(point2) - np.array(u1)) < np.linalg.norm(np.array(point2) - np.array(u2)) else u2

    #     # Traverse left and right
    #     left_traversal = obstacle.traverseLeftFromVertex(closest_v1)
    #     right_traversal = obstacle.traverseRightFromVertex(closest_v1)

    #     # Find index of closest_v2 in both traversals
    #     try:
    #         left_index = left_traversal.index(closest_v2)
    #         right_index = right_traversal.index(closest_v2)
    #     except ValueError:
    #         raise ValueError("Vertices are not reachable in traversal.")

    #     # Extract paths and compute distances
    #     left_path = [point1] + left_traversal[:left_index + 1] + [point2]
    #     right_path = [point1] + right_traversal[:right_index + 1] + [point2]

    #     left_distance = self.computeDistance(left_path)
    #     right_distance = self.computeDistance(right_path)

    #     # Return the shortest path
    #     return left_path if left_distance < right_distance else right_path