from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # flood fill algorithm
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()

        count = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    count += 1

                    self.bfs(grid, i, j)

        return count
                    
    # We can convert it to a DFS easily, by changing popleft() to pop()
    def bfs(self, grid, x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            # do not need the for loop here as we are not going
            # in level order
            item = queue.popleft()

            if item in self.visited:
                continue
            
            self.visited.add(item)
            x, y = item

            for x_i, y_i in self.directions:
                new_x = x + x_i
                new_y = y + y_i

                if (new_x, new_y) in self.visited:
                    # if we have already visited it
                    continue
                
                if new_x < 0 or new_x >= self.rows or new_y < 0 or new_y >= self.cols:
                    # if it is out of bounds
                    continue
                
                if grid[new_x][new_y] == "0":
                    # if it is an empty grid
                    continue
                
                # if not, then we add it to bfs to search
                queue.append((new_x, new_y))
        