class Solution:
    def rob(self, nums: List[int]) -> int:
        # handles the edge case where there is only 1 element in the list
        if len(nums) <= 2:
            return max(nums)

        return max(
            self.robOnce(nums[:len(nums) - 1]),
            self.robOnce(nums[1:])
        )

    
    def robOnce(self, inputs):
        # make sure to init the length of dp to be 1 more than the input length
        dp = [0 for i in range(len(inputs) + 1)]

        dp[-3] = inputs[-2]
        dp[-2] = inputs[-1]

        # we should start at the 2rd last house
        for i in range(len(inputs) - 2, -1, -1):
            # we set the current dp entry to be the max of:
            # 1. the current house + the max robbed from 2 houses away
            # 2. the max robbed from 1 house away
            # [curr, next, next-next, ...]
            # curr = max(next + rob(curr), next-next)
            dp[i] = max(
                inputs[i] + dp[i + 2],
                dp[i + 1]
            )
        
        # the first element contains the max amount that can be robbed
        return dp[0]

