class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current = 0

        for num in nums:
            if current < 0:
                current = 0
    
            current += num
            max_value = max(max_value, current)
        
        return max_value
                