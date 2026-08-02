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
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # using the max freq here instead
            max_freq = max(max_freq, count[s[right]])
            
            # right - left + 1 is window length
            # len - max_count is the number of replacements
            # we need to make so that everyone has the same character
            # NOTICE WE REPLACE MAX_FREQ FINDING WITH THE NEW STATIC
            # MAX_FREQ COUNTER HERE
            # > allowed to do that as we only trigger a window resize
            # when the max freq changes
            while (right - left + 1) - max_freq > k:
                # need to shrink the window
                # still not decrementing max f, wont affect results
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
