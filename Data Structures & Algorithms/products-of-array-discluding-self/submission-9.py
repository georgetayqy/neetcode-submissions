class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        right_product = []

        accumulation = 1
        for num in nums:
            results.append(accumulation)
            accumulation *= num

        accumulation = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= accumulation
            accumulation *= nums[i]
        
        return results
