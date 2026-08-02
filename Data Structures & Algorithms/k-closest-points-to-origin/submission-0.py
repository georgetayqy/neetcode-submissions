import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a heap
        heap = []

        for point in points:
            # we want it to be a maxheap
            heapq.heappush(heap, (-self.euclid(point), point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point[1] for point in heap]

    
    def euclid(self, point):
        return sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)