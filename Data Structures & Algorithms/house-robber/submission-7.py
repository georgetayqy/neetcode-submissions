class Solution:
    def rob(self, nums: List[int]) -> int:
        # left: lags 2 positions behind, right lags 1
        # we only need the previous 2 maxes to compute
        # the next max
        left, right = 0, 0

        for num in nums:
            # current max for this subarrary
            # terminating at num is
            # max between one pos lagging
            # and two pos lagging + num value
            temp = max(
                right, num + left
            )
            right, left = temp, right
        
        return right
