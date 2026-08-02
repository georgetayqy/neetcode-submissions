import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # just heapify the distances
        heap = [(self.euclid(point), point) for point in points]
        heapq.heapify(heap)

        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results

    
    def euclid(self, point):
        return sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)