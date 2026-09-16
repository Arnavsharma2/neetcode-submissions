class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def backtrack(i, remaining, path):
            if i >= len(nums) or remaining < 0:
                return
            
            if remaining == 0:
                self.res.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i, remaining-nums[i], path)
            del path[-1]
            backtrack(i+1, remaining, path)

        backtrack(0, target, [])
        return self.res


            