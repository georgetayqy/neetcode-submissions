class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        # skip the first element
        for i in range(1, len(nums)):
            output.append(
                output[i - 1] * nums[i - 1]
            )
        
        # constant space used
        nums.append(1)

        # skip the first element
        for i in range(len(nums) - 1, 1, -1):
            nums[i - 1] = nums[i - 1] * nums[i]
        
        # interleave, but skip the nums array's first element
        for i in range(len(output)):
            output[i] *= nums[i + 1]
        
        return output