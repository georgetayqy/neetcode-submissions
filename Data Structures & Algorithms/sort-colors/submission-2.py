class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, middle, right = 0, 0, len(nums) - 1

        while middle <= right:
            # for any nums[middle] < 2, we MUST check the nums[middle] after the swap
            # since the swapped in value may not be part of the 1 partition
            match nums[middle]:
                case 0:
                    # if middle is 0, then we need to swap
                    # with the left, 0 belongs in left
                    nums[left], nums[middle] = nums[middle], nums[left]
                    
                    # increment left and middle since we have established order
                    # 0 < 1
                    left += 1
                    middle += 1
                case 1:
                    # if middle is 1, then we are in the correct position
                    middle += 1
                case 2:
                    # if middle is 2, then we swap with the right partition
                    nums[right], nums[middle] = nums[middle], nums[right]
                    right -= 1
