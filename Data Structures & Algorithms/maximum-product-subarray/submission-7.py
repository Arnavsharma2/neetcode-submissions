class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        if len(nums) == 1:
            return nums[0]

        runningSum = nums[0]
        negativeMult = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            if runningSum == 0:
                runningSum = 1
                negativeMult = 1
            
            if negativeMult > 0:
                negativeMult *= num
            runningSum *= num

            if runningSum != negativeMult:
                res = max(res, runningSum, runningSum//negativeMult)
            else:
                res = max(res, runningSum)

        return res