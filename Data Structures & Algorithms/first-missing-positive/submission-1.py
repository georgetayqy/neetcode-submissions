class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                continue

            if nums[idx] == idx + 1:
                continue
            
            while nums[idx] != idx + 1 and 1 <= nums[idx] <= len(nums):
                current_value = nums[idx]
                to_swap = nums[nums[idx] - 1]

                if current_value == to_swap:
                    break
                else:
                    swap_index = nums[idx] - 1
                    nums[idx], nums[swap_index] = nums[swap_index], nums[idx]
        
        for idx, num in enumerate(nums):
            if num != idx + 1:
                return idx + 1
        else:
            return len(nums) + 1