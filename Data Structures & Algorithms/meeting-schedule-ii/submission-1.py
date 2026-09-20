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

            if minEnd and minEnd[0] <= nxt.start:
                rooms -= 1
                heapq.heappop(minEnd)

            if curr.end > nxt.start:
                heapq.heappush(minEnd, curr.end)
                rooms += 1
                curr = nxt
            else:
                curr = nxt
        return rooms



