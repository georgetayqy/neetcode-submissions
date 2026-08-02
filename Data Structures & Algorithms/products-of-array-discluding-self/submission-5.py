class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        for i in range(len(nums)):
            left_products = nums[:i]
            right_products = nums[i + 1:]
            value = 1

            for item in left_products:
                value *= item
            
            for item in right_products:
                value *= item
        
            results.append(value)

        return results