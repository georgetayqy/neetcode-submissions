from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)

        min_size = float("inf")

        left = 0
        right = 0
        idxes = []

        while right < len(s):
            current_character = s[right]
            right += 1

            if current_character in t_count:
                t_count[current_character] -= 1
            
            while self.is_valid(t_count) and left < right:
                curr_win_size = right - left

                if curr_win_size < min_size:
                    min_size = curr_win_size
                    idxes = [left, right]
                
                if s[left] in t_count:
                    t_count[s[left]] += 1
                
                left += 1
        
        if len(idxes) == 0:
            return ""
        
        return s[idxes[0]:idxes[1]]
    
    def is_valid(self, d):
        for key in d:
            if d[key] > 0:
                return False
        
        return True