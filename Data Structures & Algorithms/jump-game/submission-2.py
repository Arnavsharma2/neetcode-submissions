class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        visited = {}
        def paths(i):
            if i >= len(nums)-1:
                visited[i] = True
                return True
            if nums[i] == 0:
                visited[i] = False
                return False
            if i in visited:
                return visited[i]
            
            for j in range(1, nums[i]+1):
                if paths(i+j):
                    return True
                else:
                    visited[i] = False
            
            return False

        return paths(0)