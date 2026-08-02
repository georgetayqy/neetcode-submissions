class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = -1

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                curr_area = min(heights[i], heights[j]) * (j - i)
                area = max(area, curr_area)

        return area