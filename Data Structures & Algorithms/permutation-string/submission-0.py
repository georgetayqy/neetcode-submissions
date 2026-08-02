class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            # if longer, then its not possible to find a permutation
            return False
        
        # can just use an array here instead, no need to use an actual hashmap
        s1C, s2C = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}, {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}

        # initialise the first len(s1) chracters of s1 and s2 here to signify the
        # counts of characters in the current window OF LENGTH (S1) in s2
        # [abc] [abcdefgh] => [a=1, b=1, c=1] [a=1, b=1, c=1] here
        for i in range(len(s1)):
            s1C[s1[i]] += 1
            s2C[s2[i]] += 1
        
        matches = self.precompute_matches(s1C, s2C)
        
        # sliding window technique is used here
        left = 0

        # we can skip the right pointer to the index right after the end of
        # the s1 string (notice that s1 iteration above stops just before len(s1))
        for right in range(0 + len(s1), len(s2)):
            # we can put this outside before the for loop, but we could just
            # put this here so that it gets handled during the for loop itself
            if matches == 26:
                return True

            # this character is just added to the window
            current_char = s2[right]
            
            # now, we need to update the s2C map, since we added one character to the
            # s2 count map (which tracks the window sliding over string s2)
            s2C[current_char] += 1

            # now, we check:
            # if after addition the s2C count of current_char is now equal to that of
            # s1, we know that we have made another match!
            if s2C[current_char] == s1C[current_char]:
                # if we match, then we add 1 to the matches count
                matches += 1
            elif s1C[current_char] + 1 == s2C[current_char]:
                # if, they were previously equal, but after the addition of 1
                # to s2's count of current_char, they are no longer equal, then
                # we have to decrement the total number of matches

                # our inclusion of the current_char into the window has caused and
                # inequality of character counts instead
                # e.g. s1=abc, s2=abca {a=1, b=1, c=1} -> {a=2, b=1, c=1}
                # we can see that we created a mismatch in a previously matched map
                # to rectify, we need to decrement the matches by 1
                matches -= 1
        
            # this is the character on the left side of the window
            left_char = s2[left]
            
            # we need to remove this as we have slid the window across the left
            # character, so we need to remove 1 count it from the s2C map
            s2C[left_char] -= 1

            # symmetric cases as to above, if we create a match, we add 1 to matches
            if s2C[left_char] == s1C[left_char]:
                matches += 1
            elif s1C[left_char] - 1 == s2C[left_char]:
                # if after we remove the character, we have changed it from previously
                # matching to now not matching
                # s1C == s2C previously, if -1 from s2C, and s1C > s2C and differs by
                # exactly 1, then we know that we have broken a match and need to
                # decrement the matches by 1
                matches -= 1

            # now, we need to move our left forward since started with the correct
            # width of the window and have just shifted it one forward
            left += 1
        
        # possible that after changing the matches that we might end up such that
        # the final len(s1) window of s2 is actually the match
        # so we should check here if matches is equal to 26
        return matches == 26


    def precompute_matches(self, s1C, s2C):
        """Precomputes the number of matches between the two initial
        'hashmaps'"""
        matches = 0

        for i in range(ord("a"), ord("z") + 1):
            if s1C[chr(i)] == s2C[chr(i)]:
                matches += 1
        
        return matches