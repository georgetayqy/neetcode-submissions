class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        left, right = nums[:-1], nums[1:]

        return max(
            self.rob_once(left),
            self.rob_once(right)
        )
    
    def rob_once(self, arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(
                dp[i - 1],
                arr[i] + dp[i - 2]
            )

        return dp[-1]