class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_len = len(s)
        max_window = 0
        
        left = 0
        max_frequency = 0
        counts = {}

        for right in range(s_len):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            max_frequency = max(max_frequency, counts[s[right]])

            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
            
            max_window = max(max_window, right - left + 1)
        
        return max_window
