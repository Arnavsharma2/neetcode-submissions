class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        # -1 2 100 4
        # -1 2 100 -2
        if not nums:
            return 0
        best = 0
        currMax = nums[0]
        currMin = nums[0]
        for i in range(1, len(nums)):
            tempMin = currMin
            tempMax = currMax
            currMin = min(nums[i], nums[i]*tempMin, tempMax*nums[i])
            currMax = max(nums[i], nums[i]*tempMax, tempMin*nums[i])

            best = max(best, currMax)
        return best
            

            

