from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_numbers = []
        window = []
        left = right = 0

        while right < len(nums):
            if right - left < k:
                heappush(window, (-nums[right], right))
                right += 1
                continue

            print("Before", window)
            while window and not left <= window[0][-1] < right:
                heappop(window)
            print("After", window)

            max_numbers.append(-window[0][0])
            heappush(window, (-nums[right], right))
            print("\tAfter", window)
            right += 1
            left += 1
        
        while window and not left <= window[0][-1] < right:
            heappop(window)
        
        max_numbers.append(-window[0][0])
        
        return max_numbers
