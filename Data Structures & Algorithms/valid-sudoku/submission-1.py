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

                sub_row_index = i // 3
                sub_col_index = j // 3
                sub_set_index = 3 * sub_row_index + sub_col_index
                print(i, j, sub_set_index)

                if current in sub_sets[sub_set_index]:
                    return False

                sub_sets[sub_set_index].add(current)

        return True
