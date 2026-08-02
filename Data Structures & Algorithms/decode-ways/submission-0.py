class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        
        if s[0] == "0":
            return 0

        dp = [0 for i in range(len(s))]
        dp[0] = 1

        for i in range(1, len(s)):
            if 0 < int(s[i]) <= 9:
                # is valid
                dp[i] += dp[i - 1]
            
            if s[i - 1] != "0" and 1 <= int(s[i - 1:i + 1]) <= 26:
                if i - 2 < 0:
                    dp[i] += 1
                elif 0 <= i - 2 < len(s):
                    dp[i] += dp[i - 2]
        
        return dp[-1]

