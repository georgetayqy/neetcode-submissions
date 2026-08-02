class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []

        def find_next_unique_number(idx):
            current = nums[idx]

            for i in range(idx, len(nums)):
                if nums[i] != current:
                    return i
            
            # if cannot find unique number, then must be at the end of the list
            return len(nums)

        def recurse(array, current_idx):
            if current_idx >= len(nums):
                results.append(array)
                return
            
            # either pick the current number and continue on to the next number
            # or pick a new number and continue on from there
            recurse(array.copy() + [nums[current_idx]], current_idx + 1)
            recurse(array.copy(), find_next_unique_number(current_idx))

        # sort first then permute
        nums.sort()
        
        recurse([], 0)
        return results
