class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_value = 0
        
        # at least n^2 so might as well just sort
        nums.sort()

        for i in range(len(nums)):
            print(nums[i])

            previous = nums[i]
            inner_count = 1

            for j in range(i + 1, len(nums)):
                if nums[j] - previous == 1:
                    print(f"woah: {nums[j]}")
                    previous = nums[j]
                    inner_count += 1

            max_value = max(max_value, inner_count)

        return max_value