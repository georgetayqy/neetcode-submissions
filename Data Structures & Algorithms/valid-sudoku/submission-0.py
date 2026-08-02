class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            print(row)

        DIMENSIONS = 9

        row_sets = [set() for i in range(DIMENSIONS)]
        col_sets = [set() for i in range(DIMENSIONS)]
        sub_sets = [set() for i in range(DIMENSIONS)]

        for i in range(DIMENSIONS):
            for j in range(DIMENSIONS):
                current = board[i][j]

                if current == ".":
                    continue

                if current in row_sets[i] or current in col_sets[j]:
                    return False

                row_sets[i].add(current)
                col_sets[j].add(current)

                sub_row_index = 0 if i < 3 else 3 if i < 6 else 6
                sub_col_index = 0 if j < 3 else 1 if j < 6 else 2
                sub_set_index = sub_row_index + sub_col_index
                print(i, j, sub_set_index)

                if current in sub_sets[sub_set_index]:
                    return False

                sub_sets[sub_set_index].add(current)

        return True
