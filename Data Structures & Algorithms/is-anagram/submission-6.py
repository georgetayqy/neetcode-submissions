from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s, char_t = defaultdict(int), defaultdict(int)
        for char in s:
            char_s[char] += 1
        for char in t:
            char_t[char] += 1
        
        return char_s == char_t
