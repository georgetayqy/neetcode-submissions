class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        # we can think of it as shifting the prefix sum forward by 1, and replacing
        # the first element as 1
        # [1, 2, 3, 4] => [1, 1, 2, 3] (effectively) => [1, 1, 2, 6]
        # we can skip the first element here
        for i in range(1, len(nums)):
            output.append(output[i - 1] * nums[i - 1])

        # shifting the postfix sum backwards by 1
        # [1, 2, 3, 4] => [2, 3, 4, 1] => [24, 12, 4, 1]
        # we need to save the postfix value to carry over the computations
        # across the 2nd pass of the output
        # we can skip the first element here
        postfix = 1
        for j in range(len(nums) - 1, 0, -1):
            # see below for the reason of modifying the previous item for the
            # postfix array iteration
            postfix *= nums[j]
            output[j - 1] *= postfix
        # for j in range(len(nums) - 1, -1, -1):
            # if we swap these 2 operations, then it must go all the way to the end
            # output[j] *= postfix
            # postfix *= nums[j]

        # [1, 2, 3, 4]
        # pre: [1, 1, 2, 6]
        # pre-unshifted: [1, 2, 6, 24]
        # post:[24, 12, 4, 1]
        # post-unshifted: [24, 24, 12, 4]
        # each position: [pre[i - 1] * post[i + 1]]
        # if we shift the pre forward by 1 and the post backwards by 1,
        # we get the new position function: [pre[i] * post[i]]

        return output
