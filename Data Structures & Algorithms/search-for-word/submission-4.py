from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS) or (
                board[row][col] != word[index] or (row, col) in visited
            ):
                return False
            
            # mark as visited first
            visited.add((row, col))

            # recurse
            results = dfs(row + 1, col, index + 1) or \
                      dfs(row, col + 1, index + 1) or \
                      dfs(row - 1, col, index + 1) or \
                      dfs(row, col - 1, index + 1)

            # unmark it for future iteration
            visited.remove((row, col))

            # return result
            return results

        for row in range(ROWS):
            for col in range(COLS):
                visited = set()

                if dfs(row, col, 0):
                    return True

        return False
