from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, count in counter.items():
            if not heap:
                heap.append([count, key])
            else:
                heappush(heap, [count, key])

                if len(heap) > k:
                    heappop(heap)
        
        return [key for (count, key) in heap]
