class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        This is how the unique paths table look like initially
        > There is only one from the location to the destination

        +---+---+---+---+
        | X | X | X | 1 |
        +---+---+---+---+
        | X | X | X | 1 |
        +---+---+---+---+
        | 1 | 1 | 1 | 1 |
        +---+---+---+---+
        """
        # m is num rows, n is num cols
        # this is the current bottom row
        row = [1 for i in range(n)]

        # skip the last row (m - 1)th row since we know that it is always 1s
        # and it is filled above
        for i in range(m - 1):
            new_row = [1 for j in range(n)]
            
            # we avoid checking the rightmost column to avoid errors
            # we know that it is always 1
            for j in range(n - 2, -1, -1):
                # new_row represents the new row to add to the results 
                # row[j] represents the previous row
                """
                +---+---+---+---+
                | X | X | X | 1 |
                +---+---+---+---+
                | X | X | X | 1 |   < new row
                +---+---+---+---+
                | 1 | 1 | 1 | 1 |   < prev row
                +---+---+---+---+


                +---+---+------------+--------------+
                | X | X |     X      |      1       |
                +---+---+------------+--------------+
                | X | X | new_row(j) | new_row(j+1) |
                +---+---+------------+--------------+
                | 1 | 1 | row(j)     | 1            |
                +---+---+------------+--------------+
                """
                new_row[j] = new_row[j + 1] + row[j]
            
            # once we are done forming the row, we can set the prev row to the newly formed row
            row = new_row
        
        # once we are at the end, the new_row contains the most updated counts
        # we return the first element of the row
        return row[0]