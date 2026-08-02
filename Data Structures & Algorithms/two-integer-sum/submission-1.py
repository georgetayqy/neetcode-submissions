class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_idx = {}

        for i in range(len(nums)):
            num = nums[i]
            delta = target - num

            if delta in diff_to_idx:
                return [diff_to_idx[delta], i]
            
            diff_to_idx[num] = i
