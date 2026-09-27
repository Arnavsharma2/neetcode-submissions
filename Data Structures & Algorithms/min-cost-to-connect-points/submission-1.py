class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        connected = [points[0]]
        best = {}
        while points:
            candidate = (float('inf'), [])
            x = connected[-1]
            for i in range(len(points)):
                y = points[i]
                dist = abs(x[0]-y[0]) + abs(x[1]-y[1])
                key = tuple(y)
                best[key] = min(best.get(key, float('inf')), dist)
                if best[key] < candidate[0]:
                    candidate = (best[key], y)
            if candidate:
                res += candidate[0]
                connected.append(candidate[1])
                points.remove(candidate[1])

        
        return res