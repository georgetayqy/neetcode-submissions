class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            # change the starting point
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                left_num, right_num = nums[left], nums[right]

                if left_num + right_num == -num:
                    results.append([num, left_num, right_num])
                    
                    # incrementing either pointer ensures uniqueness
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif left_num + right_num < -num:
                    left += 1
                else:
                    right -= 1
        
        return results