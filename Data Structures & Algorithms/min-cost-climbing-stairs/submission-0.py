class Solution:
    def __init__(self):
        self.dp = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(pos):
            if pos >= len(cost):
                # cannot reach
                return 0
            elif pos in self.dp:
                return self.dp[pos]
            else:
                self.dp[pos] = cost[pos] + min(
                    dp(pos + 1),
                    dp(pos + 2)
                )

                return self.dp[pos]
        
        print(self.dp)

        return min(dp(0), dp(1)) 