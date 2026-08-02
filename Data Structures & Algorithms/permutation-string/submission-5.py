class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count, matches = self.precompute_matches(s1, s2)

        left = 0
        
        # offset by len(s1) as we want to start off at the next char
        # in the window
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            left_char = s2[left]
            right_char = s2[right]

            s2Count[right_char] = s2Count.get(right_char, 0) + 1
            if s1Count.get(right_char, 0) == s2Count[right_char]:
                matches += 1
            elif s1Count.get(right_char, 0) + 1 == s2Count[right_char]:
                matches -= 1
            
            s2Count[left_char] = s2Count.get(left_char, 1) - 1
            if s1Count.get(left_char, 0) == s2Count[left_char]:
                matches += 1
            elif s1Count.get(left_char, 1) - 1 == s2Count[left_char]:
                matches -= 1
            
            left += 1
        
        return matches == 26
            
        
    
    def precompute_matches(self, s1, s2) -> bool:
        s1Count, s2Count = {}, {}
        matches = 0
        
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        for i in range(26):
            character = chr(ord("a") + i)

            if s1Count.get(character, 0) == s2Count.get(character, 0):
                matches += 1
            
        return s1Count, s2Count, matches
    