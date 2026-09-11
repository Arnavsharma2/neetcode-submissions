class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = set(nums)
        maxi = 0
        for num in nums:
            i = 1
            tempMax = 1
            if num-1 not in search:
                while num + i in search:
                    i += 1
                    tempMax += 1
            maxi = max(tempMax, maxi)

        return maxi
