class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        if not nums:
            return 0
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            prev = dp[i-1]
            curr = nums[i]
            if prev + curr < 0:
                dp[i] = 0
            elif abs(prev) > curr and prev < curr:
                dp[i] = curr
            else:
                dp[i] = curr + prev

        return max(dp)
                