class Solution:
    def __init__(self):
        self.delimiter = "#"
        self.is_empty_input = False

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            self.is_empty_input = True

        encoded_strings = []
        for s in strs:
            encoded_strings.append(str(len(s)) + self.delimiter + s)
        
        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        if self.is_empty_input:
            return []
        
        left_pointer = 0
        decoded = []

        while left_pointer < len(s):
            # keep going until we meet the delimiter
            right_pointer = left_pointer

            while s[right_pointer] != "#":
                right_pointer += 1
            
            # slice out the length numbers
            length = int(s[left_pointer:right_pointer])

            # reset the left and right pointers to
            # after the # and the end of the string
            left_pointer = right_pointer + 1
            right_pointer = left_pointer + length
            
            # get the encoded string
            decoded.append(s[left_pointer:right_pointer])

            # move the left pointer forward to the location of
            # the next string
            left_pointer = right_pointer

        return decoded
