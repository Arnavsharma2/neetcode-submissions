class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        minHeap = []
        index = defaultdict(list)
        for i in range(len(temperatures)):
            index[temperatures[i]].append(i)

        heapq.heapify(minHeap)
        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            while minHeap and minHeap[0] < curr:
                for pos in index[minHeap[0]]:
                    res[pos] = i-pos
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, curr)
        
        return res


