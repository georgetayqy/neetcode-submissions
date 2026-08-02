class Solution:
    def char2idx(self, char: str) -> int:
        return ord(char) - ord("a")

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s, char_t = [0 for i in range(26)], [0 for i in range(26)]
        for char in s:
            char_s[self.char2idx(char)] += 1
        for char in t:
            char_t[self.char2idx(char)] += 1
        
        for i in range(26):
            if char_s[i] != char_t[i]:
                return False
        
        return True
