class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        connected = [points[0]]
        while points:
            candidate = (float('inf'), [])
            for point in connected:
                x = point
                for i in range(len(points)):
                    y = points[i]
                    dist = abs(x[0]-y[0]) + abs(x[1]-y[1])
                    if dist < candidate[0]:
                        candidate = (dist, y)
            if candidate:
                res += candidate[0]
                connected.append(candidate[1])
                points.remove(candidate[1])

        
        return res