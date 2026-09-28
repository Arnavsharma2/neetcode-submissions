class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1


        while nums[slow] != nums[fast] and slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        return nums[fast]