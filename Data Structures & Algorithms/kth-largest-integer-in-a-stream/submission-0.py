class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        minHeap = []
        heapq.heapify(minHeap)
        for num in nums:
            heapq.heappush(minHeap, num)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        self.minHeap = minHeap
        

    def add(self, val: int) -> int:
        if self.minHeap[0] < val:
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]
        
        
