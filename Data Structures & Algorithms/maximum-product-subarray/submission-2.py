class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = [1 for i in range(len(nums) + 2)]
        min_so_far = [1 for i in range(len(nums) + 2)]
        
        max_pdt = float("-inf")
        for i in range(1, len(nums) + 1):
            max_so_far[i] = max(
                nums[i - 1],
                nums[i - 1] * max_so_far[i - 1],
                nums[i - 1] * min_so_far[i - 1],
            )
            min_so_far[i] = min(
                nums[i - 1],
                nums[i - 1] * max_so_far[i - 1],
                nums[i - 1] * min_so_far[i - 1],
            )
            max_pdt = max(max_so_far[i], max_pdt)
        
        return max_pdt
