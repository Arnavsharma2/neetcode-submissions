class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        minHeap = []

        heapq.heapify(minHeap)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while minHeap and minHeap[0][0] < curr:
                res[minHeap[0][1]] = i-minHeap[0][1]
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, (curr, i))
        
        return res


