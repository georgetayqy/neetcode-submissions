class Solution:
    def __init__(self):
        self.delimiter = "💀"
        self.is_empty_input = False

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            self.is_empty_input = True

        return self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        if self.is_empty_input:
            return []
        
        return [""] if len(s) == 0 else s.split(self.delimiter)
