import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pows(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                return pows(x, math.floor(n / 2)) * \
                       pows(x, math.ceil(n / 2))
        
        ans = pows(x, n if n >= 0 else -n)

        return ans if n >= 0 else 1 / ans
    