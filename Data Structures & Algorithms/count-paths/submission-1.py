from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(x, y):
            if x >= m or y >= n:
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1
            
            return dfs(x + 1, y) + dfs(x, y + 1)
        
        return dfs(0, 0)
        