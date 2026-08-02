from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.length = len(cost)
        self.cost = cost

        return min(
            self.lowCost(0),
            self.lowCost(1)
        )
        
    
    def lowCost(self, start) -> int:
        @lru_cache
        def dfs(index):
            if index >= self.length:
                return 0
            
            return min(
                dfs(index + 1) + self.cost[index],
                dfs(index + 2) + self.cost[index]
            )
        
        return dfs(start)
