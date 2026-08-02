class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Since we cannot rob the first and last house together, we should
        find the max amount to rob from the houses
        1. without the first house
        2. without the last house
        
        > Find the max when we skip the first house [1:]
        > Find the max when we skip the last house [:-1]
        > If we only have 1 house, then it is the max amount robbed
        """

        return max(
            nums[0],
            self.robber(nums[:len(nums) - 1]),
            self.robber(nums[1:])
        )
    
    def robber(self, nums):
        """
        Reusing house robber I
        """

        # [rob1, rob2, n, n + 1, ...]
        rob1, rob2 = 0, 0

        for num in nums:
            # current max = max(
            #   [not robbing the previous house => skipping rob2](rob1 + n)
            #   [robbing the previous house => robbing rob2 instead, so cannot rob n](rob2)
            # )
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp

        # contains the max amount we can rob from the entire input array
        return rob2