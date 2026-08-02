class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        funcs = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        stack = []

        for token in tokens:
            if token not in funcs:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                stack.append(funcs[token](left, right))
        
        return stack.pop()