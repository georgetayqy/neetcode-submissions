class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        
        if s[0] == "0":
            return 0

        prev, curr = 1, 1

        for i in range(1, len(s)):
            value = 0

            if 0 < int(s[i]) <= 9:
                # is valid
                value += curr
            
            if s[i - 1] != "0" and 1 <= int(s[i - 1:i + 1]) <= 26:
                if i - 2 < 0:
                    value += 1
                elif 0 <= i - 2 < len(s):
                    value += prev

            prev, curr = curr, value
        
        return curr

