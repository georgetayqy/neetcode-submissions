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
            if not stack or char not in close_to_open:
                stack.append(char)
            else:
                # must have something in the stack by now
                peek = stack.pop()

                if close_to_open[char] != peek:
                    return False                

        return not bool(stack)
