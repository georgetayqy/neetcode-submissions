class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We can cache the key (index_in_prices, True if buy else False if sell)

        # Memoization
        # key is (index, True/False), value is the max value
        dp = {}

        def dfs(i, buySell):
            # if we have an empty array, then profit is 0
            if i >= len(prices):
                return 0
            
            if (i, buySell) in dp:
                # if it is in the dp, we assume already computed
                return dp[(i, buySell)]
            
            if buySell:
                # if we are buying
                # we can buy or cooldown
                # we need to invert the buy state, and subtract from the total
                # since we BOUGHT
                buy = dfs(i + 1, not buySell) - prices[i]
                cool = dfs(i + 1, buySell)
                dp[(i, buySell)] = max(buy, cool)  # cache result
                
            else:
                # if we are selling
                # we increment by 2 since we need to take a cooldown after it
                sell = dfs(i + 2, not buySell) + prices[i]

                # we can still cooldown here
                cool = dfs(i + 1, buySell)
                dp[(i, buySell)] = max(sell, cool)

            # return the current max value
            return dp[(i, buySell)]

        # call with 0 and True
        dfs(0, True)
        return dp[(0, True)]

