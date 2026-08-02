from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(index):
            if index >= len(nums):
                return 0
            
            return max(
                dfs(index + 2) + nums[index],
                dfs(index + 1)
            )
        
        return dfs(0)
