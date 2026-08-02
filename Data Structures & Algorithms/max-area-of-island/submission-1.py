class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.grid = grid

        row, col = len(grid), len(grid[0])
        self.is_valid_grid = lambda x, y: 0 <= x < row and 0 <= y < col

        for i in range(row):
            for j in range(col):
                if self.grid[i][j] == 0:
                    continue

                max_area = max(max_area, self.dfs(i, j))

        return max_area

    def dfs(self, i, j):
        stack = [(i, j)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        area = 0

        while stack:
            r, c = stack.pop()

            if self.grid[r][c] == 0:
                continue
            
            self.grid[r][c] = 0
            area += 1

            for x, y in directions:
                x_new, y_new = x + r, y + c

                if self.is_valid_grid(x_new, y_new):
                    stack.append((x_new, y_new))
        
        return area
