class Solution:
    def jump(self, nums: List[int]) -> int:
        # Do 1D BFS here
        results = 0
        
        # this is our window to BFS
        left, right = 0, 0
        
        # we continue BFS until we reach the end
        # once the right reaches the end, we get a 
        while right < len(nums) - 1:
            # between our window, we need to decide the farthest index
            # we can jump to
            # once we determine that, we set left = right + 1
            # and right to be our farthest index
            farthest = 0
            
            # we need to include the right value
            for i in range(left, right + 1):
                # determine who can jump the farthest
                # i + nums[i] is the index where we can jump right now
                farthest = max(farthest, i + nums[i])

            left, right = right + 1, farthest

            # everytime we cross the BFS window, we need to add 1
            results += 1

        return results