class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        close_to_open = {
            value: key for key, value in open_to_close.items()
        }

        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            elif char in open_to_close:
                stack.append(char)
            elif char in close_to_open:
                # must have something in the stack by now
                peek = stack.pop()

                if close_to_open[char] != peek:
                    return False                

        return not bool(stack)
