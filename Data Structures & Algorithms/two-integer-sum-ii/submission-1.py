class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_value = numbers[left] + numbers[right]

            if current_value == target:
                return [left + 1, right + 1]
            elif current_value > target:
                right -= 1
            elif current_value < target:
                left += 1
