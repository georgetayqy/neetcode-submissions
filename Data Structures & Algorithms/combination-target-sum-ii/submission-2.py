class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort to determine stopping conditions easier
        candidates.sort()

        results = []
        combi = []

        def dfs(i, sum):
            if sum == target:
                results.append(combi.copy())
                return

            if i >= len(candidates) or sum > target:
                return
        
            combi.append(candidates[i])
            dfs(i + 1, sum + candidates[i])

            combi.pop()
            i_new = i

            while i_new < len(candidates) and candidates[i_new] == candidates[i]:
                i_new += 1

            dfs(i_new, sum)
        
        dfs(0, 0)

        return results