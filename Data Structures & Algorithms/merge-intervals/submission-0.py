class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])

        # before
        # after
        # overlap
        result = []
        curr = []
        for i in range(len(intervals)-1):
            curr = intervals[i]
            nxt = intervals[i+1]
            if curr[1] < nxt[0]:
                print(True)
                for j in range(i, len(intervals)):
                    result.append(intervals[j])
                return result
            elif curr[0] > nxt[1]:
                result.append(nxt)
            else:
                curr[0], curr[1] = min(curr[0], nxt[0]), max(curr[1], nxt[1])
            
        result.append(curr)
        return result