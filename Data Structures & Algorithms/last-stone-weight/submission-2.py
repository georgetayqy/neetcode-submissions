import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue
            
            if x < y:
                heapq.heappush(stones, (x - y))
        
        return 0 if not stones else abs(stones[0])
