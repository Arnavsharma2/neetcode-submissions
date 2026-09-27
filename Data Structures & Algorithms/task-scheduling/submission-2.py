class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = {}
        for task in tasks:
            countDict[task] = countDict.get(task, 0) + 1

        maxHeap = []
        heapq.heapify(maxHeap)
        for key, freq in countDict.items():
            heapq.heappush(maxHeap, -freq)
        
        cycle = 0
        cooldown = deque()
        while maxHeap or cooldown:
            if cooldown and cooldown[0][1] == cycle:
                heapq.heappush(maxHeap, -cooldown.popleft()[0])
            if maxHeap:
                freq = -heapq.heappop(maxHeap) - 1
                if freq != 0:
                    cooldown.append((freq, cycle + n + 1))
            cycle += 1
        
        return cycle



