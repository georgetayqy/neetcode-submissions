class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}

        return self.robbed(0)
    
    def robbed(self, num):
        if num >= len(self.nums):
            return 0
        
        if num in self.memo:
            return self.memo[num]
        
        self.memo[num] = max(self.nums[num] + self.robbed(num + 2),
                             self.robbed(num + 1))
        return self.memo[num]
