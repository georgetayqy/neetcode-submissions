from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        max_area = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.visited or grid[i][j] == 0:
                    continue
                
                max_area = max(max_area, self.bfs(grid, i, j))
        
        return max_area
    
    # to change to dfs, change the order in which we remove it
    # by calling pop() instead
    def bfs(self, grid, x, y):
        queue = deque()
        queue.append((x, y))
        area = 0

        while queue:
            # I AM NOW A STACK
            current = queue.pop()

            if current in self.visited:
                continue
            
            self.visited.add(current)
            curr_x, curr_y = current
            
            area += grid[curr_x][curr_y]

            for x_i, y_i in self.directions:
                new_x = curr_x + x_i
                new_y = curr_y + y_i

                if (new_x, new_y) in self.visited:
                    # if it is already visited, then we don't want to visit it again
                    continue
                
                if new_x < 0 or new_x >= self.rows or new_y < 0 or new_y >= self.cols:
                    # if out of range, then we dont do anything
                    continue
                
                if grid[new_x][new_y] == 0:
                    # we do nothing here as there is no island
                    continue
                
                # if we found a legit spot to extend into, we add it into the queue
                queue.append((new_x, new_y))

        return area
