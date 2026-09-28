class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        visited = set()

        def backtrack(start):
            res.append(path.copy())
            
            for i in range(start, len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                backtrack(i + 1)
                visited.remove(nums[i])
                path.pop()
        
        backtrack(0)
        return res
                
