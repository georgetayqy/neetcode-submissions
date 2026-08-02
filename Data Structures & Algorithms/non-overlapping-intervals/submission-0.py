class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        count = 0
        right_min = intervals[0][1]

        for i in range(1, len(intervals)):
            # if there are overlaps, we need to consider
            # which one ends first

            if intervals[i][0] >= right_min:
                # no overlap! = is considered non overlapping
                # max not needed here as we know that the right
                # interval should be larger than the left value
                right_min = max(intervals[i][1], right_min)
            else:
                # overlap!
                count += 1

                # no need to delete, just need to update the previous end
                # -> we keep the min of the end values
                right_min = min(right_min, intervals[i][1])

        return count