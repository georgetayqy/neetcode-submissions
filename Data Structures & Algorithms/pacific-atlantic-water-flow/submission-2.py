class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited_set, previous_height):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row, col) in visited_set or
                heights[row][col] < previous_height
            ):
                return
            
            visited_set.add((row, col))

            dfs(row + 1, col, visited_set, heights[row][col])
            dfs(row - 1, col, visited_set, heights[row][col])
            dfs(row, col + 1, visited_set, heights[row][col])
            dfs(row, col - 1, visited_set, heights[row][col])
        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])
        
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])
        
        return [
            list(x) for x in pacific.intersection(atlantic)
        ]
