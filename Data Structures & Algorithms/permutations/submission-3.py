class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        in_nums = [False for i in range(len(nums))]
        results = []
        
        def recurse(seen_nums, recursed):
            if all(seen_nums):
                results.append(recursed)
                return
            
            for i in range(len(seen_nums)):
                if not seen_nums[i]:
                    recursed_copy = recursed.copy() + [nums[i]]
                    seen_nums[i] = True
                    recurse(seen_nums, recursed_copy)
                    seen_nums[i] = False

            return recursed
        
        recurse([False for i in range(len(nums))], [])
        return results
