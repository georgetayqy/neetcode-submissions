class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            current_target = target - numbers[i]
            left, right = i + 1, len(numbers) - 1

            while left <= right:
                middle = left + (right - left) // 2
                
                if numbers[middle] == current_target:
                    return [i + 1, middle + 1]
                elif numbers[middle] < current_target:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return []
