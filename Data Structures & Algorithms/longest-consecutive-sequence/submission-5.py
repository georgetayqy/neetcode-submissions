class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_value = 0
        
        # at least n^2 so might as well just sort
        nums.sort()

        counter = 0
        
        for i in range(len(nums)):
            previous = nums[i]
            inner_total = 1

            for j in range(i + 1, len(nums)):
                if nums[j] - previous == 1:
                    previous = nums[j]
                    inner_total += 1
            
            counter = max(counter, inner_total)

        return counter
            