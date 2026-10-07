class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [1]*len(nums)
        for i in range(1, len(nums)):
            forward[i] = nums[i-1]*forward[i-1]

        backward = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            backward[i] = nums[i+1]*backward[i+1]
            forward[i] *= backward[i]
        return forward
        # 1 1 2 8
        # 48 24 6 1
        
