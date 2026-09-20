class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [float('-inf')] * len(nums)
        if not nums:
            return 0
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            prev = dp[i-1]
            curr = nums[i]
            if prev < 0 and curr > 0:
                dp[i] = curr
            else:
                dp[i] = prev + curr
            print(dp[i])

        return max(dp)
                