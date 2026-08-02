class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list first to take advantage of monotonic properties
        nums.sort()  # n log n

        print(nums)

        solutions = []
        previous = -(10 ** 5) - 1

        for i in range(len(nums)):
            if nums[i] == previous:
                continue
            
            previous = nums[i]
            solution = self.twoSum(nums, i, i + 1, -(nums[i]))

            if len(solution) > 0:
                solutions.extend(solution)
        
        return solutions

    def twoSum(self, nums: List[int], pointer: int, start: int, target: int) -> List[List[int]]:
        solutions = set()

        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                solutions.add((nums[pointer], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        
        return list(map(list, solutions))
 