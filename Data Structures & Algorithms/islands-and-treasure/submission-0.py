class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        INF = 2 ** 31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        all_sources = deque()

        # multisource BFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    all_sources.append((i, j, 0))
        
        seen = set()
        
        while all_sources:
            for i in range(len(all_sources)):
                x, y, distance = all_sources.popleft()

                if (x, y) in seen:
                    continue
                
                seen.add((x, y))

                if grid[x][y] == INF:
                    grid[x][y] = min(grid[x][y], distance)
                
                for x_i, y_i in directions:
                    new_x, new_y = x + x_i, y + y_i

                    if 0 <= new_x < ROWS and 0 <= new_y < COLS \
                            and (new_x, new_y) not in seen \
                            and grid[new_x][new_y] == INF:
                        all_sources.append((new_x, new_y, distance + 1))
