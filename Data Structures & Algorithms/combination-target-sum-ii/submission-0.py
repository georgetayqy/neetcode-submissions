class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort to determine stopping conditions easier
        candidates.sort()

        results = []
        combi = []

        def dfs(i, sum):
            if i >= len(candidates):
                if sum == target:
                    results.append(combi.copy())
                return

            if sum > target:
                # dont even bother, too high already
                return
            
            if sum == target:
                results.append(combi.copy())
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