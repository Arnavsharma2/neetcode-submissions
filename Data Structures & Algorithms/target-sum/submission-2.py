class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        res = 0
        visited = {}
        self.res = 0
        def backtrack(i, curr):
            if i == len(nums) and curr == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, curr) in visited:
                return visited[(i, curr)]
            
            plus = backtrack(i+1, curr+nums[i])
            minus = backtrack(i+1, curr-nums[i])
            visited[(i, curr)] = plus + minus

            return plus + minus

        
        return backtrack(0, 0)


        


        
        
        