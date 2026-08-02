from collections import deque

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

        # add all pacific starting points
        pstack = self.get_pacific_starts(pset, heights)

        # add all atlantic starting points
        astack = self.get_atlantic_starts(aset, heights)
        
        # iterative BFS for both queues
        self.iter_dfs(pstack, pset, heights)
        self.iter_dfs(astack, aset, heights)
        
        # return the intersection
        return list(map(lambda x: list(x), pset.intersection(aset)))
    
    def get_pacific_starts(self, pset, heights):
        stack = deque()

        for i in range(len(heights)):
            if i == 0:
                for j in range(len(heights[0])):
                    stack.append(((i, j), heights[i][j]))
            else:
                stack.append(((i, 0), heights[i][0]))
        
        return stack
    
    def get_atlantic_starts(self, aset, heights):
        stack = deque()

        for i in range(len(heights)):
            if i == len(heights) - 1:
                for j in range(len(heights[0])):
                    stack.append(((i, j), heights[i][j]))
            else:
                stack.append(((i, len(heights[0]) - 1), heights[i][len(heights[0]) - 1]))
        
        return stack

    def iter_dfs(self, stack, s, heights):
        distances = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while stack:
            (x, y), prev_height = stack.popleft()

            if (x, y) in s:
                continue
            
            if x >= self.ROWS or x < 0 or y >= self.COLS or y < 0:
                continue
            
            # remember, from the ocean's perspective, the cell must have a height that
            # is greater than the previously seen height in order for water to flow from
            # the cell into the oceam
            # [5, 4, 3] OCEAN
            # 5 -> 4 -> 3 -> OCEAN
            # BUT
            # [3, 4, 5] OCEAN
            # 3 -> X
            if heights[x][y] < prev_height:
                continue
            
            s.add((x, y))

            for xd, yd in distances:
                new_x, new_y = xd + x, yd + y
                stack.append(((new_x, new_y), heights[x][y]))
            