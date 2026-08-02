from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        adj = {i: set() for i in range(numCourses)}
        indegrees = [0 for i in range(numCourses)]
        seen_nodes = 0

        for src, dest in prerequisites:
            adj[dest].add(src)
            indegrees[src] += 1
        
        for node in range(numCourses):
            if indegrees[node] == 0:
                q.append(node)
        
        while q:
            current = q.popleft()
            seen_nodes += 1

            for dependent in adj[current]:
                indegrees[dependent] -= 1
            
                if indegrees[dependent] == 0:
                    q.append(dependent)

        return seen_nodes == numCourses
