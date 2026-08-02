class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the dp table
        dp = [float("inf") for i in range(amount + 1)]

        # base case, since no amount means no coins
        dp[0] = 0
        
        # iterate through the [1, amount] range
        for i in range(1, amount + 1):
            # looks like brute force honestly
            for coin in coins:
                # if we can evenly exchange the amount of money we have with the coins
                # or have any leftovers from the exchange
                if i - coin >= 0:
                    # check the min between our current value and the
                    # dp[i - coin] amount (meaning we have exchanged our $ for this coin)
                    # + 1 (since we have exchanged for 1 additional coin)

                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # do one final check
        return dp[-1] if dp[-1] != float("inf") else -1
