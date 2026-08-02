from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = list(map(lambda x: (self.edist(x), x), points))
        heapq.heapify(points)

        return [heapq.heappop(points)[1] for i in range(k)]
    
    def edist(self, point):
        return sqrt(point[0] ** 2 + point[1] ** 2)
