
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        bucketDict = defaultdict(list)
        for num, freq in freqDict.items():
            bucketDict[freq].append(num)
        
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in bucketDict:
                for num in bucketDict[freq]:
                    res.append(num)
                    if len(res) == k:
                        return res
        
        return res

            