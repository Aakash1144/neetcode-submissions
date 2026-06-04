"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key= lambda x:x.start)
        left = 0
        right = 1
        while(right<len(sorted_intervals)):
            print("left ", sorted_intervals[left].start, sorted_intervals[left].end)
            print("right ", sorted_intervals[right].start, sorted_intervals[right].end)
            if(sorted_intervals[right].start<sorted_intervals[left].end):
                return False
            left += 1
            right += 1
        return True