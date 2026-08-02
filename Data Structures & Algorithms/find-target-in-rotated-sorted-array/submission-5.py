class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot point first
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] <= target <= nums[-1]:
            # search on the right
            return self.binary_search(left, len(nums) - 1, target, nums)
        else:
            # search on the left
            return self.binary_search(0, left, target, nums)
    
    def binary_search(self, left, right, target, nums):
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
            



