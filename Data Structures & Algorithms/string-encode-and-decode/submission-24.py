class Solution:
    def encode(self, strs: List[str]) -> str:
        processed_strings = []
        
        for st in strs:
            processed_strings.append(f"#{len(st)}#{st}")
        
        return "".join(processed_strings)

    def decode(self, s: str) -> List[str]:
        ptr = 0
        all_words = []

        while ptr < len(s):
            if s[ptr] == "#":
                ptr += 1
                length_string = []

                while s[ptr] != "#":
                    length_string.append(s[ptr])
                    ptr += 1
                
                ptr += 1

                word = []
                for i in range(int("".join(length_string))):
                    word.append(s[ptr])
                    ptr += 1

                all_words.append("".join(word))
        
        return all_words
