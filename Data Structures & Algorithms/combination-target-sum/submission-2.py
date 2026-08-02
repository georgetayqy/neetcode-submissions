class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current = []

        # pick the current number and reuse it, or skip to the next
        def dfs(iterator, sum):
            nonlocal current
            
            if sum > target or iterator >= len(nums):
                # no way to sum to the target
                return
            elif sum == target:
                results.append(current.copy())
                return
            
            # use the current number
            current.append(nums[iterator])
            dfs(iterator, sum + nums[iterator])

            # don't use the current number
            current.pop()
            dfs(iterator + 1, sum)
            
        dfs(0, 0)
        return results