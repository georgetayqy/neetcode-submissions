class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    Solution.isPal(left, right - 1, s) or
                    Solution.isPal(left + 1, right, s)
                )
            
            left += 1
            right -= 1
        
        return True

    @staticmethod
    def isPal(left, right, string):
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
