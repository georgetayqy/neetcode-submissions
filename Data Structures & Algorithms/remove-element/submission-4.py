class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader, writer = len(nums), 0

        while writer < reader:
            # if writer is not equal to the value, we skip the replacement
            if nums[writer] != val:
                writer += 1
            else:
                # if writer is equal to value, then we decrement the reader
                reader -= 1
                nums[writer] = nums[reader]
        
        return writer
