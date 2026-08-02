class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        similar_strings = {}

        for s in strs:
            counts = [0 for i in range(26)]

            for char in s:
                counts[ord(char) % 26] += 1
            
            tup_counts = tuple(counts)
            
            similar_strings[tup_counts] = similar_strings.get(tup_counts, []) + [s]

        return similar_strings.values()
