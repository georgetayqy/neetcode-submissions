class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it, then convert it to a 2 sum by affixing the first element
        # naive is n^3, n log n is acceptable
        nums.sort()

        # no need to guard against funny length nums, since minimally guaranteed 3
        # but if needed
        # if len(nums) < 3:
        #     return []

        possible = []

        for i in range(0, len(nums) - 2):
            left_value = nums[i]

            # there is no way that the following elements can add to 0
            # since everyone is +ve
            if left_value > 0:
                break

            # skipping duplicates at the start of the array
            # since numbers are sorted, it is possible that we may create
            # outputs that start with the same element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            mid, right = i + 1, len(nums) - 1

            while mid < right:
                mid_value, right_value = nums[mid], nums[right]

                if left_value + mid_value + right_value == 0:
                    possible.append([left_value, mid_value, right_value])
                    mid += 1

                    # idea is to always skip the left number if it is duplicated
                    # and to increment it (!!! the left value will always determine
                    # the solutions that we get in the array, if we keep it unique
                    # per iteration then the solutions will also be unique !!!)
                    # right pointer will be fixed by the next iteration of the loop
                    # there is no need to update it
                    while nums[mid] == nums[mid - 1] and mid < right:
                        mid += 1

                elif left_value + mid_value + right_value > 0:
                    right -= 1
                else:
                    mid += 1

        return possible
