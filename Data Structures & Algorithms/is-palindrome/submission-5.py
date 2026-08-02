import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        alphanumerics = string.ascii_letters + string.digits

        while left < right:
            while left < len(s) and s[left] not in alphanumerics:
                left += 1
            
            while right >= 0 and s[right] not in alphanumerics:
                right -= 1
            
            if left >= len(s) or right < 0:
                # all are invalid chars, so string must be empty
                return True

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
