class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            if maxHeap and maxHeap[0] < num:
                heapq.heappushpop(maxHeap, num)
            else:
                heapq.heappush(maxHeap, num)
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        return maxHeap[0] if maxHeap else 0
            
            
            
