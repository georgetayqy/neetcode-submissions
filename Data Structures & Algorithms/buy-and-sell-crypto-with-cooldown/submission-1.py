from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def recurse(idx, has_stock):
            if idx >= len(prices) - 1:
                return prices[idx] if has_stock else 0
            
            if has_stock:
                # choose to sell or hold
                return max(
                    prices[idx] + recurse(idx + 2, not has_stock),
                    recurse(idx + 1, has_stock)
                )
            else:
                print()
                return max(
                    -prices[idx] + recurse(idx + 1, not has_stock),
                    recurse(idx + 1, has_stock)
                )
        
        return recurse(0, False)
