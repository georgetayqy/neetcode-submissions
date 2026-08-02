from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multiple source BFS
        treasure_coordinates = []
        INF = 2147483647
        ROW, COL = len(grid), len(grid[0])
        directions = (
            (1, 0), (0, 1), (-1, 0), (0, -1)
        )
        visited = set()
        is_valid = lambda x, y: 0 <= x < ROW and 0 <= y < COL and grid[x][y] != -1 and (x, y) not in visited

        # iterate to find the treasures first
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    treasure_coordinates.append((i, j))
        
        q = deque([(point, 0) for point in treasure_coordinates])

        while q:
            for i in range(len(q)):
                (row, col), distance = q.popleft()
                
                if (row, col) in visited:
                    continue

                grid[row][col] = distance                
                visited.add((row, col))

                for x, y in directions:
                    new_row, new_col = x + row, y + col

                    if is_valid(new_row, new_col):
                        q.append(((new_row, new_col), distance + 1))
    