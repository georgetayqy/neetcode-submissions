class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.rows, self.cols = ROWS, COLS
        self.prefix = [[0 for i in range(COLS)] for j in range(ROWS)]

        for row in matrix:
            print(row)

        for row in range(ROWS):
            for col in range(COLS):
                if row == col == 0:
                    self.prefix[row][col] = matrix[row][col]
                    continue
                
                self.prefix[row][col] = matrix[row][col]
                
                if 0 <= row - 1 < ROWS:
                    self.prefix[row][col] += self.prefix[row - 1][col]
                
                if 0 <= col - 1 < COLS:
                    self.prefix[row][col] += self.prefix[row][col - 1]
                
                if 0 <= row - 1 < ROWS and 0 <= col - 1 < COLS:
                    self.prefix[row][col] -= self.prefix[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        max_row, min_row, max_col, min_col = max(row1, row2), min(row1, row2), max(col1, col2), min(col1, col2)

        # <> X <>
        #  X O X
        # <> X O

        big_bounding_area = self.prefix[row2][col2]

        if 0 <= min_row - 1 < self.rows:
            big_bounding_area -= self.prefix[min_row - 1][max_col]
        
        if 0 <= min_col - 1 < self.cols:
            big_bounding_area -= self.prefix[max_row][min_col - 1]

        if 0 <= min_row - 1 < self.rows and 0 <= min_col - 1 < self.cols:
            big_bounding_area += self.prefix[min_row - 1][min_col - 1]

        return big_bounding_area


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)