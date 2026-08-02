class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for number, count in counts.items():
            buckets[count].append(number)
        
        topk = []

        for i in range(len(buckets) - 1, -1, -1):
            for buck in buckets[i]:
                if len(topk) == k:
                    return topk

                topk.append(buck)

        return topk