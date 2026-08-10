from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)

        for key, count in counter.items():
            frequency[count].append(key)
        
        results = []
        for idx in range(len(frequency) - 1, -1, -1):
            for key in frequency[idx]:
                if len(results) == k:
                    return results
                
                results.append(key)

        return results
