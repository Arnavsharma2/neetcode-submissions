class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        countDict = {}
        for num in hand:
            countDict[num] = countDict.get(num, 0) + 1
        
        group = groupSize
        val = 0
        while countDict:
            if group == groupSize:
                val = max(countDict.keys())
                countDict[val] -= 1
                if countDict[val] == 0:
                    del countDict[val]
                group = 1
            if group < groupSize:
                if val - 1 not in countDict:
                    return False
                if countDict[val - 1] == 0:
                    return False
                countDict[val-1] -= 1
                if countDict[val - 1] == 0:
                    del countDict[val-1]
            
                val -= 1
                group += 1
        if group == groupSize:
            return True
        return False
