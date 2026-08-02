class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            counter = [0 for i in range(26)]

            for char in s:
                counter[ord(char) % 26] += 1

            tup_counter = tuple(counter)
            anagram_item = anagrams.get(tup_counter, [])
            anagram_item.append(s)
            anagrams[tup_counter] = anagram_item

        return anagrams.values()


