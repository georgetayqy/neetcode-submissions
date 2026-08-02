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

            stack = [(row, col)]

            while stack:
                r, c = stack.pop()

                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue
                
                if board[r][c] != "O":
                    continue
                
                board[r][c] = "$"
                
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row == 0 or 
                    row == ROWS - 1 or 
                    col == 0 or 
                    col == COLS - 1) and
                    board[row][col] == "O"
                ):
                    dfs(board, row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "$":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

