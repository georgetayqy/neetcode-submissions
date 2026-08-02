import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        heap = []
        to_return = []

        for num in nums:
            counts[num] += 1
        
        counts = dict(counts)

        for item, frequency in counts.items():
            heapq.heappush(heap, (-frequency, item))
        
        for i in range(k):
            to_return.append(heapq.heappop(heap)[-1])
        
        return to_return

