class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        current = []
        candidates.sort()

        def dfs(iterator, sum):
            nonlocal current

            if sum == target:
                results.append(current.copy())
                return
            
            if sum > target or iterator >= len(candidates):
                return
            
            # append the current number and proceed
            current.append(candidates[iterator])
            dfs(iterator + 1, sum + candidates[iterator])

            # or don't append the current number and skip to the next unique number
            current.pop()

            while iterator + 1 < len(candidates) and candidates[iterator + 1] == candidates[iterator]:
                iterator += 1
            
            dfs(iterator + 1, sum)
        
        dfs(0, 0)
        return results
