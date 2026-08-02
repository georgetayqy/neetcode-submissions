class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1 for i in range(len(nums))]

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            results[i] *= prefix
            prefix *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            results[j] *= postfix
            postfix *= nums[j]
        
        return results
