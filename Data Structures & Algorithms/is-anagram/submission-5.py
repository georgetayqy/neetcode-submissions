
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = [0 for i in range(26)]
        t_array = [0 for i in range(26)]

        for char in s:
            s_array[ord(char) % 26] += 1

        for char in t:
            t_array[ord(char) % 26] += 1

        return s_array == t_array
