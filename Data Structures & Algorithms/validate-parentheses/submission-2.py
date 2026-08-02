class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        if len(s) == 0:
            return True
        
        stack = []

        for char in s:
            if char not in closing:
                stack.append(char)
            else:
                # nothing to pop, so must be an error
                if len(stack) == 0:
                    return False
                
                if closing[char] == stack[-1]:
                    stack.pop()
                else:
                    # do not match
                    return False
        
        return len(stack) == 0


