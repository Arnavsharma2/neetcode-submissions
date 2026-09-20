class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        for i in range(len(nums)+1):
            expected += i
        return expected-sum(nums)