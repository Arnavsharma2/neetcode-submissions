class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            x, y = point
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(minHeap, (dist,point))

        while len(minHeap) > k:
            minHeap.pop()
        
        res = []
        for i in range(len(minHeap)):
            _, point = minHeap.pop()
            res.append(point)
        return res

