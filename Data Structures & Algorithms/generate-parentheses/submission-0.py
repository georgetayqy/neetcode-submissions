class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open, close):
            if open == close == n:
                # stack has the correct parenthesis
                result.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                # stack is being reused, so once we recurse by adding
                # an item to the stack, we need to remove it
                stack.pop()
            
            # we can only add closing parenthesis if close is < open count
            # if close is more, then we already have something invalid
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result
