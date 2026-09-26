class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        minHeap = []
        heapq.heapify(minHeap)
        for num in nums:
            heapq.heappush(minHeap, num)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        self.minHeap = minHeap
        

    def add(self, val: int) -> int:
        if not self.minHeap:
            heapq.heappush(self.minHeap, val)
        elif self.minHeap[0] < val:
            heapq.heappushpop(self.minHeap, val)
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]

        
