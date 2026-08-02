class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # reverse the problem
        # find the enclosed region ->
        # find the region that are not enclosed, the complement is the answer
        ROWS, COLS = len(board), len(board[0])

        def dfs(board, row, col):
            """
            Marks the outer region as "$", which means that it is the region
            that are not enclosed
            """

            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            
            if board[row][col] != "O":
                return
            
            board[row][col] = "$"

            dfs(board, row + 1, col)
            dfs(board, row - 1, col)
            dfs(board, row, col + 1)
            dfs(board, row, col - 1)            

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                    dfs(board, row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "$":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

