from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        t_count = {}
        s_count = {}

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        want, have = len(t_count), 0
        min_size = float("inf")

        left = 0
        right = 0
        idxes = []

        while right < len(s):
            current_character = s[right]
            right += 1

            s_count[current_character] = s_count.get(current_character, 0) + 1

            if current_character in t_count and s_count[current_character] == t_count[current_character]:
                have += 1

            while have == want:
                current_win_size = right - left

                if current_win_size < min_size:
                    min_size = current_win_size
                    idxes = [left, right]
                
                s_count[s[left]] -= 1

                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    have -= 1
                
                left += 1
        
        if len(idxes) == 0:
            return ""
        
        return s[idxes[0]:idxes[1]]