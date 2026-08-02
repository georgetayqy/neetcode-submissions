class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        
        while True:
            value = nums[index]

            nums[index] = None
            if nums[value] is None:
                return value
            
            index = value
