class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for fix in range(len(nums)):
            if nums[fix] == nums[fix-1] and fix > 0:
                continue
            l = fix + 1
            r = len(nums)-1
            while l < r:
                summ = nums[fix] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[fix], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return res
                    



