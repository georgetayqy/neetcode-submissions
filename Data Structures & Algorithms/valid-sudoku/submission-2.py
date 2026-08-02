class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9

        rows = [set() for i in range(ROWS)]
        cols = [set() for i in range(COLS)]
        subboxes = [set() for i in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                current_item = board[row][col]

                if current_item == ".":
                    continue

                subbox_idx = (row // 3) * 3 + (col // 3)
            
                if current_item in rows[row] or current_item in cols[col] or current_item in subboxes[subbox_idx]:
                    return False
                
                rows[row].add(current_item)
                cols[col].add(current_item)
                subboxes[subbox_idx].add(current_item)

        return True
