class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            value = numbers[start] + numbers[end]

            if value == target:
                # add 1 as it is 1-indexed
                return [start + 1, end + 1]
            elif value > target:
                end -= 1
            else:
                start += 1
        
        # return nothign as it is guaranteed to have at least 1 solution