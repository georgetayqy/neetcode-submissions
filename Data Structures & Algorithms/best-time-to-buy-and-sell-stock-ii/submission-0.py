class Solution:
    # recursive solution
    # def yes(day, profit, hasStock):
    #     if day >= len(prices):
    #         return profit
    #     if hasStock:
    #         # sell or hold, can sell then buy
    #         return max(
    #             yes(day, profit + prices[day], not hasStock),
    #             yes(day + 1, profit, hasStock)
    #         )
    #     else:
    #         # if no stock, can either hold or buy
    #         return max(
    #             yes(day + 1, profit, hasStock),
    #             yes(day + 1, profit - prices[day], not hasStock)
    #         )
        
    def maxProfit(self, prices: List[int]) -> int:
        # (profit by holding, profit by not holding)
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            # if i am holding today, that means that a buy or hold
            # has happened
            dp[i][0] = max(
                dp[i - 1][1] - prices[i],
                dp[i - 1][0]
            )

            # if i am not holding today, means that i must have
            # either not be holding yesterday or a sell happened
            dp[i][1] = max(
                dp[i - 1][1],
                dp[i - 1][0] + prices[i]
            )
        
        return max(dp[-1])

