class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # (idx, element)
        out = [0 for i in range(len(temperatures))]

        # stack should be a monotonic decreasing stack
        # we append to the stack if the current value is <= new value

        for idx, element in enumerate(temperatures):
            # if the stack is not empty, is the current temp > the top of
            # stack? if so we have found the condition that violates a
            # monotonic decreasing stack, so we pop until the condition is true

            while stack and element > stack[-1][1]:
                curr_idx, curr_element = stack.pop()

                # computes the distance between the item in the stack,
                # and the new max item we just found
                out[curr_idx] = idx - curr_idx

            stack.append((idx, element))

        return out
