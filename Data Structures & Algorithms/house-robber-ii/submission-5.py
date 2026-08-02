from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.robOnce(
                nums[:-1]
            ),
            self.robOnce(
                nums[1:]
            )
        )
    
    def robOnce(self, nums: List[int]) -> int:
        @lru_cache
        def dfs(index):
            if index >= len(nums):
                return 0
            
            return max(
                dfs(index + 2) + nums[index],
                dfs(index + 1)
            )
        
        return dfs(0)
