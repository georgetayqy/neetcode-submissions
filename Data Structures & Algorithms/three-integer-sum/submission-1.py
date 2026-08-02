class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it, then convert it to a 2 sum by affixing the first element
        # naive is n^3, n log n is acceptable
        nums.sort()

        # no need to guard against funny length nums, since minimally guaranteed 3
        # but if needed
        # if len(nums) < 3:
        #     return []

        possible = set()

        for i in range(0, len(nums) - 2):
            left_value = nums[i]

            mid, right = i + 1, len(nums) - 1

            while mid < right:
                mid_value, right_value = nums[mid], nums[right]

                if left_value + mid_value + right_value == 0:
                    possible.add((left_value, mid_value, right_value))
                    mid += 1
                    right -= 1
                elif left_value + mid_value + right_value > 0:
                    right -= 1
                else:
                    mid += 1

        return [list(x) for x in possible]
