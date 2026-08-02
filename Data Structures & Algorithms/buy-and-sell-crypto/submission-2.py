class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_total = 0

        for i in range(len(prices)):
            max_so_far = 0
            for j in range(i + 1, len(prices)):
                max_so_far = max(max_so_far, -prices[i] + prices[j])

            max_total = max(max_total, max_so_far)
        
        return max_total
