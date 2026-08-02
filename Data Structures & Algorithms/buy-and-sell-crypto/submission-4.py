class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane algo
        max_price = -101
        current_price = prices[0]

        for price in prices:
            current_price = min(current_price, price)
            max_price = max(max_price, price - current_price)
        
        return max_price
