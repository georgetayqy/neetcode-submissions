class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = -float("inf")
        current = 0

        for num in nums:
            current += num
            max_value = max(max_value, current)

            if current < 0:
                current = 0

        return max_value
                