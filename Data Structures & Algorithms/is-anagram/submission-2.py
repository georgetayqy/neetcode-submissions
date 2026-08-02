class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = [0 for i in range(26)]
        t_dict = [0 for i in range(26)]

        for char in s:
            s_dict[ord(char) % 26] += 1
        
        for char in t:
            t_dict[ord(char) % 26] += 1

        return s_dict == t_dict