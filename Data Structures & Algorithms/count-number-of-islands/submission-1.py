class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        self.grid = grid
        self.is_valid_row = lambda x: 0 <= x <= row - 1
        self.is_valid_col = lambda x: 0 <= x <= col - 1
        self.is_valid_grid = lambda x, y: self.is_valid_row(x) and self.is_valid_col(y)

        num_island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                
                self.dfs(i, j)
                num_island += 1

        return num_island
    
    def dfs(self, row, col):
        stack = [(row, col)]
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        while stack:
            print(stack)
            curr_row, curr_col = stack.pop()
            current_item = self.grid[curr_row][curr_col]

            if current_item == "0":
                continue
            
            self.grid[curr_row][curr_col] = "0"
            for row_delta, col_delta in directions:
                new_row, new_col = row_delta + curr_row, col_delta + curr_col

                if self.is_valid_grid(new_row, new_col):
                    stack.append((new_row, new_col))
        