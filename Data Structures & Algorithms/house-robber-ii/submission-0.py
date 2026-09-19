class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, first):
            if i == len(nums)-1 and first:
                return 0
            if (i, first) in memo:
                return memo[(i, first)]
            if i >= len(nums):
                return 0

            if i == 0:
                rob = nums[i] + dfs(i + 2, True)
                next = dfs(i + 1, False)
            else:
                rob = nums[i] + dfs(i + 2, first)
                next = dfs(i + 1, first)

            memo[(i, first)] = max(rob, next)

            return max(rob, next)
        
        return dfs(0, False)