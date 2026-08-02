class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_length = len(numbers)
        for i in range(num_length):
            for j in range(i + 1, num_length):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
