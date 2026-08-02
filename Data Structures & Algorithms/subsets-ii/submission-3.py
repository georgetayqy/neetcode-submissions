class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        def recurse(shared, idx):
            if idx >= len(nums):
                results.append(shared.copy())
                return
            
            shared.append(nums[idx])
            recurse(shared, idx + 1)

            shared.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            recurse(shared, idx + 1)
        
        recurse([], 0)
        return results