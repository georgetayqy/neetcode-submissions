class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        result = []

        for i in range(len(intervals)):
            # we iterate through the intervals
            
            curr = intervals[i]

            """
            Non-overlapping intervals
            """

            # if new interval goes before the current interval,
            # we can just append the new intervals and then add
            # the rest of the list to it, cuz we know that there
            # is never going to be an overlap with the next few intervals
            if newInterval[1] < curr[0]:
                result.append(newInterval)
                return result + intervals[i:]

            # new interval goes after the interval, but we do not add
            # the new interval yet, as it is possible that it might
            # overlap with the next coming intervals
            elif newInterval[0] > curr[1]:
                result.append(curr)
            else:
                """
                Overlapping intervals
                """
                # if the newInterval is potentially overlapping with
                # the current interval iterated
                # if newInterval[1] >= curr[0] or newInterval[0] <= curr[1]
                # newInterval's right extends into the curr's interval
                # or if curr's right extends into the newInterval
                
                # key is to USE NEWINTERVAL TO STORE THE MERGED
                # INTERVALS WHICH ARE POTENTIALLY OVERLAPPING
                # MAKE SURE NOT TO ADD IT TO THE RESULT LIST YET
                newInterval = [
                    min(newInterval[0], curr[0]),
                    max(newInterval[1], curr[1])
                ]

        # the only condition which does not return here is when
        # the new interval does not overlap at all
        # if it does, it is possible that newInterval is never inserted
        # into the list at all

        # MAKE SURE TO APPEND IT TO THE END OF THE INTERVAL
        # IN THE EVENT THAT THE OVERLAP RESULTED IN THE COLLAPSE OF ALL
        # SUBSEQUENT INTERVALS OF THE LIST
        result.append(newInterval)

        return result

