class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1 and candidates[0] > target:
            return []
        
        self.results = []
        self.iterator = []
        self.target = target

        self.backtrack(candidates, 0, 0)

        return self.results
    
    def backtrack(self, nums, curr_index, sum):
        if sum == self.target:
            self.results.append(self.iterator.copy())
            return
        
        if sum > self.target:
            # overshot, so we return
            return
        
        for i in range(curr_index, len(nums)):
            self.iterator.append(nums[i])
            self.backtrack(nums, i, sum + nums[i])

            self.iterator.pop()
    
