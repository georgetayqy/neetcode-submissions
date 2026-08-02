class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(parenthesis, _open, close):
            if _open < 0 or close < 0:
                return

            if _open == close and _open == 0:
                results.append(parenthesis)
                return
            elif _open > close:
                return
            
            dfs(parenthesis + "(", _open - 1, close)
            dfs(parenthesis + ")", _open, close - 1)
        
        dfs("", n, n)

        return results