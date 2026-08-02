from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect selects the smallest k, so convert k to n - k
        # to find the n - kth smallest element == kth largest element

        k = len(nums) - k

        def quickselect(left, right):
            pivot = self.partition(nums, left, right)

            # if the current pivot is smaller than the target, then we need to look
            # on the right
            if pivot < k:
                return quickselect(pivot + 1, right)
            # if the current pivot is greater than the target, then we need to look
            # on the left
            elif pivot > k:
                return quickselect(left, pivot - 1)
            else:
                # if we have found the correct pivot == k, then we return the pivot
                return nums[pivot]

        return quickselect(0, len(nums) - 1)

    
    def partition(self, nums, left, right):
        # p acts as the left pointer and the pivot to return
        random_pivot = randint(left, right)
        nums[right], nums[random_pivot], nums[random_pivot], nums[right]
        pivot, p = nums[right], left

        # i acts as the right pointer
        for i in range(left, right):
            if nums[i] <= pivot:
                # if less than pivot, swap with the left pointer
                nums[p], nums[i] = nums[i], nums[p]

                # increment the left pointer
                p += 1
        
        nums[p], nums[right] = nums[right], nums[p]
        return p
                