class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        res = 0
        path = []

        visited = {}

        def dfs(i, total):
            if total == target and i == len(nums):
                return 1
            elif i >= len(nums):
                return 0
            elif (i, total) in visited:
                return visited[(i, total)]
            
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])
            visited[(i, total)] = add + sub

            return add + sub
        
        return dfs(0, 0)