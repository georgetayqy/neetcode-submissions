class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        current = []

        def dfs(current, start):
            results.append(current.copy())
            
            if len(current) == len(nums):    
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(current, i + 1)
                current.pop()
            
        dfs(current, 0)
        
        return results
