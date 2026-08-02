class Solution:
    def countSubstrings(self, s: str) -> int:
        # we expand from the middle from each string
        results = 0

        for i in range(len(s)):
            # start with the odd length palindromes
            results += self.palindrome(s, i, i)
            results += self.palindrome(s, i, i + 1)
        
        return results

    def palindrome(self, s, left, right):
        result = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1

        return result
