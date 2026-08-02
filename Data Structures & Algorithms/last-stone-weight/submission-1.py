import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            first, second = - heapq.heappop(heap), - heapq.heappop(heap)

            if first == second:
                continue
            
            if first < second:
                second -= first
                heapq.heappush(heap, -second)
            else:
                first -= second
                heapq.heappush(heap, -first)
        
        return -heapq.heappop(heap) if heap else 0
