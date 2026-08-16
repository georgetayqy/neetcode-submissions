class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        all_rows, all_cols, all_boxes = [set() for i in range(9)], [set() for i in range(9)], [[set() for i in range(3)] for j in range(3)]

        for row in range(9):
            for col in range(9):
                current_cell = board[row][col]

                if current_cell in all_rows[row] and current_cell != ".":
                    return False
                all_rows[row].add(current_cell)

                if current_cell in all_cols[col] and current_cell != ".":
                    return False
                all_cols[col].add(current_cell)
                
                subbox_row, subbox_col = row // 3, col // 3
                if current_cell in all_boxes[subbox_row][subbox_col] and current_cell != ".":
                    return False
                all_boxes[subbox_row][subbox_col].add(current_cell)

        return True
