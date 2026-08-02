class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        current = []
        
        def dfs(iterator):
            nonlocal current

            if iterator >= len(nums):
                results.append(current.copy())
                return
            
            # append current number and try
            current.append(nums[iterator])
            dfs(iterator + 1)

            # pop the current number and try
            current.pop()
            dfs(iterator + 1)

        dfs(0)  
        return results
