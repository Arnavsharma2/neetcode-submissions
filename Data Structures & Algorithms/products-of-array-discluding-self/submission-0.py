class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        left[0] = 1
        prod = 1
        for i in range(1, len(nums)):
            left[i] *= nums[i-1]*prod
            prod *= nums[i-1]
        
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            left[i] *= nums[i+1]*prod
            prod *= nums[i+1]
    

        return left
