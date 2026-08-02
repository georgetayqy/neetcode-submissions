class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert it to a hashset
        numset = set(nums)

        # note that the start of a sequence does not have a left
        # neighbour, if it the start of a sequence
        # 1, 2, 3, 4, 100, 200
        # 0 not in sequence, hence it is the start
        max_len = 0

        for num in numset:
            if num - 1 not in numset:
                # we found the start! we can start at 0 since
                # the current value num + 0 = num is in the set
                # removes iterator logic from checking the first element
                iterator = 0

                while num + iterator in numset:
                    iterator += 1

                max_len = max(max_len, iterator)

        return max_len
