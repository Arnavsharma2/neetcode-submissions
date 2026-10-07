class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            if len(maxHeap) == k and maxHeap[0] < num:
                heapq.heappushpop(maxHeap, num)
            elif len(maxHeap) < k:
                heapq.heappush(maxHeap, num)
        
        return maxHeap[0]
            
            
            
