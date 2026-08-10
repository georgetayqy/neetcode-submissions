class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        previous_element = None
        count = 0

        for num in nums:
            if previous_element is None:
                previous_element = num
                count = 1
                continue
            
            if num == previous_element:
                count += 1
            else:
                count -= 1

                if count < 0:
                    previous_element = num
        
        return previous_element
