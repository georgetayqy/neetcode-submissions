from math import ceil

class Solution:
    def can_consume_bananas(self, bananas, rate, max_hours):
        hours = 0

        for banana in bananas:
            hours += math.ceil(banana / rate)

        return hours <= max_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1

        # O(n)
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if self.can_consume_bananas(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
