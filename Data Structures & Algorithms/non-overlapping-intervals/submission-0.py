class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return []
        intervals.sort(key=lambda i: i[0])

        deletes = 0
        curr = intervals[0]
        for i in range(len(intervals)-1):
            nxt = intervals[i + 1]

            if curr[1] > nxt[0]:
                deletes += 1
                if nxt[1] < curr[1]:
                    curr = nxt
            else:
                curr = nxt
        
        return deletes


            