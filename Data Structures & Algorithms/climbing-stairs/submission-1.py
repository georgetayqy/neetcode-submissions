from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(stair):
            if stair > n:
                return 0
            
            if stair == n:
                return 1
            
            return dfs(stair + 1) + dfs(stair + 2)
        
        return dfs(0)
