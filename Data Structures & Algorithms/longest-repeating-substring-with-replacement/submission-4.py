class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_f = 0
        left = 0
        results = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(max_f, count[s[right]])

            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            
            results = max(results, right - left + 1)

        return results
