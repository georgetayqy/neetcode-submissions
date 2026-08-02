class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start at the end and move towards the middle, going in the direction of the max height

        left, right = 0, len(height) - 1
        max_volume = -1

        while left < right:
            left_height, right_height = height[left], height[right]
            curr_volume = (right - left) * min(left_height, right_height)
            max_volume = max(max_volume, curr_volume)

            if left_height > right_height:
                right -= 1
            elif left_height < right_height:
                left += 1
            else:
                right -= 1
                left += 1

        return max_volume
    