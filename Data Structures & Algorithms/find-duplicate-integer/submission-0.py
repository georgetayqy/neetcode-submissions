class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            else:
                # we swap until we end up swapping two numbers which are the same
                # guaranteed to find the correct position or find a dupe
                while nums[i] != i + 1:
                    idx_to_swap = nums[i] - 1

                    if nums[idx_to_swap] == nums[i]:
                        return nums[idx_to_swap]
                    
                    nums[i], nums[idx_to_swap] = nums[idx_to_swap], nums[i]
