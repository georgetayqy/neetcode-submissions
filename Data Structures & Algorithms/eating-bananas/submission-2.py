from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # fastest rate is simply just the max banana pile in the piles
        left, right = 1, max(piles)

        while left < right:
            middle = left + (right - left) // 2
    
            if self.canEatBananas(piles, middle, h):
                # lower down the right boundary
                right = middle
            else:
                # shift up the left boundary
                left = middle + 1
        
        return left + (right - left) // 2
    
    def canEatBananas(self, banana: List[int], rate: int, maxH: int) -> bool:
        total_hours = 0

        for b in banana:
            total_hours += ceil(b / rate)
        
        return total_hours <= maxH
