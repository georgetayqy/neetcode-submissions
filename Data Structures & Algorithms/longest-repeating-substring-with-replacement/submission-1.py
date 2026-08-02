class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we can count the number of characters we need to replace
        # is given by the windowLength - most_frequent(substring)
        # so long as windowLength - most_frequent(substring) <= k,
        # we grow the window as it is the max

        # finding max in the dict takes O(26) time
        # but its still technically linear
        count = {}
        
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = count.get(max(count, key=count.get))

            # right - left + 1 is window length
            # len - max_count is the number of replacements
            # we need to make so that everyone has the same character
            while (right - left + 1) - max(count.values()) > k:
                # need to shrink the window
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
