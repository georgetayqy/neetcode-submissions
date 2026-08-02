class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = nums[0]

        for i in range(1, len(nums)):
            value ^= nums[i]
        
        return value
