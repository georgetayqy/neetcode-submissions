class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = [None for i in range(len(nums) * 2)]
        for idx, num in enumerate(nums):
            new_nums[idx] = new_nums[idx + len(nums)] = num
        
        return new_nums
