class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer, reader = 0, 0

        while reader < len(nums) and writer < len(nums):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
            
            reader += 1
        
        return writer
            