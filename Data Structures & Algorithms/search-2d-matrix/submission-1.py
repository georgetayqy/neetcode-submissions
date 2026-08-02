class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find the row first
        # then binary search to find the column
        row_low, row_high, col_low, col_high = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while row_low < row_high:
            mid_row = row_low + (row_high - row_low) // 2
            max_list = matrix[mid_row][-1]

            if max_list == target:
                return True
            elif max_list < target:
                row_low = mid_row + 1
            else:
                row_high = mid_row

        correct_row = matrix[row_low]

        while col_low < col_high:
            mid_col = col_low + (col_high - col_low) // 2
            current_element = correct_row[mid_col]

            if current_element == target:
                return True
            elif current_element < target:
                col_low = mid_col + 1
            else:
                col_high = mid_col

        return correct_row[col_low] == target
