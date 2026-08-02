from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = [[]]
        self.nums = nums
        self.backtrack([], -1)

        return self.results

    def backtrack(self, current, index):
        if index == len(self.nums):
            return

        for i in range(index + 1, len(self.nums)):
            copied = current.copy() + [self.nums[i]]
            self.results.append(copied)
            self.backtrack(copied, i)
