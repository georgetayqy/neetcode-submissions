class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deltas = {}

        for i in range(len(nums)):
            num = nums[i]
            delta = target - num
            
            if delta in deltas:
                return [deltas[delta], i]
            
            # update the index in the hash map
            deltas[num] = i
