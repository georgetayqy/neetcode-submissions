class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            mid_elem = nums[mid]

            if mid_elem < nums[right]:
                # the ans must be on the left
                right = mid
            else:
                left = mid + 1

            # [4, 5, 0, 1, 2, 3]
            #     ^
            #        l
            #        r


        return nums[left]