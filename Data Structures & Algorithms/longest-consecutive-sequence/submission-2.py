class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_set = 0

        for num in nums:
            if num - 1 not in num_set:
                # possible starting point
                set_count = 0

                while num in num_set:
                    set_count += 1
                    num += 1

                max_set = max(max_set, set_count)
        
        return max_set
