class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        if nums[0] == target:
            return 0

        while l < r:
            m = (r-l)//2 + l
            if nums[m] == target:
                return m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return -1