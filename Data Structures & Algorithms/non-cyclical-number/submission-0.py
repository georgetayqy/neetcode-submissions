class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            new_number = 0

            while n > 0:
                new_number += ((n % 10) ** 2)
                n //= 10

            if new_number in seen:
                return False
            
            seen.add(new_number)
            n = new_number
        
        return True
