class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def go(index):
            if index >= len(nums):
                return True

            if nums[index] == 0:
                return index >= len(nums) - 1

            for i in range(1, nums[index] + 1):
                result = go(index + i)

                if result:
                    return True
            
            return False
        
        return go(0)




        
            