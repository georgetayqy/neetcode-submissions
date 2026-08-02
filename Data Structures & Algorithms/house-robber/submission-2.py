class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0 for i in range(len(nums))]
        dp[-2] = nums[-2]
        dp[-1] = nums[-1]
        
        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return dp[0]