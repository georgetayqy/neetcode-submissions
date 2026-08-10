class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])

        total_sum = [[0 for i in range(col + 1)] for j in range(row + 1)]

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                total_sum[r][c] = (
                    matrix[r][c] 
                    + total_sum[r + 1][c]
                    + total_sum[r][c + 1]
                    - total_sum[r + 1][c + 1]
                )
        self.total_sum = total_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_top_left = self.total_sum[row1][col1]
        total_top_right = self.total_sum[row1][col2 + 1]
        total_bottom_left = self.total_sum[row2 + 1][col1]
        total_bottom_right = self.total_sum[row2 + 1][col2 + 1]

        return (
            total_top_left
            - total_top_right
            - total_bottom_left
            + total_bottom_right
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)