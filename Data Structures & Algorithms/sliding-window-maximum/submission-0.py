from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_numbers = []
        window = SortedList()
        left = right = 0

        while right < len(nums):
            if right - left < k:
                print("\tcontinued")
                window.add(nums[right])
                right += 1
                continue
            print(">>", right, window)
            max_numbers.append(window[-1])
            window.add(nums[right])
            window.discard(nums[left])
            right += 1
            left += 1
        
        max_numbers.append(window[-1])
        
        return max_numbers
