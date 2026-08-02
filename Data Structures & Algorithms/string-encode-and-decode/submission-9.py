class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        chars = []

        for i in range(len(strs)):
            for char in strs[i]:
                if char == "\\":
                    chars.append("\\")
                chars.append(char)

            chars.append("\\")
            chars.append("0")

        return "".join(chars)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        if len(s) == 0:
            return []

        split = s.split("\\0")

        if len(split) > 0:
            split = split[:-1]
        results = []

        for string in split:
            i = 0
            to_resolve = []

            while i < len(string):
                if string[i] == "\\":
                    to_resolve.append("\\")
                    i += 2
                else:
                    to_resolve.append(string[i])
                    i += 1
            results.append("".join(to_resolve))

        return results


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))