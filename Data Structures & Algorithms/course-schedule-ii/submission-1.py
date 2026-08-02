from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        q = deque()
        adj = {i: set() for i in range(numCourses)}
        indegrees = [0 for i in range(numCourses)]

        for src, dest in prerequisites:
            adj[dest].add(src)
            indegrees[src] += 1
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        traversed = 0

        while q:
            current = q.popleft()
            order.append(current)
            traversed += 1

            for dependent in adj[current]:
                indegrees[dependent] -= 1
            
                if indegrees[dependent] == 0:
                    q.append(dependent)
        
        return order if traversed == numCourses else []

            
