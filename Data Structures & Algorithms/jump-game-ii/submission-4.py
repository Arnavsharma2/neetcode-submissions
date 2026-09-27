class Solution:
    def jump(self, nums: List[int]) -> int:
        
        visited = {}
        def paths(i):
            if i >= len(nums)-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            if i in visited:
                return visited[i]
            
            best = float('inf')
            for j in range(1, nums[i]+1):
                best = min(best, 1 + paths(i + j))
                visited[i] = best
            
            return best
        
        return paths(0)
                    
