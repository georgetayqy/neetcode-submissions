class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict
        # target: index

        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return sorted((i, seen[difference]))
            
            seen[nums[i]] = i
        
        