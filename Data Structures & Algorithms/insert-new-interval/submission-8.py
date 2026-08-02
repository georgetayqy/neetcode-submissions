import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []

        for i in range(len(intervals)):
            # if there are no right-border overlaps, 
            # then just append our new interval, no overlaps at all
            # and return it lol
            #                   [     ]
            # new:      [    ]
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                return results + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                #        [    ]
                # new:          [     ]
                # just add the current iterated intervals
                # first, then keep going
                # can't add new in anyways as it is out of order
                results.append(intervals[i])
            elif intervals[i][0] <= newInterval[0] <= intervals[i][1] or \
                    intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                # if there are some overlaps:
                # update newInterval with the correct min/max value
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

            # not so fast!
            # there are 2 exit conditions
            # 1. if the right new bound never overlap with old left bound
            #    then it must mean that there should be no possible overlaps
            #    from there on, so insert new interval and concat results
            # 2. if there are some possible overlaps or if there are actual
            #    overlaps, then we either append the current iterated item
            #    or update the new interval with the min/max but don't append
            #    anything
            # in case 2, we didn't append to the result, so we must add back the
            # new interval to the results
        
        results.append(newInterval)
        return results


                