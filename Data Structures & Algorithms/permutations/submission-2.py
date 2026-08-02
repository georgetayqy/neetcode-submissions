class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(numbers, visited):
            if len(numbers) == len(nums):
                results.append(numbers.copy())
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    numbers.append(nums[i])

                    dfs(numbers, visited)
                    
                    numbers.pop()
                    visited[i] = False
            
        dfs([], [False for i in range(len(nums))])

        return results


