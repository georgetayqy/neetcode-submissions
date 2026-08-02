class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We can think of it as selecting and not selecting
        # each number to form the subset
        # if we draw it out as a tree, we can see that it looks like
        # a complete tree, where the leaves represent all the subsets
        #          ┌───────[]───────┐                   
        #          ▼                ▼                   
        #     ┌────1────┐       ┌───[]──┐         1 item
        #     ▼         ▼       ▼       ▼               
        #  ┌─12─┐     ┌─1─┐   ┌─2─┐   ┌─[]─┐      2 item
        #  ▼    ▼     ▼   ▼   ▼   ▼   ▼    ▼            
        # 123   12    13  1   2   23  3    []     3 item

        self.results = []
        self.subsets = []
        self.nums = nums
        self.backtrack(0)

        return self.results

    def backtrack(self, index_of_decision):
        # index_of_decision represents the 

        if index_of_decision >= len(self.nums):
            self.results.append(self.subsets.copy())
            return
        
        # include nums[i]
        # appending item includes the current num into
        # the subsets
        self.subsets.append(self.nums[index_of_decision])
        self.backtrack(index_of_decision + 1)

        # dont include nums[i]
        # popping it removes the current num from the subsets
        self.subsets.pop()
        self.backtrack(index_of_decision + 1)