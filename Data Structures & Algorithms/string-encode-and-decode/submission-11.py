class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        chars = []

        for i in range(len(strs)):
            chars.append(str(len(strs[i])))
            chars.append("+")
            chars.append(strs[i])

        return "".join(chars)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        results = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "+":
                # still in an int
                j += 1

            # the int must be before from i -> j (exclusive)
            length = int(s[i:j])

            # if we start at j + 1, we need to count length times
            # to get entire string
            # left_bound = j + 1
            # right_bound = j + length + 1
            results.append(s[j + 1:j + 1 + length])

            # increment i to the next item, which is j + 1 + length
            # j is currently at +, we need to + 1 to skip to the next
            # char that is in word
            # then increment by length times to reach the end of the
            # word and land on the next word
            i = j + 1 + length

        return results

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
