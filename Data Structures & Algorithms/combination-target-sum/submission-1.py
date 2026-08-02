class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i, sum):
            if sum == target:
                results.append(subset.copy())
                return
            
            if i >= len(nums) or sum > target:
                return
            
            # include this current number
            subset.append(nums[i])
            dfs(i, sum + nums[i])

            # dont stick to this number, move to the next number
            subset.pop()
            dfs(i + 1, sum)
        
        dfs(0, 0)

        return results
