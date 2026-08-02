import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        q = deque()  # (-freq, idleTime)
        time = 0

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = list(map(lambda x: -x, freq.values()))
        heapq.heapify(heap)

        # keep processing if q or heap is not empty
        while heap or q:
            time += 1

            if heap:
                # update the counts, incr by 1 as we run the task
                count_left = heapq.heappop(heap)
                count_left += 1
                
                if count_left < 0:
                    # append the new count and the next time we can
                    # run it again to the queue for waiting
                    q.append((count_left, time + n))
            
            # keep popping out and rejoining items that are
            # available for rescheduling
            while q and q[0][1] == time:
                count_left, next_time_to_run = q.popleft()
                heapq.heappush(heap, count_left)
        
        return time


        
        
