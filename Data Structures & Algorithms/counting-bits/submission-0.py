class Solution:
    def countBits(self, n: int) -> List[int]:
        return [
            x.bit_count() for x in range(0, n + 1)
        ]