class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1 for i in range(len(nums))]
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] *= nums[i - 1] * prefix[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            postfix[j] *= nums[j + 1] * postfix[j + 1]
        
        for k in range(len(nums)):
            results[k] = prefix[k] * postfix[k]

        return results
