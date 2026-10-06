class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        res = []
        for i in range(1, len(intervals)):
            curr = intervals[i-1]
            next = intervals[i]
            if next[0] > curr[1]:
                res.append(curr)
            elif curr[0] <= next[0] <= curr[1]:
                intervals[i] = [min(next[0], curr[0]), max(next[1], curr[1])]
        
        res.append(intervals[-1])
        return res

