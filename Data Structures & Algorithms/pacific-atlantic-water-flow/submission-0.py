class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        The intuition is that a point is can reach both the pacific ocean
        and the atlantic ocean IFF there is a non-increasing path of heights
        leading from the cell to both oceans

        From the perspective of the oceans, a cell is reachable IFF there is a
        NON-DECREASING path from it to the cell.

        We do 2 passes to scan the areas that are reachable from the pacific
        and the atlantic

        And we find the intersection of the two sets of reachable cells
        to get cells that are reachable from the pacific and the atlantic
        (which is our answer)
        """

        self.ROWS, self.COLS = len(heights), len(heights[0])

        # store areas that are reachable from the pacific ocean and the
        # atlantic ocean
        pset = set()
        aset = set()

        # DFS starting from the top row and the bottom row where the pacific
        # and atlantic oceans are at
        for i in range(self.COLS):
            # dfs the pacific ocean first to find all nodes reachable from pacific ocean
            self.dfs(pset, 0, i, heights[0][i], heights)
            self.dfs(aset, self.ROWS - 1, i, heights[self.ROWS - 1][i], heights)
        
        # DFS starting from the left and right column where the pacific
        # and atlantic oceans are at
        for i in range(self.ROWS):
            # dfs the pacific ocean first to find all nodes reachable from pacific ocean
            self.dfs(pset, i, 0, heights[i][0], heights)
            self.dfs(aset, i, self.COLS - 1, heights[i][self.COLS - 1], heights)
        
        return list(map(lambda x: list(x), pset.intersection(aset)))
        

    def dfs(self, s, x, y, previous_height, heights):
        distances = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        # if visited, do not explore again
        if (x, y) in s:
            return
        
        # if out of bounds we dont explore
        if x < 0 or x >= self.ROWS or y < 0 or y >= self.COLS:
            return

        # check if our current height is less than the previous height
        # means that the cell cannot reach the ocean (ocean cannot reach the cell)
        if heights[x][y] < previous_height:
            return

        # if it is valid, we add it to the seen set
        s.add((x, y))

        # then, we explore the neighbours of the cell
        for deltax, deltay in distances:
            new_x = deltax + x
            new_y = deltay + y

            # we need to pass in the CURRENT HEIGHT
            # WHICH WOULD BE THE PREVIOUS HEIGHT WRT THE NEW DFS NODE EXPLORED
            self.dfs(s, new_x, new_y, heights[x][y], heights)
    
        
        

            