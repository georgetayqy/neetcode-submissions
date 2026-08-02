class Solution:
    def jump(self, nums: List[int]) -> int:
        u"""
        L/R───┐│      │            │ L    │            │      │ L              
              ││      │            │ │    │            │ ┌────┼┐              
              ▼│      │            │ ▼    │            │ │    │▼              
            [ 2│ 3, 1,│1, 4 ] > [ 2│ 3, 1,│1, 4 ] > [ 2│ 3, 1,│1, 4 ]         
               │      │           ││    ▲ │            │ │    │   ▲           
               │      │           └┼────┘ │            │ └────┼───┘           
               │      │            │    R │            │      │   R           
                                                                                
        For each "Section" of the array, defined as the max distance we can      
        jump to, we compute the new max distance we can jump to and set our      
        right pointer to that. The left pointer merely iterates from left        
        to right, computing the max distance we can jump and setting right       
        to that. left = right + 1 (to skip the end) right = index + farthest jump

        The total number of jumps is hence the total number of partitions of the array
        that we have "jumped" across
        """

        # Do 1D BFS here
        results = 0
        
        # this is our window to BFS
        left, right = 0, 0
        
        # we continue BFS until we reach the end
        # once the right reaches the end, we can terminate and return the max number of counts
        while right < len(nums) - 1:
            # between our window, we need to decide the farthest index we can jump to
            # once we determine that, we set left = right + 1
            # and right to be our farthest index
            farthest = 0
            
            # to determine the farthest distance we can jump, we advance our left pointer
            # towards and cross the right pointer
            # need to include right as well as it is at the edge of the same segment of the
            # array
            for i in range(left, right + 1):
                # determine who can jump the farthest
                # i + nums[i] is the index where we can jump right now
                farthest = max(farthest, i + nums[i])

            # at the end, make sure to advance left FORWARD TO RIGHT + 1
            # since we HAVE PREVIOUSLY TAKEN RIGHT INTO ACCOUNT WHEN FINDING THE NEXT FARTHEST JUMP INDEX
            # set right to farthest
            left, right = right + 1, farthest

            # every time we have cross our current BFS window and JUMPED INTO THE NEXT PARTITION, WE HAVE
            # TO INCREMENT THE NUMBER OF JUMPS BY 1
            results += 1

        return results