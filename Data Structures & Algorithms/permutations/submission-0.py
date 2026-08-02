class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 1:
            return nums
        
        if length == 1:
            return [[nums[0]]]
        
        results = []
        # O(n!) operation
        self.permutation([], nums, results)
        return results

    # O(n) space since we can reach up to n depth of the recursion before backtracking
    def permutation(self, current, nums, results):
        if len(current) == len(nums):
            # O(n) operation because of the slice
            results.append(current[:])
            return
        
        for num in nums:
            # check if the number is already exists in the list and move on if we found it
            # O(1)
            if num not in current:
                current.append(num)
                self.permutation(current, nums, results)
                current.pop()
