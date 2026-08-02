class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map char count to the strings, we use a defaultdict here to
        # avoid having to handle adding a list to the dict
        hashed = defaultdict(list)
        a_ord = ord('a')

        for s in strs:
            count = [0 for i in range(26)]

            for char in s:
                # use the ascii number to bound i to 0 to 25
                count[ord(char) - a_ord] += 1

            hashable_list = tuple(count)
            hashed[hashable_list].append(s)
        
        # no need to do list comprehension, hashed.values() will return
        # a list of the list nicely
        return hashed.values()
