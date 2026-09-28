class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1


        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]

        return nums[fast]