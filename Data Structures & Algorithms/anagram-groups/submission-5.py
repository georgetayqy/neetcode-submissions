class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            counter = [0 for i in range(26)]

            for char in s:
                counter[ord(char) % 26] += 1

            anagrams[tuple(counter)].append(s)
            
        return anagrams.values()


