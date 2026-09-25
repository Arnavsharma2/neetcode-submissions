class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            if len(minHeap) == k and minHeap[0] < num:
                heapq.heappushpop(minHeap, num)
            elif len(minHeap) != k:
                heapq.heappush(minHeap, num)
        
        return minHeap[0]

