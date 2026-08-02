from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def robber(idx):
            if idx >= len(nums):
                return 0
            
            return max(
                nums[idx] + robber(idx + 2),
                robber(idx + 1)
            )
        
        return max(
            robber(0),
            robber(1)
        )
