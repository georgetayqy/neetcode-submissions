class Solution:
    def rob(self, nums: List[int]) -> int:
        # break the loop, check two possible robbable
        # arrays

        if len(nums) <= 2:
            return max(nums)
        
        return max(
            self.rob_once(0, len(nums) - 2, nums),
            self.rob_once(1, len(nums) - 1, nums)
        )
    
    def rob_once(self, left, right, nums):
        rob_lag_two, rob_lag_one = 0, 0

        for i in range(left, right + 1):
            temp = max(
                rob_lag_one,
                rob_lag_two + nums[i]
            )
            rob_lag_one, rob_lag_two = temp, rob_lag_one
        
        return rob_lag_one
