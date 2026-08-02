import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for num in nums:
            # find the index to insert the current item into
            idx = bisect.bisect_left(dp, num)

            # if it can be inserted into the dp array at the edge
            # that means that we have found something that goes into
            # the array in sorted order (means that we can add it and
            # the sequence is still increasing)
            if idx == len(dp):
                dp.append(num)
            else:
                # if not, we add it into the array at the correct index
                # and keep going
                # replacing the item that is way too large with
                # our current item
                dp[idx] = num
        
        return len(dp)
