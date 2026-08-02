class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dp = [[0 for i in range(len(coins) + 1)] for j in range(amount + 1)]
        dp[0] = [1 for i in range(len(coins) + 1)]

        for a in range(1, amount + 1):
            for c in range(len(coins) - 1, -1, -1):
                new_amount = a - coins[c]
                new_coin = c + 1

                if new_amount >= 0:
                    dp[a][c] += dp[a - coins[c]][c]
                    dp[a][c] += dp[a][new_coin]

        return dp[amount][0]
