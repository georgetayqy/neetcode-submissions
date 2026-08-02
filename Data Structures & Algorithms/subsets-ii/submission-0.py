class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # similar idea to the one without dupes
        # difference being that if we choose not to include a particular
        # value, then we need to skip it for ALL occurrences of the
        # number to prevent the repeated formation of a repeated subset
        """
                        121                                                
                 ┌───────[]───────┐                                        
                 ▼                ▼             Make decision to include or
            ┌────1───┐        ┌───[]──┐ ◄───────exclude ALL 1s             
            ▼        ▼        ▼       ▼                                    
         ┌─12─┐    ┌─1─┐    ┌─2─┐     []◄───────Make decision to include or
         ▼    ▼    ▼   ▼    ▼   ▼               exclude ALL 2s             
        121   12   11  1    2   21                                         
        """
        
        results = []

        # we need to sort our input array first to make sure that
        # we can always select all of one element of the same value
        # or none of the element
        # [1, 1, 2, ...] -> [1, 1, ...] or [2, ...]
        nums.sort()

        def iterate(numbers, idx):
            # choose to include the idx's term in the solution or not
            # base case is to append when we reach the end
            if idx == len(nums):
                results.append(numbers.copy())
                return
            
            # create subsets that include all nums[i]
            numbers.append(nums[idx])
            iterate(numbers, idx + 1)
            numbers.pop()
            
            # create subsets that do NOT include nums[i]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                # why?
                # e.g. [1, 2, 2, 3],
                #             ^
                # if we are at 2, then we should skip 2 as well
                # until we are at the carat

                idx += 1
            
            # even if we skipped until the end of the array, we
            # still want to call iterate() to add the final
            # empty array
            iterate(numbers, idx + 1)

        iterate([], 0)
        return results
        