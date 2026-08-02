class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0

        while n > 0:
            if n & 1:
                num_ones += 1

            n >>= 1

        return num_ones
