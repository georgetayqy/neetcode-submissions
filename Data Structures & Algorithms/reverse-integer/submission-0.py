class Solution:
    def reverse(self, x: int) -> int:
        results = 0
        is_negative = True if x < 0 else False
        x = abs(x)

        while x:
            final_digit = x % 10
            x //= 10
            results *= 10
            results += final_digit

            if results > (2**31) - 1:
                return 0
        
        return results * (-1 if is_negative else 1)
