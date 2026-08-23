class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                continue
            
            # now, keep swapping until we put the right number into this index
            while (nums[idx] != idx + 1 and 1 <= nums[idx] <= len(nums)):
                # to_swap index is always -1 of the value, since arrays are 0 indexed
                swap_index = nums[idx] - 1
                current, to_swap = nums[idx], nums[swap_index]

                if current == to_swap:
                    break
                else:
                    nums[idx], nums[swap_index] = nums[swap_index], nums[idx]
            
        for idx, num in enumerate(nums):
            if num != idx + 1:
                return idx + 1
        
        return len(nums) + 1
