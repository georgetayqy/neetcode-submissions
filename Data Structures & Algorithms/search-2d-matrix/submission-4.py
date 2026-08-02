class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            middle = left + (right - left) // 2

            mrow, mcol = middle // COLS, middle % COLS
            middle_element = matrix[mrow][mcol]

            if target == middle_element:
                return True
            elif target < middle_element:
                right = middle - 1
            else:
                left = middle + 1

        return False