class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []

        accumulation = 1
        for num in nums:
            left_product.append(accumulation)
            accumulation *= num

        accumulation = 1
        for i in range(len(nums) - 1, -1, -1):
            right_product.append(accumulation)
            accumulation *= nums[i]

        result = []
        for i in range(len(nums)):
            result.append(
                left_product[i] * right_product[len(nums) - i - 1]
            )
        
        return result
