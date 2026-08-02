import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify the nums
        heapq.heapify(nums)
        
        # k largest = n - k smallest
        for i in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)