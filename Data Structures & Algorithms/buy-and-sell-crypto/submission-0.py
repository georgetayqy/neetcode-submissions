class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        previous_min = -1
        max_profit = 0
        
        for price in prices:
            if not stack:
                previous_min = price
                stack.append(price)
            else:
                if price > stack[-1]:
                    max_profit = max(max_profit, price - previous_min)
                else:
                    stack = [price]
                    previous_min = price
        
        return max_profit