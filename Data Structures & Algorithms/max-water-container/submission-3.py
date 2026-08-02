class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = -1

        while left < right:
            left_height, right_height = heights[left], heights[right]
            max_area = max(max_area, min(left_height, right_height) * (right - left))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area
