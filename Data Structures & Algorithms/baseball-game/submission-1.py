class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            try:
                stack.append(int(operation))
            except ValueError:
                if operation == "+":
                    right, left = stack[-1], stack[-2]
                    stack.append(
                        left + right
                    )
                elif operation == "C":
                    stack.pop()
                elif operation == "D":
                    stack.append(
                        stack[-1] * 2
                    )
        
        return sum(stack)
