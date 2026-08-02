class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_chars = ""

        for i in range(len(s)):
            # check odd length palindromes
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_chars = s[l:r + 1]
                    max_len = r - l + 1
                
                l -= 1
                r += 1
            
            # check even lengths
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_chars = s[l:r + 1]
                    max_len = r - l + 1
                
                l -= 1
                r += 1

        return max_chars
