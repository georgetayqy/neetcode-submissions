class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                operation = operands[token]
                prev1, prev2 = stack.pop(), stack.pop()
                stack.append(operation(prev2, prev1))                
        
        return stack[-1]
