class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #                         [        ]
        #                [     ]
        #       [     ] <- if left here is <= top of stack's right
        #   [           ]  there are some overlaps, so we merge
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            left, right = intervals[i]

            if left <= results[-1][1]:
                results[-1][1] = max(results[-1][1], right)
            else:
                results.append(intervals[i])
        
        return results