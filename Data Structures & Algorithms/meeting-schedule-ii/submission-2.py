"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([s.start for s in intervals])
        ends = sorted([e.end for e in intervals])

        start, end = 0, 0
        count, result = 0, 0
        interval_len = len(intervals)

        # end < interval_len is not needed
        while start < interval_len and end < interval_len:
            if starts[start] < ends[end]:
                # we admit one concurrent meeting
                count += 1
                start += 1
            else:
                end += 1
                count -= 1
            
            result = max(result, count)
        
        return result
