from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        removed = set()
        indegrees = {i: set() for i in range(numCourses)}

        for src, dest in prerequisites:
            indegrees[dest].add(src)
        
        has_zero = False
        for node, indegree in indegrees.items():
            if len(indegree) == 0:
                has_zero = True
                q.append(node)
        
        if not has_zero:
            return False

        while q:
            current = q.popleft()
            removed.add(current)

            for node, indegree in indegrees.items():
                if current in indegree:
                    indegree.remove(current)

                if len(indegree) == 0 and node not in removed:
                    q.append(node)

        for src, indegree in indegrees.items():
            if len(indegree) != 0:
                return False
        
        return True
