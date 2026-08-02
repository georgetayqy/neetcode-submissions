class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack = []

        # The stack holds the tuple pairs (starting index, height)
        for index, height in enumerate(heights):
            """
            We notice that the heights should only increase in order to find the max rectangle area

            Once we encounter an element that breaks the monotonic increasing pattern, we can
            begin to pop the items off the stack until the top element in the stack is <= 
            the current element.

            For each iteration where we pop the rectangle, we need to compute the max size of
            the rectangle that can be formed if we were to take the currently iterated rectangle
            and extend it towards the right, towards the rectangle that breaks the monotonic
            increasing pattern.

            e.g. [1, 2, 3, 4, 1]
                              ^
            Iter1: [1, 2, 3, 1], max area = 4 * (index(^) - index(4)) => Notice how the area grows to the right
            Iter2: [1, 2, 1], max area = 3 * (index(^) - index(3))
            Iter3: [1, 1], max_area = 2 * (index(^) - index(2))
            Iter 4: [1 <= 1], so we terminate, and update index(^) = index(2) (NOT index(1, left), ALWAYS
                              ASSIGNED THE INDEX FOR THE ELEMENT THAT COMES NEXT)

            We can then push this (1, right) element onto the stack with the index(2)
            > But why?
              - By finding the left most index of the stack such that the height is <= current height,
                and assigning this value to the index of the current height, we essentially "EXTEND"
                the rectangle that can be formed at the leftmost index to the current index.
              - [1, 2, 3, 4, 2] => analogous to [1, 2, 2, 2, 2] (cuz, we can form the biggest rectangle
                                   with the last element, with the 3 element preceding it)

            If there are still elements in the stack at the end, then there are rectangles that we can
            extend to the end of the histogram.

            We need to repeat the same process as above when finding a non-monotonic increasing rectangle
            and find the max areas.

            > Note, at any point in the stack, each (index, element) means that there is a rectangle area of
              (len(heights) - index) * element

            >>> This algo is O(n) time, since we at worst need to push each element once and pop each 
            element once. O(2n) = O(2n)
            """

            # set the left most index where height(left_most) <= current iterated height
            starting_point = index

            # while the stack is not empty and the current element is < top of stack
            # violation of monotonic stack condition
            while stack and stack[-1][1] > height:
                # remove the current top of the stack
                curr_idx, element = stack.pop()

                # compute the max are that can form if we were to extend our current rectangle
                # all the way to current iterated rectangle (as above, in the for loop)
                # width = index - curr_index
                max_rect = max(max_rect, element * (index - curr_idx))

                # we can then extend the starting index of the current iterated rectangle (as in for loop)
                # all the way back to simulate the largest possible rectangle that can be formed using the
                # current iterated rectangle
                starting_point = curr_idx

            # add the currently iterated rectangle to the stack with the extended index
            stack.append((starting_point, height))

        # we then do a last computation of rectangles that can be extended to the END of the histogram
        # width = len(heights) - current index
        for index, height in stack:
            max_rect = max(max_rect, height * (len(heights) - index))

        return max_rect
