class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        We can view the positions and speeds as a system of linear equations
        Think of plotting position against time. Each vector represents the
        car's path in spacetime. If the vector intersect at a point before 
        the target, then they will become a car fleet (since no car can move 
        faster than the other)

        If we consider the cars in sorted order (why? relative order of the
        cars won't change).

        How do we know if they will collide? We can either compute the
        intersection point between any two pairs of cars,

        OR

        we can compute the time needed to reach the target.

        e.g. If car moves at 2 unit/s and bus move at 1 unit/s
        from a starting position of 2, 3, with target = 4,
        we know that the total time the car needs to get to the
        target is (target - position) / 2 (-> speed) = 1s and
        the total time the bus needs to get to the target is
        (target - position) / 1 (-> speed) = 1s.

        Since the time of the bus ahead is >= car, then we know that
        they MUST intersect somewhere before or at the target.

        NOTE THAT WE MUST CHECK THAT THE CAR IN FRONT HAS A TIME >= THE CAR BEHIND
        > LESS TIME TO REACH THE TARGET FOR CAR BEHIND -> MUST SOMEHOW COLLIDE

        ---

        We can also remove cars that intersect since they are now part of the fleet,
        but which car do we keep? We keep the one in front as fleets will move at
        the same speed as the car at the front of the fleet.

        ---

        We will also iterate in reverse since we need the final speeds of the cars,
        if we start from the front of the list, we wont know if the cars will collide
        since we dont know the final speed of the car in front.
        """

        # package the car's position and speed together
        cars = list(zip(position, speed))

        # we need to sort by the position of the cars to ensure that we can get
        # the formation of car fleets in order
        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for pos, spd in cars:
            time_to_reach_target = (target - pos) / spd
            stack.append(time_to_reach_target)

            # collision possible here since there are 2 cars at least
            # check if the current top of the stack reaches the end faster than that
            # of the car at the front
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # if so, we need to pop the head of the stack
                # why? if the head contains a car that reaches the target faster than the car
                # in front (in the stack), then it must collide and travel at the same speed
                # as the car in front, so we remove the car behind (the car we just added to
                # the stack) to ensure that the slowest moving car (the limiting factor) is 
                # always at the front of the stack
                stack.pop()

            # but why if and not while?
            # We are traversing the cars in reverse, so we dont have to check if the cars
            # will continue to collide with the cars in front
            # The stack will always maintain the car that is at the frontier of each fleet.
            # If you will collide with the frontier, then you are already part of it and will
            # travel at the same speed as the other cars in the frontier

        return len(stack)
