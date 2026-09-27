class Solution:
    def jump(self, nums: List[int]) -> int:
        
        self.jumps = float('inf')
        failed = {}
        def paths(i, dist):
            if i >= len(nums)-1:
                self.jumps = min(dist, self.jumps)
                return True
            if nums[i] == 0:
                failed[i] = True
                return False
            if i in failed:
                return failed[i]

            for j in range(1, nums[i]+1):
                paths(i + j, dist + 1)
        
        paths(0, 0)
        return self.jumps
                    
