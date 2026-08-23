from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefix_sum = 0
        count = 0
        prefixes[0] = 1

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefixes:
                count += prefixes[prefix_sum - k]
            
            prefixes[prefix_sum] += 1

        return count
