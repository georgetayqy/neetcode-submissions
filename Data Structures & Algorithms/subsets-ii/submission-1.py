class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # subsets that start with the same number is skipped
        nums.sort()

        results = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                results.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            next_i = i
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1

            subset.pop()
            dfs(next_i)

        dfs(0)

        return results




