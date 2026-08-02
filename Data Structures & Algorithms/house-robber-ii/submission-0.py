class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        self.nums = nums

        return max(
            self.robOnce(nums[:len(nums) - 1]),
            self.robOnce(nums[1:])
        )

    
    def robOnce(self, inputs):
        dp = [0 for i in range(len(inputs) + 1)]

        dp[-3] = inputs[-2]
        dp[-2] = inputs[-1]

        for i in range(len(inputs) - 2, -1, -1):
            dp[i] = max(
                inputs[i] + dp[i + 2],
                dp[i + 1]
            )
        
        return dp[0]

