class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[-1])
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        def dfs(row, col):
            index = 0
            seen = set()

            def _inner_dfs(row, col, index):
                if index == len(word):
                    return True

                if (
                    (row >= ROWS or col >= COLS or row < 0 or col < 0) or
                    (board[row][col] != word[index]) or
                    ((row, col) in seen)
                ):
                    return False
                
                seen.add((row, col))
                results = (
                    _inner_dfs(row + 1, col, index + 1) or
                    _inner_dfs(row - 1, col, index + 1) or
                    _inner_dfs(row, col + 1, index + 1) or
                    _inner_dfs(row, col - 1, index + 1)
                )

                seen.remove((row, col))
                
                return results

            return _inner_dfs(row, col, 0)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col):
                        return True

        return False
