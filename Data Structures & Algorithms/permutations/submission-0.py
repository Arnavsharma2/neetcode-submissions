class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        visited = set()

        def backtrack(i):
            if len(path) == len(nums):
                res.append(path.copy())
                return
                
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                backtrack(i + 1)
                visited.remove(nums[i])
                path.pop()


        

        backtrack(0)
        return res