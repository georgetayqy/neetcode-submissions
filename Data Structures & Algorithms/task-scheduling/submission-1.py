import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        previous_task = {}
        heap = []

        for task in tasks:
            if task not in previous_task:
                previous_task[task] = 1
            else:
                previous_task[task] += (n + 1)
            heapq.heappush(heap, (previous_task[task], task))

        min_time = 0
        print(heap)
        while heap:
            freq, current = heapq.heappop(heap)

            if freq <= min_time:
                min_time += 1
            else:
                min_time = freq

            while heap and heap[-1][0] == freq:
                min_time += 1
                heapq.heappop(heap)

        return min_time
