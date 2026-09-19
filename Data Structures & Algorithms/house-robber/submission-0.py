class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11
        
        def dfs(i):
            if i >= len(nums):
                return 0
            
            rob = nums[i] + dfs(i+2)
            next = dfs(i+1)

            return max(rob, next)
        
        return dfs(0)
