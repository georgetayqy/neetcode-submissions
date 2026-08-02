class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charf = {}
        results = 0
        left = 0
        max_f = 0
        
        for r in range(len(s)):
            charf[s[r]] = charf.get(s[r], 0) + 1
            max_f = max(max_f, charf[s[r]])

            while (r - left + 1) - max_f > k:
                charf[s[left]] -= 1
                left += 1
            
            results = max(results, r - left + 1)
        
        return results
