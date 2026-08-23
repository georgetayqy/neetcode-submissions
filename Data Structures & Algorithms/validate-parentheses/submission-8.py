class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if not stack:
                stack.append(char)
            elif char not in brackets:
                stack.append(char)
            elif brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack
