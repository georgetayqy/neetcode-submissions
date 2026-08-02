class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                print(stack)
                val1, val2 = stack.pop(), stack.pop()
                stack.append(ops[token](val2, val1))
                print(stack)

        return stack.pop()