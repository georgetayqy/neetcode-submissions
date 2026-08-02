class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[index][True] = 1 + dp[index - 1][False]
        # dp[index][False] = 1 + dp[index - 1][True]

        cache = {}

        def recurse(index, sum):
            if index >= len(nums):
                return 1 if sum == target else 0
            
            if (index, sum) in cache:
                return cache[(index, sum)]
            
            cache[(index, sum)] = recurse(
                    index + 1, sum + nums[index]
                ) + recurse(
                    index + 1, sum - nums[index]
                )
            return cache[(index, sum)]
        
        return recurse(0, 0)
