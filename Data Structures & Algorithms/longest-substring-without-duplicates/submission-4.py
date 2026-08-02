class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # make sure that our window/substring is unique values only
        # no dupes using set
        seen = set()
        result = 0
        left = 0
        
        # right pointer is constantly shifting
        for right in range(len(s)):
            # if it is in the window, we have to remove the left pointer
            # item from the set and increment it to find the point where
            # we managed to delete s[right] from the set
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # after we removed the dupes, we add back the current char
            seen.add(s[right])

            # update the max result
            # right index - left index gives the exclusive width of
            # the window, + 1 to get the inclusive width
            result = max(result, right - left + 1)

        return result
