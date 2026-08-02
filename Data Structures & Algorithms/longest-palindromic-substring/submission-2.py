class Solution:
    def longestPalindrome(self, s: str) -> str:
        # naive is to just form the n^2 strings, then do a n check to make sure it is
        # palindromic

        result = ""
        result_length = 0

        for i in range(len(s)):
            # check odd length palindromes
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1
                
                left -= 1
                right += 1
            
            # now check even length palindromes, wlog use i + 1
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1
                
                left -= 1
                right += 1
        
        return result
        
