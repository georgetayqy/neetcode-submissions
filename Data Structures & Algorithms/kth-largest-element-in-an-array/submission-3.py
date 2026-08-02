import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest = n - kth smallest element
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)

            while len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)