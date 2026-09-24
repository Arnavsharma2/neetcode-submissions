class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        check = set()

        for num in nums:

            for i in range(len(res)):
                newArr = res[i] + [num]
                newArr.sort()
                if tuple(newArr) not in check:
                    check.add(tuple(newArr))
                    res.append(newArr)
        
        return res
