class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [0,1,2,3]
        # [1,4,2,3]
        # [1,2,2,3]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)



