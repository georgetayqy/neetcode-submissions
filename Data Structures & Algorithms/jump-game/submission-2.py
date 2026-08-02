class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def go(index):
            print("exploring", index)
            if index >= len(nums):
                print("im done")
                return True

            if nums[index] == 0:
                print("not yet")
                return index >= len(nums) - 1

            for i in range(1, nums[index] + 1):
                print("keep going", i)
                result = go(index + i)

                if result:
                    return True
            
            return False
        
        return go(0)




        
            