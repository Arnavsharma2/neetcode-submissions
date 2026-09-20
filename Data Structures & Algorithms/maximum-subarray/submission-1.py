class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [float('-inf')] * len(nums)
        if not nums:
            return 0
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            prev = dp[i-1]
            curr = nums[i]
            if abs(prev) > curr and prev < curr:
                dp[i] = curr
            elif prev + curr < 0:
                dp[i] = 0
            else:
                dp[i] = curr + prev

        return max(dp)
                