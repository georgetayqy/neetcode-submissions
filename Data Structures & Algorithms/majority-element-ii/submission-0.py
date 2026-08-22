class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()

        previousElement = None
        left = 0
        numbers = []

        for right in range(len(nums)):
            if previousElement is None:
                previousElement = nums[right]
                continue
            
            if nums[right] == previousElement:
                continue
            else:
                if (right - left) > len(nums) // 3:
                    numbers.append(previousElement)
                
                previousElement = nums[right]
                left = right
        
        if right - left + 1 > len(nums) // 3:
            numbers.append(previousElement)

        return numbers
