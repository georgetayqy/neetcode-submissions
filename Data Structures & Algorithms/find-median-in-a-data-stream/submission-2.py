class MedianFinder:
    """
    The idea is to think of the median number as the partitioning
    number, and to split it into two halves,
    -> left half, values smaller than the median
    -> right half, values larger than the median

    [1, 2, 3, 4]

    The median can be defined as the average of:
    1. The LARGEST value on the left half of the array :: [2, 1]
    2. The SMALLEST value on the right half of the array :: [3, 4]

    We can use two heaps:
      - MAX_HEAP :: LEFT_HALF
      - MIN_HEAP :: RIGHT_HALF
    
    Invariant: All items in the MIN_HEAP must be >= all items in the
    MAX_HEAP. This is required for the sorted property of the two
    sublists/heaps.

    For each number:
        Push elements into the MAX_HEAP by default

        If both heaps have elements and heads of MAX_HEAP is larger than
        MIN_HEAP:
            Move from MIN_HEAP to MAX_HEAP

        If MIN_HEAP has more elements:
            Move from MIN_HEAP to MAX_HEAP
        
        If MAX_HEAP has more elements:
            Move from MAX_HEAP to MIN_HEAP
    """
    
    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max, -num)

        if self.left_max and self.right_min and \
                (-self.left_max[0] > self.right_min[0]):
            heapq.heappush(
                self.right_min, -heapq.heappop(self.left_max)
            )
        
        if len(self.left_max) - len(self.right_min) > 1:
            heapq.heappush(
                self.right_min, -heapq.heappop(self.left_max)
            )
        elif len(self.right_min) - len(self.left_max) > 1:
            heapq.heappush(
                self.left_max, -heapq.heappop(self.right_min)
            )

    def findMedian(self) -> float:
        if len(self.left_max) > len(self.right_min):
            return -self.left_max[0]
        elif len(self.right_min) > len(self.left_max):
            return self.right_min[0]
        
        return (-self.left_max[0] + self.right_min[0]) / 2
        