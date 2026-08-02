class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sorted_strs = list(map(lambda x: "".join(sorted(x)), strs))

        for i in range(len(strs)):
            ss = sorted_strs[i]
            anagram_item = anagrams.get(ss, [])
            anagram_item.append(strs[i])
            anagrams[ss] = anagram_item

        return anagrams.values()
