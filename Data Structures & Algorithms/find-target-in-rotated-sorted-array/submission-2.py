class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            mid_number = nums[mid]

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # must be on the left portion of the array
                # if the target is greater than the middle number
                # or if the target is less than the left value (is on
                # the other side of the rotation)
                # then we should search right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # must be on the right portion of the array
                # if the target is smaller than the middle number
                # or if the target is greater than the right value (
                # is on the other side of the rotation)
                if target < nums[mid] or target > nums[right]:
                    right = mid
                else:
                    left = mid + 1
        
        return left if nums[left] == target else -1
