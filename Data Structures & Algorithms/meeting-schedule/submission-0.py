"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)

        curr = intervals[0]
        for i in range(len(intervals)-1):
            nxt = intervals[i+1]
            
            if curr.end > nxt.start:
                return False
            curr = nxt

        
        return True
            