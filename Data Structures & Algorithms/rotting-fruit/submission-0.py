from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multisource BFS
        self.ROWS, self.COLS = len(grid), len(grid[0])
        num_fresh = 0
        # start the BFS from multiple sources

        queue = deque()

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if num_fresh == 0:
            # no fresh oranges
            return 0

        return self.bfs(num_fresh, grid, queue)

    def bfs(self, fresh, grid, queue):
        seen = set()
        count = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            count += 1

            for i in range(len(queue)):
                current = queue.popleft()
                
                if grid[current[0]][current[1]] == 1:
                    fresh -= 1

                for x_i, y_i in directions:
                    new_x, new_y = current[0] + x_i, current[1] + y_i

                    if 0 <= new_x < self.ROWS and 0 <= new_y < self.COLS \
                            and (new_x, new_y) not in seen \
                            and grid[new_x][new_y] == 1:
                        
                        seen.add((new_x, new_y))
                        queue.append((new_x, new_y))
        
        return -1 if fresh > 0 else count - 1
