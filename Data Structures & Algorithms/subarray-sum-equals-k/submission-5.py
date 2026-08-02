from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        total_sum = 0

        for num in nums:
            total_sum += num
            diff_to_find = total_sum - k
            
            count += prefix[diff_to_find]
            prefix[total_sum] += 1

        return count
