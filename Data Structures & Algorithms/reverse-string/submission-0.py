class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s) // 2):
            left, right = i, len(s) - i - 1
            s[left], s[right] = s[right], s[left]
