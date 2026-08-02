class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        dfs = []
        parenthesis = []

        dfs.append((n, n))

        def backtrack(open, close):
            if open < 0 or close < 0 or open > close:
                return
            elif open == close and open == 0:
                results.append("".join(parenthesis))
                return
            
            if open - 1 <= close:
                parenthesis.append("(")
                backtrack(open - 1, close)
                parenthesis.pop()
            
            if open <= close - 1:
                parenthesis.append(")")
                backtrack(open, close - 1)
                parenthesis.pop()

        backtrack(n, n)
        return results