class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DFS/Backtracking with Brute force: Select a number of don't: O(2^n)
        Cache the Brute force:
            > Check all subsequences starting from each indices in the num
            > X -> start at 1
            >   |_> start at 2
                |_> start at 3
                ...
            > Starting from the end, we can compute the LIS properly with
              a cache
        """

        dp = [1 for i in range(len(nums))]    

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # if we want increasing subseq, we need i < j
                # j comes after i
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        # return the max of the dp array
        # dp only compute the pattern, but we need to find the max
        return max(dp)