class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # terminate early if there is only 1 or no elements in the list
        if len(nums) <= 1:
            return len(nums)

        # sort the numbers first
        nums.sort()

        # set vars to check, make sure to init to 1, since the first element is already taken into consideration
        max_len = 1
        curr_len = 1

        # then, increment from left to right, skipping past elements of the same value
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_len += 1
                else:
                    max_len = max(curr_len, max_len)
                    curr_len = 1
            # else condition can be skipped, if they are equal, do nothing, the max and curr values
            # should still be the same (since no element was added or removed from the sequence)
            # can be thought of as compressing the duplicates into 1

        return max(max_len, curr_len)
