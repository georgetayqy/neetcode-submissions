from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = {i: set() for i in range(numCourses)}
        q = deque()
        seen = set()
        order = []

        for _in, _out in prerequisites:
            ind[_in].add(_out)
        
        has_zero = False
        for src, indegree in ind.items():
            if len(indegree) == 0:
                has_zero = True
                q.append(src)
        
        if not has_zero:
            return []
        
        while q:
            current = q.popleft()
            
            if current in seen:
                continue
            
            seen.add(current)
            order.append(current)
            
            for src, indegree in ind.items():
                if src in seen:
                    continue

                if current in indegree:
                    indegree.remove(current)
                
                if len(indegree) == 0:
                    q.append(src)
        
        for i, indegree in ind.items():
            if len(indegree) > 0:
                return []
        
        return order
        