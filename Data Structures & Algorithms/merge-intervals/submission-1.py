class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key= lambda i: i[0])

        # before
        # after
        # overlap
        result = []
        curr = intervals[0]
        for i in range(len(intervals)-1):
            nxt = intervals[i+1]
            if curr[1] < nxt[0]:
                result.append(curr)
                curr = nxt
            else:
                curr[0], curr[1] = min(curr[0], nxt[0]), max(curr[1], nxt[1])
            
        result.append(curr)
        return result