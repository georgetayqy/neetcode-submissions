class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maxlen = 0

        for right in range(len(s)):
            right_char = s[right]

            if right_char in seen:
                # change the rightmost index of the occurence of this value
                left = max(seen[right_char] + 1, left)
            
            seen[right_char] = right
            maxlen = max(maxlen, right - left + 1)

        return maxlen
                
        