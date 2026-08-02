class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recurse(index, sum):
            if index >= len(nums):
                return 1 if sum == target else 0
            
            return recurse(
                index + 1, sum + nums[index]
            ) + recurse(
                index + 1, sum - nums[index]
            )
        
        return recurse(0, 0)
