from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l >= len(text1) or r >= len(text2):
                return 0

            if text1[l] == text2[r]:
                return 1 + dfs(l + 1, r + 1)

            return max(
                dfs(l + 1, r),
                dfs(l, r + 1)
            )
        
        return dfs(0, 0)
