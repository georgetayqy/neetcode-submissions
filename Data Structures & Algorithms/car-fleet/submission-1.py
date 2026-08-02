class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position first
        sorted_cars = sorted(list(zip(position, speed)), key=lambda x: x[0], reverse=True)
        time_stack = []

        # compute the time taken to reach the end
        # if the time taken by a car to reach the end is <= the top of the stack,
        # then it will join the fleet, otherwise create a new fleet

        for car_pos, speed in sorted_cars:
            T_delta = (target - car_pos) / speed
            
            if not time_stack:
                time_stack.append(T_delta)
            else:
                if time_stack[-1] < T_delta:
                    time_stack.append(T_delta)
                # else do nothing, part of the fleet
        
        return len(time_stack)