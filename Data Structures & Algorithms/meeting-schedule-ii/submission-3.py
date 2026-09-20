"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda i: i.start)
        
        rooms = 1
        curr = intervals[0]
        minEnd = [curr.end]
        heapq.heapify(minEnd)
        for i in range(len(intervals)-1):
            nxt = intervals[i + 1]
            heapq.heappush(minEnd, nxt.end)

            if minEnd and minEnd[0] <= nxt.start:
                heapq.heappop(minEnd)
                curr = nxt
            elif curr.end > nxt.start:
                rooms += 1
                curr = nxt
            else:
                curr = nxt
            
        return rooms



