class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        other_slow = 0
        while True:
            slow = nums[slow]
            other_slow = nums[other_slow]

            if slow == other_slow:
                return slow
