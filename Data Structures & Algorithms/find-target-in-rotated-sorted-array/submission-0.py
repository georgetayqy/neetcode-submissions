class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        if target == nums[left]:
            return left
        elif target > nums[left] and target <= nums[-1]:
            # binary search on right side
            l, r = left, len(nums) - 1

            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            return -1 if nums[l] != target else l

        else:
            # binary search on the left
            l, r = 0, left

            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            return -1 if nums[l] != target else l

        return -1
