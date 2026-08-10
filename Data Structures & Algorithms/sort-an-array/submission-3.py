import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums

        self.partitionSort(0, len(nums) - 1)
        return nums
    
    def partitionSort(self, left, right):
        if left >= right:
            return
        
        # swap the pivoting number to the right
        pivot = random.randint(left, right)
        self.nums[pivot], self.nums[right] = self.nums[right], self.nums[pivot]
        
        boundary = left
        for idx in range(left, right):
            if self.nums[idx] < self.nums[right]:
                # if current number is smaller than pivot
                self.nums[boundary], self.nums[idx] = self.nums[idx], self.nums[boundary]
                boundary += 1
        
        # swap back
        self.nums[boundary], self.nums[right] = self.nums[right], self.nums[boundary]
    
        self.partitionSort(left, boundary - 1)
        self.partitionSort(boundary + 1, right)

