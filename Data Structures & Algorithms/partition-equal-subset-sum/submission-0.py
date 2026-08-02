class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            # cannot partition odd numbers
            return False
        
        target = totalSum // 2

        def recurse(index, sums):
            if sums == target:
                return True
            elif index == len(nums):
                return sums == target
            
            return recurse(index + 1, sums + nums[index]) or recurse(index + 1, sums)
        
        return recurse(0, 0)
