class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            rob = nums[i] + dfs(i+2)
            next = dfs(i+1)
            memo[i] = max(rob, next)

            return max(rob, next)
        
        return dfs(0)
