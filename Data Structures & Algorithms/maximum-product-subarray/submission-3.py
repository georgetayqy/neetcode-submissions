class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = [1 for i in range(len(nums) + 2)]
        min_so_far = [1 for i in range(len(nums) + 2)]

        max_pdt = float("-inf")
        maxes = 1
        mins = 1
        
        for num in nums:
            maxes, mins = max(
                num,
                num * maxes,
                num * mins
            ), min(
                num,
                num * maxes,
                num * mins
            )

            max_pdt = max(max_pdt, maxes)
        
        return max_pdt
