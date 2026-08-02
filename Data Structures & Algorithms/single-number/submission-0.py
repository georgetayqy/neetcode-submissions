class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        results = 0

        for num in nums:
            results ^= num

        return results
    