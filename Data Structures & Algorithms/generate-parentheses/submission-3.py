class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        dfs = []

        dfs.append(("", n, n))

        while dfs:
            parenthesis, open, close = dfs.pop()

            if open < 0 or close < 0:
                continue
            
            if open == close and open == 0:
                results.append(parenthesis)
                continue
            elif open > close:
                continue
            
            dfs.append((parenthesis + "(", open - 1, close))
            dfs.append((parenthesis + ")", open, close - 1))

        return results