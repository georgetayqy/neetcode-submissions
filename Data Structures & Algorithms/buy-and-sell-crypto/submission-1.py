class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is the buying price,
        # right is the selling price
        left, right = 0, 1
        max_price = 0
        
        while right < len(prices):
            if prices[right] < prices[left]:
                # found a new low price
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                max_price = max(max_price, profit)
                right += 1

        return max_price
