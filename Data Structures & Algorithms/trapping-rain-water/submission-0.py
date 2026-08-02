class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            # there is no way for the pillars to trap any sort of water if there are only 2 pillars
            return 0
        
        left, right = 0, length - 1
        max_left, max_right = height[left], height[right]
        total = 0

        while left < right:
            # we shift the pointer with the smaller max value
            # if the left has a smaller max, we shift it to the right
            # if the right has a smaller min, we shift it to the left

            # we know the max left at any time, but we dont know the corresponding
            # max right, but why don't we need it?
            # we want the min(max_left, max_right), if our max_left is lower
            # then the right, then we know it is the bottleneck (any water between
            # the bounding pillars will be restricted to the min of the max heights
            # of the bounding pillars)
            
            # Alternatively, if we know that left=k and right=m and if k = m,
            # and the current height is < k, then we know that k - current
            # height of water must be stored somewhere between the bounding
            # pillars (water flows down) 
            
            # if both maxes are the same, we can just shift any pointer

            # **this process defines the bounding areas of the water body**

            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])

                # if we subtract without updating the max first, then we
                # need to check to make sure that the difference is not
                # negative
                total += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                total += max_right - height[right]

        return total
