class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # overlap
        # before
        # after
        # [[1,2],[4,5],[8,9]]
        # [2, 10]
        
        index = 0

        result = []
        nI = newInterval
        for i in range(len(intervals)):
            old = intervals[i]
            if nI[1] < old[0]:
                result.append(nI)
                for j in range(i, len(intervals)):
                    result.append(intervals[j])
                return result
            elif nI[0] > old[1]:
                result.append(old)
            else:
                nI[0], nI[1] = min(old[0], nI[0]), max(nI[1], old[1])
            
        result.append(nI)
        return result
            
                