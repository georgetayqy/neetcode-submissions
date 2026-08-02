class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # we set left == right here as we can only consider the middle explored
            # when left crosses right
            # e.g [1] => l = 0, r = 0, t = 2 [not explored yet] ==> l += 1, r = 0 [EXPLORED]
            # overflow-safe
            mid = left + (right - left) // 2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            elif mid_num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
