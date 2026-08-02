from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)

        min_size = float("inf")

        left = 0
        right = 0
        idxes = []

        while right < len(s):
            print("Looking at right:", right)
            current_character = s[right]
            right += 1

            if current_character in t_count:
                print("\tDecrementing character")
                t_count[current_character] -= 1
            
            while self.is_valid(t_count) and left < right:
                print("\tCounter Before Window Shrink:", t_count)
                curr_win_size = right - left

                if curr_win_size < min_size:
                    print("\t\tSmaller Window Size at:", (left, right))
                    min_size = curr_win_size
                    idxes = [left, right]
                
                if s[left] in t_count:
                    print(f"\tAdding back {s[left]}")
                    t_count[s[left]] += 1
                
                left += 1
                print("\tCounter After Window Shrink:", t_count)
                print("\tIndex after Window Shrink", (left, right))
        
        if len(idxes) == 0:
            return ""
        
        return s[idxes[0]:idxes[1]]
    
    def is_valid(self, d):
        for key in d:
            if d[key] > 0:
                return False
        
        return True