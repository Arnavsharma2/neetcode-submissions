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
            return []
        intervals.sort(key= lambda i: i.start)

        rooms = 1
        curr = intervals[0]
        for i in range(len(intervals)-1):
            nxt = intervals[i + 1]

            if curr.end > nxt.start:
                rooms += 1
                curr = nxt
            else:
                curr = nxt
        return rooms



