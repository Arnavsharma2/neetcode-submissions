class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}
        def dfs(i):
            if i == len(nums)-1:
                return True
            if nums[i] == 0 or i >= len(nums):
                memo[i] = False
                return False
            
            if i in memo:
                return memo[i]

            for j in range(nums[i]):
                if dfs(i+j+1):
                    return True
            return False

        return dfs(0)   
