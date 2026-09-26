class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            x, y = point
            dist = math.sqrt(x**2+y**2)
            if len(maxHeap) == k and -maxHeap[0][0] > dist:
                heapq.heappushpop(maxHeap, (-dist,point))
            elif len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist,point))

        
        res = []
        for i in range(len(maxHeap)):
            _, point = maxHeap.pop()
            res.append(point)
        return res

