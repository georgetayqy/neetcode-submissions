class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.add((nums[i], nums[j], nums[k]))
        
        return list(map(list, results))
