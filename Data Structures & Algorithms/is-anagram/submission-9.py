class Solution:
    def char2idx(self, char: str) -> int:
        return ord(char) - ord("a")

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
