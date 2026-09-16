class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif self.minHeap[0] > num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap)-len(self.maxHeap) >= 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))

        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0]
        
        