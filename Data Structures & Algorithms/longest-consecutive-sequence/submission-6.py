class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        longest_length, current_length = 0, 0
        for num in nums:
            if num - 1 not in unique_nums:
                iterator = num

                while iterator in unique_nums:
                    current_length += 1
                    unique_nums.remove(iterator)
                    iterator += 1
                
                longest_length = max(longest_length, current_length)
                current_length = 0
        
        return longest_length
