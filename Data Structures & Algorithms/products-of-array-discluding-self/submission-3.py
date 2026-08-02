class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_shift_right = [1] + nums
        right_shift_left = nums + [1]

        for i in range(len(nums)):
            left_shift_right[i + 1] = left_shift_right[i] * left_shift_right[i + 1]
        
        for i in range(len(nums) - 1, 0, -1):
            right_shift_left[i] = right_shift_left[i] * right_shift_left[i + 1]

        for i in range(len(left_shift_right) - 1):
            left_shift_right[i] = left_shift_right[i] * right_shift_left[i + 1]
        
        left_shift_right.pop()
        return left_shift_right
        