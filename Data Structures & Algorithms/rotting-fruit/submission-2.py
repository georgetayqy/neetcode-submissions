from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        is_valid = lambda x, y: 0 <= x < row and 0 <= y < col
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        rotten = deque()
        visited = set()
        num_healthy = 0
        num_minutes = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num_healthy += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        # dfs?
        while rotten:
            did_rot = False

            for rot in range(len(rotten)):
                r, c = rotten.popleft()
                
                if (r, c) in visited or grid[r][c] == 0:
                    continue

                if grid[r][c] == 1:
                    num_healthy -= 1
                    grid[r][c] = 2
                    did_rot = True
                
                visited.add((r, c))

                for x, y in directions:
                    new_r, new_c = r + x, c + y

                    if is_valid(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        rotten.append((new_r, new_c))
            
            if did_rot:
                num_minutes += 1

        return -1 if num_healthy != 0 else num_minutes






