class Solution:
    def __init__(self):
        self.is_empty_string: bool = False

    def encode(self, strs: List[str]) -> str:
        if not strs:
            self.is_empty_string = True

        return "💀".join(strs)

    def decode(self, s: str) -> List[str]:
        if self.is_empty_string:
            return []

        return s.split("💀")