class Solution:
    def reverseBits(self, n: int) -> int:
        results = 0

        for i in range(32):
            last_bit = (n >> i) & 1
            results = results | (last_bit << (31 - i))
        
        return results