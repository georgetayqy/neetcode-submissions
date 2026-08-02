class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Why is it a tortoise and hare problem?

        see [1, 2, 3, 2, 2]
             ^
                ^
                   ^
        If we start at the 0th index, we are then led to the 1st pointer
        If we start at the 1st index, we are then led to the 2nd pointer
        If we start at the 2nd index, we are then led to the 3rd pointer
        If we are at the 3rd pointer, we realise we are redirected back to 2
          > so we have found a rho-shaped loop!
          > so it must be a tortoise and hare problem
        
        Prove: The distance between the start of the list to the point where the 
               loop begins is equal to the distance between where the loop ends
               and begins intersecting with the start of the loop
        
        0 -> 1 -> 2 -> 3 -> 4
             ^              |
             |              |
             ----------------

        If we define the distance between 0 to 1 as p, the distance between the start
        of the list to the start of the loop, and the distance between 4 to 1 as x,
        the distance between the end of the loop to the intersection point of the list
        and c as the overall length of the loop, we observe the following:

        For the fast and slow pointer to meet,
        SLOW: Traverse the first p distance to enter the loop, make one round around the loop
              and stop right before the intersection point 4. So its total distance travelled
              is (p + c - x)
        FAST: Traverse the first p distance to enter the loop, make one full round around the
              loop, and then make one more round around the loop, stopping short of the 
              intersection point. (why? the fast pointer covers 2x the distance compared to 
              the slow pointer)

        We also notice that d(slow) * 2 = d(fast), where d=distance the pointers travel
        => 2(p + c - x) = p + c - x + c
        => 2(p + c - x) = p + 2c - x
        => p - x = 0
        => p = x
        
        Proven.

        ---

        The starting portion of the loop can actually be very long, longer than the length
        of the loop itself at times.

        But it doesn't matter, it just means that we need to traverse many rounds around 
        the loop before we reach back at the intersection point again and the pointers
        would then be at the start of the loop
        """

        # we start at 0 as 0 is confirm not part of the loop

        # 0 -> 1 -> 2 ... -> 1 BUT NEVER 0 as n in > [1 ... n]
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # if it intersects, break
            if slow == fast:
                break
            
        # we need to start from the start of the list (the non-returning
        # points)
        slow_traverser = 0

        while True:
            slow_traverser = nums[slow_traverser]
            slow = nums[slow]

            # once they meet, we know that it must have intersected
            # and we have found the start of the loop
            if slow_traverser == slow:
                return slow_traverser
